#####################################################################
#   Chunk number 1: Importing datas and experiment design ----
#####################################################################

# setting the wd
setwd('C:/Users/nicco/OneDrive/Documenti/Univeristy/Bioinformatics/Exam Project/Datas')

# uploading the files

counts <- read.delim(file = 'E-GEOD-52249-raw-counts.tsv',header = TRUE, row.names = 1) # gene id as rownames
counts <- counts[-1] # removing genes symnbols column 
head(counts) # checking everything is ok

sampledata <- read.delim(file = 'E-GEOD-52249-experiment-design.tsv',header = TRUE, row.names = 1, stringsAsFactors = TRUE)

'''
I was obtainig the error:
Error in DESeqDataSetFromMatrix(countData = counts, colData = sampledata,  : 
  rownames of the colData:
   SRR1028343,SRR1028344,SRR1028345,SRR1028346,SRR1028347,SRR1028348,SRR1028349 
  are not in the same order as the colnames of the countData:
   SRR1028343,SRR1028346,SRR1028347,SRR1028344,SRR1028349,SRR1028348,SRR1028345
so i sort the sampledata rows by rownames and counts coloumn by names
'''

sampledata <-sampledata[order(row.names(sampledata)), ] # sorting them by gene ids
counts <- counts[ , order(names(counts))]
sampledata
counts # just checking if they are correctly ordered to proceed with create the dds obj

#####################################################################
#   Chunk number 2: DESeqDataSetFromMatrix() function and DESeq pipeline ----
#####################################################################

library(DESeq2)
dds <- DESeqDataSetFromMatrix(countData = counts,
                              colData = sampledata,  
                              design = as.formula("~ Factor.Value.disease."))

dds # having a first look to the data - 58735 genes

# ill remove all the loe expressed genes that have less than 1 count as sum of all samples
keep <- rowSums(counts(dds)) > 1
dds <- dds[keep, ]
dds # now I have 38233 genes

# DESeq2 pipeline
dds <- DESeq(dds)

#####################################################################
#   Chunk number 3: PCA plot and Heatmap of sample to sample distances ----
#####################################################################



library(pheatmap) # charging the libraryes
library(ggplot2)
library(RColorBrewer)

### PCA Plot 

# using vst() function to normalize, it is more sensitive to library size than rlog
# it calculates a variance stabilizing transformation and transforms the count data
vsd <- varianceStabilizingTransformation(dds)

# plotting the PCA and seems that there is no miss classification of samples
plotPCA(vsd, intgroup = 'Factor.Value.disease.') + 
  theme_bw()

### Samples Distances Heatmap 

sampleDists <- dist(t(assay(vsd))) # to prosuce an analysis of distances of samples
sampleDists # matrixes of sample distances

sampleDistMatrix <- as.matrix( sampleDists )
colors <- colorRampPalette( rev(brewer.pal(9, "Blues")) )(255) # setting the colors for the heatmap

# creating the Heatmap
pheatmap(sampleDistMatrix,
         clustering_distance_rows = sampleDists,
         clustering_distance_cols = sampleDists,
         col = colors)
# darker is the color, more similiar are the samples
# trees represent the gerarchy of cluster
# same result of PCA plot, all samples seems to be correctly classified
# DS samples are similiar each other and same for Normal ones

#####################################################################
#   Chunk number 4: Comparison between the grops ----
#####################################################################

DEresults <- results(dds, contrast = c("Factor.Value.disease.", 'Down syndrome', 'normal'))
# specified the coloumn of sampledata (experimental design) that has the group classification
# Down syndrome vs Normal

summary(DEresults) # 5241 genes are over oxpressed in DS while 5374 underexpressed

DEresults <- DEresults[order(DEresults$pvalue), ] #  ordering the genes by pvalues
head(DEresults) # further looking at the results

# comparison of my results to results section of the Expression Atlas
# some examples:
DEresults['ENSG00000229807',]  # XIST gene - it gives a fold of -10 instead of -9.6 on publication
DEresults['ENSG00000184486',]  # POU3F2 gene - it gives a fold of -8.3 instead of -8 on publication
DEresults['ENSG00000105996',]  # HOXA2 gene - it gives a fold of -9.96 instead of -7.7 on publication
DEresults['ENSG00000164778',]  # - it gives a fold of -13.16 instead of -5.3 on publication
DEresults['ENSG00000175745',]  # NRF2F1 gene - it gives a fold of -6.8 instead of -6.6 on publication
DEresults['ENSG00000177853',]  # ZNF518A gene - it gives a fold of 8 instead of 7.9 on publication
# results are very similiar despite that some genes have log2 fold change 
# twice the result of the study (as ENSG00000164778)

#####################################################################
#   Chunk number 5: More Plots!! ----
#####################################################################

### Volcano plot with *EnhancedVolcano*

library(EnhancedVolcano)

DEresults$symbol <- mapIds(org.Hs.eg.db,      # Here im adfding the gene names also on
                           keys=rownames(DEresults), # on the obj 'DEresults' to use the gene
                           column="SYMBOL",          # names as label on the plot
                           keytype="ENSEMBL",
                           multiVals="first")

EnhancedVolcano(DEresults,
                lab = DEresults$symbol,
                x = 'log2FoldChange',
                y = 'pvalue',
                title = 'Down syndrome versus Normal',
                pCutoff = 0.05,
                FCcutoff = 2,
                pointSize = 3.0,
                cutoffLineType = 'twodash',
                col = c('medium blue', 'steel blue', 'dodger blue', 'sky blue'),
                legendPosition = 'bottom',
                drawConnectors = TRUE,
                widthConnectors = 0.756,
                labSize = 5.0) + coord_flip()
### MA plot

plotMA(object = DEresults, ylim = c(-13, 13), main = 'MA Plot', colSig = "sky blue")

#####################################################################
#   Chunk number 6: Gene Ontology (GO) Enrichment Analysis ----
#####################################################################

### Enrhichment analysis

DEresults <- DEresults[!is.na(DEresults$padj),] # I eliminate genes with NA values in adj pvalue
DE <- DEresults[DEresults$padj < 0.1,] # selecting only the genes with adj pvalue lower than 0.1
DE <- DE[abs(DE$log2FoldChange) > 1,] # selecting genes that are over/under expressed
# absoolute value of log2 fold change higher than 1
summary(DE) 
# 5682 genes with log2 fold change higher than 1 or lower than -1
# and with a adj pvalue lower than 0.1
head(DE)

# addition of the gene symbol for the Gene ontology analysis
library("AnnotationDbi")
library("org.Hs.eg.db")

DE$symbol <- mapIds(org.Hs.eg.db, # becous the sample are form Humans
                    keys=rownames(DE),
                    column="SYMBOL",
                    keytype="ENSEMBL",
                    multiVals="first")

DE_up <- DE[DE$log2FoldChange > 1,] # creating two data sets
DE_down <- DE[DE$log2FoldChange < -1,] # one for Up regulated and one for Down

summary(DE_up) # 2400 genes are UP regulated
summary(DE_down) # 3282 genes are DOWN regulated

library(clusterProfiler)

### Analysis and plots

# for UP regulated ones:
GO_BP <- enrichGO(DE$symbol, OrgDb = "org.Hs.eg.db", 
                  keyType = "SYMBOL", ont = "BP")
GO_MF <- enrichGO(DE_up$symbol, OrgDb = "org.Hs.eg.db", 
                  keyType = "SYMBOL", ont = "MF")
GO_CC <- enrichGO(DE_up$symbol, OrgDb = "org.Hs.eg.db", 
                  keyType = "SYMBOL", ont = "CC")


dotplot(GO_BP, title = "Biological Process")
dotplot(GO_MF, title = "Molecular Functions")
dotplot(GO_CC, title = "Cellular Component")


# for DOWN regulated ones:

GO_BP <- enrichGO(DE_down$symbol, OrgDb = "org.Hs.eg.db", 
                  keyType = "SYMBOL", ont = "BP")
GO_MF <- enrichGO(DE_down$symbol, OrgDb = "org.Hs.eg.db", 
                  keyType = "SYMBOL", ont = "MF")
GO_CC <- enrichGO(DE_down$symbol, OrgDb = "org.Hs.eg.db", 
                  keyType = "SYMBOL", ont = "CC")


dotplot(GO_BP, title = "Biological Process")
dotplot(GO_MF, title = "Molecular Functions")
dotplot(GO_CC, title = "Cellular Component")

# THE END


DiffExp <- DEresults[DEresults$padj < 0.05 & abs(DEresults$log2FoldChange) > 0,]
summary(DiffExp)
write.table(DiffExp,"Differentially Expressed Genes", sep="\t", row.names=TRUE)

setwd('C:/Users/nicco/OneDrive/Documenti/Univeristy/Bioinformatics/Exam Project/Final Project')
count_ <- read.delim(file = 'Differentially Expressed Genes',header = TRUE)
head(count_) 

