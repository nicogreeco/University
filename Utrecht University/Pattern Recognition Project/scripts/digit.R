



#### - LIBRARY AND FUNCTIONS - #####

library(tidyverse)
library(magrittr)
library(nnet)
library(caret)
library(glmnet)
library(e1071)

show_row <- function(row) {
  OpenImageR::imageShow(matrix(as.numeric(row[-1]),nrow=28,ncol=28,byrow=T))
}

getMaxClass <- function(pred_probs) {
  max_class <- apply(pred_probs, 1, which.max)
  max_class <- max_class -1
  return(max_class)
}

#### - QUESTION 1 - #####

mnist.dat <- read.csv("mnist.csv")

dim(mnist.dat)

## SUMMARY STATISTIC AND USELESS PIXEL ##

summary.stat <- sapply(mnist.dat, summary) %>% t()


# identical(summary.stat[,1]==summary.stat[,6], summary.stat[,4]==0)


useless.pixel <- (summary.stat[,1]==summary.stat[,6])


sum(useless.pixel)
# 76 useless pixels are found, thir minimum is equal to their maximum


useless.pixel.name <- names(useless.pixel[useless.pixel])

## CLASS DISTRIBUTION ##

mnist.dat$label <- as.factor(mnist.dat$label) 


table(mnist.dat$label)


class.distribution <- table(mnist.dat$label)
# most frequent is class 1


accuracy_predicting_major <- class.distribution["1"]/sum(class.distribution) * 100


#### - QUESTION 2 - #####


## INK COLUMN ##


mnist.dat.ink <- mnist.dat


mnist.dat.ink$ink <- c()


mnist.dat.ink$ink <- apply(mnist.dat.ink, 1, function(row) sum(as.integer(row[-1])))


## INK COLUMN ##


nested.mean <- mnist.dat.ink %>% group_by(label) %>% select(ink) %>% summarise_all(mean) %>% rename(mean.ink=ink)


nested.sd <- mnist.dat.ink %>% group_by(label) %>% select(ink) %>% summarise_all(sd) %>% rename(sd.ink=ink)


ink.stat.per.label <- merge(nested.mean, nested.sd, by = "label")


mnist.dat.ink %<>% left_join(nested.mean, by = "label") %>% left_join(nested.sd, by = "label")


head(mnist.dat.ink[,c(1,786,787,788)])

show_row(mnist.dat.ink[5,])
show_row(mnist.dat.ink[6,])



## MODEL FITTING ##


## --- on the whole dataset --- ##

    # - TRAIN - #


mnist.dat.ink$ink.scaled <- scale(mnist.dat.ink$ink)


multi.logit.ink.only <- multinom(label ~ ink.scaled, data = mnist.dat.ink)


    # - TEST - #


predictions.whole.data <- predict(multi.logit.ink.only, newdata = mnist.dat.ink)


table(mnist.dat.ink$label, predictions.whole.data)

## --- only for some class --- ##

    # - TRAIN - # 


multi.logit.ink.only.1.8 <- multinom(label ~ ink.scaled, data = mnist.dat.ink[mnist.dat.ink$label %in% c(1,8),])


multi.logit.ink.only.4.0 <- multinom(label ~ ink.scaled, data = mnist.dat.ink[mnist.dat.ink$label %in% c(4,0),])


multi.logit.ink.only.3.8 <- multinom(label ~ ink.scaled, data = mnist.dat.ink[mnist.dat.ink$label %in% c(3,8),])


    # - TEST - #

prediction.ink.only.1.8 <- predict(multi.logit.ink.only.1.8, newdata = mnist.dat.ink[mnist.dat.ink$label %in% c(1,8),])


prediction.ink.only.4.0 <- predict(multi.logit.ink.only.4.0, newdata = mnist.dat.ink[mnist.dat.ink$label %in% c(4,0),])


prediction.ink.only.3.8 <- predict(multi.logit.ink.only.3.8, newdata = mnist.dat.ink[mnist.dat.ink$label %in% c(3,8),])


table(mnist.dat.ink[mnist.dat.ink$label %in% c(1,8),"label"], prediction.ink.only.1.8)
confusionMatrix(data = prediction.ink.only.1.8, reference = mnist.dat.ink[mnist.dat.ink$label %in% c(1,8), "label"])

table(mnist.dat.ink[mnist.dat.ink$label %in% c(4,0),"label"], prediction.ink.only.4.0)


table(mnist.dat.ink[mnist.dat.ink$label %in% c(3,8),"label"], prediction.ink.only.3.8)

# -- probabilities -- #

predictions.prob <- predict(multi.logit.ink.only, newdata = mnist.dat.ink, type = "probs") %>% as.data.frame()


predictions.prob$label <- mnist.dat.ink[, "label"]


predictions.prob$prediction <- predictions.whole.data


sum(predictions.prob$label == predictions.prob$prediction)/nrow(predictions.prob)


#### - QUESTION 3 - #####


features <- mnist.dat[,!useless.pixel]


pca_result <- prcomp(features[,-1], center = TRUE, scale. = TRUE)

# first_pc <- pca_result$x[, 1]

projection_1pc <- as.vector(as.matrix(features[,-1]) %*% pca_result$rotation[, 1])
projection_2pc <- as.vector(as.matrix(features[,-1]) %*% pca_result$rotation[, 2])

mnist.dat.ink <- cbind(mnist.dat.ink, PC1_Projection = projection_1pc)
mnist.dat.ink <- cbind(mnist.dat.ink, PC2_Projection = projection_2pc)


str(mnist.dat.ink[,c(1,2,785:790)])


multi.logit.ink.PC1 <- multinom(label ~ ink.scaled + PC1_Projection, data = mnist.dat.ink)
multi.logit.ink.PC2 <- multinom(label ~ ink.scaled + PC2_Projection, data = mnist.dat.ink)

plot(mnist.dat.ink$ink, mnist.dat.ink$PC1_Projection)

ggplot(mnist.dat.ink, aes(x=ink, y=PC1_Projection, color = label)) +
  geom_point(size=2, shape=23)

predictions.whole.data.PC1 <- predict(multi.logit.ink.PC1, newdata = mnist.dat.ink)


predictions.prob.PC1 <- predict(multi.logit.ink.PC1, newdata = mnist.dat.ink, type = "probs") %>% as.data.frame()


predictions.prob.PC1$label <- mnist.dat.ink[, "label"]


predictions.prob.PC1$prediction <- predictions.whole.data.PC1

sum(predictions.prob.PC1$label == predictions.prob.PC1$prediction)/nrow(predictions.prob.PC1)

#### - QUESTION 5 - ####



set.seed(1234)
train.mnist.dat <- mnist.dat %>% sample_n(5000)
test.mnist.dat <- mnist.dat %>% anti_join(train.mnist.dat)



## - MULTI LOGIT ON ALL PIXEL  - ##

response.all.pixel <- as.integer(as.character(train.mnist.dat[, 1]))  # Extract the response variable (label)

predictors.all.pixel <- as.matrix(train.mnist.dat[, -1])  # Extract predictors (exclude the first column)

cv.multi.logit.all.pixel <- cv.glmnet(x = predictors.all.pixel, y = response.all.pixel, 
                           family = "multinomial", nfolds = 15, alpha = 1)
plot(cv.multi.logit.all.pixel)

multi.logit.all.pixel <- coef(cv.multi.logit.all.pixel, s = "lambda.min")

predictions.logit.all.pixel.test <- predict(cv.multi.logit.all.pixel, 
                                            newx = as.matrix(test.mnist.dat[,-1]), s = "lambda.min", type = "response") %>% 
                                                as.data.frame()

names(predictions.logit.all.pixel.test) <- sub("\\..*", "", names(predictions.logit.all.pixel.test))

predictions.logit.all.pixel.test$prediction <- as.factor(getMaxClass(predictions.logit.all.pixel.test[,1:10]))

confusionMatrix(data = predictions.logit.all.pixel.test$prediction, reference = test.mnist.dat$label)




## - MULTI LOGIT ON NON-ZERO VARIANCE PIXEL  - ##

response.some.pixel <- as.integer(as.character(train.mnist.dat[, 1]))  # Extract the response variable (label)

predictors.some.pixel <- train.mnist.dat[, !useless.pixel] %>% select(-label) %>% as.matrix() # Extract predictors (exclude the first column)

test.some.pixel <- test.mnist.dat[, !useless.pixel] %>% select(-label) %>% as.matrix()
  
cv.multi.logit.some.pixel <- cv.glmnet(x = predictors.some.pixel, y = response.some.pixel, 
                                   family = "multinomial", nfolds = 15, alpha = 1)
plot(cv.multi.logit.some.pixel)

predictions.logit.some.pixel.test <- predict(cv.multi.logit.some.pixel, 
                                            newx = test.some.pixel, s = "lambda.min", type = "response") %>% 
                                                as.data.frame()

names(predictions.logit.some.pixel.test) <- sub("\\..*", "", names(predictions.logit.some.pixel.test))

predictions.logit.some.pixel.test$prediction <- as.factor(getMaxClass(predictions.logit.some.pixel.test[,1:10]))

confusionMatrix(data = predictions.logit.some.pixel.test$prediction, reference = test.mnist.dat$label)


## - SVM ON NON-ZERO VARIANCE PIXEL  - ##

train.mnist.some.pixel <- train.mnist.dat[, !useless.pixel]
test.mnist.some.pixel <- test.mnist.dat[, !useless.pixel]

# Tune differnt type of models

## 3 svm with radial kernel and different ranges of parameters
cv.svm.some.pixel <- tune.svm( label ~ ., data = train.mnist.some.pixel, gamma = 10^(-6:-1), cost = 10^(1:2))
plot(cv.svm.some.pixel)

cv.svm.some.pixel.2 <- tune.svm( label ~ ., data = train.mnist.some.pixel, gamma = 10^(-10:1), cost = 10^(-1:3))
plot(cv.svm.some.pixel.2)

cv.svm.some.pixel.3 <- tune.svm( label ~ ., data = train.mnist.some.pixel, gamma = c(0.005,0.01,0.015,0.02,0.025,0.03,0.035,0.04,0.045,0.05), cost = 2^(0:5))
plot(cv.svm.some.pixel.3)

# tune.svm with linear kernel
cv.svm.linear.some.pixel <- tune.svm(label ~ ., data = train.mnist.some.pixel, kernel = "linear", cost = 10^(0:4))
plot(cv.svm.linear.some.pixel)

# tune.svm with polynomial kernel
cv.svm.polynomial.some.pixel <- tune.svm(label ~ ., data = train.mnist.some.pixel, kernel = "polynomial", degree = c(2:3), cost = 10^(0:4))
plot(cv.svm.polynomial.some.pixel)

models_list <- list(
  cv.svm.some.pixel = list(tune.svm = cv.svm.some.pixel),
  cv.svm.some.pixel.2 = list(tune.svm = cv.svm.some.pixel.2),
  cv.svm.some.pixel.3 = list(tune.svm = cv.svm.some.pixel.3),
  cv.svm.linear.some.pixel = list(tune.svm = cv.svm.linear.some.pixel),
  cv.svm.polynomial.some.pixel = list(tune.svm = cv.svm.polynomial.some.pixel)
)


for (i in names(models_list)) {
  best.svm <- models_list[[i]][["tune.svm"]]$best.model
  best.param.svm <- models_list[[i]][["tune.svm"]]$best.parameters
  
  # Make predictions on test data using each model
  predictions <- predict(best.svm, newdata = test.mnist.some.pixel) %>% unlist()
  
  # Create confusion matrix
  confusion_matrix <- confusionMatrix(data = predictions, reference = test.mnist.some.pixel$label)
  
  # Save predictions and confusion matrix in the models_list
  models_list[[i]]$predictions <- predictions
  models_list[[i]]$confusion.matrix <- confusion_matrix
  models_list[[i]]$best.parameters <- best.param.svm
  # Print model name, best parameters, and confusion matrix
  cat("Confusion matrix for", i, ":\n")
  cat("\n")
  cat("Best parameters are: ","\n")
  print(best.param.svm)
  cat("\n")
  print(confusion_matrix)
  cat("------------------------------------------------------------------------------------------")
  cat("\n")
  cat("\n")
}

models_list[[4]][["tune.svm"]]
summary.stat.svm <- train.mnist.some.pixel  %>% mutate(label = as.integer(as.character(label))) %>% sapply(summary) %>% t()


useless.pixel.svm <- (summary.stat.svm[,1]==summary.stat.svm[,6])


sum(useless.pixel.svm)
# 44 useless pixels are found, thir minimum is equal to their maximum


useless.pixel.name.svm <- names(useless.pixel.svm[useless.pixel.svm])


train.mnist.no.zero.sd.pixel <- train.mnist.some.pixel[, !useless.pixel.svm]
test.mnist.no.zero.sd.pixel <- train.mnist.some.pixel[, !useless.pixel.svm]


train.mnist.no.zero.sd.pixel  %>% mutate(label = as.integer(as.character(label))) %>% sapply(summary) %>% t()

cv.svm.no.zero.sd.pixel.final <- tune.svm(label ~ ., data = train.mnist.no.zero.sd.pixel, gamma = c(10^-8,10^-7,10^-6,10^-5), cost = c(10,50,100,200))
plot(cv.svm.no.zero.sd.pixel.final)
cv.svm.no.zero.sd.pixel.final$performances

cv.svm.no.zero.sd.pixel.final.2 <- tune.svm(label ~ ., data = train.mnist.no.zero.sd.pixel, gamma = c(10^-9,10^-6), cost = c(10, 1000))
plot(cv.svm.no.zero.sd.pixel.final.2)
cv.svm.no.zero.sd.pixel.final.2$performances

cv.svm.no.zero.sd.pixel.final.3 <- tune.svm(label ~ ., data = train.mnist.no.zero.sd.pixel, gamma = c(10^-9,10^-6), cost = c(10, 1000))
plot(cv.svm.no.zero.sd.pixel.final.3)
cv.svm.no.zero.sd.pixel.final.3$performances

cv.svm.no.zero.sd.pixel.final.4 <- tune.svm(label ~ ., data = train.mnist.no.zero.sd.pixel, gamma = c(10^-8,10^-7,10^-6,10^-5), cost = c(1,10,50,100))
plot(cv.svm.no.zero.sd.pixel.final.4)
cv.svm.no.zero.sd.pixel.final.4$performances

predictions.svm.no.zero.sd.pixel <- predict(cv.svm.no.zero.sd.pixel$best.model, newdata = test.mnist.no.zero.sd.pixel) %>% unlist()

# Create confusion matrix
confusion_matrix <- confusionMatrix(data = predictions.svm.no.zero.sd.pixel, reference = test.mnist.no.zero.sd.pixel$label)


for (i in names(models_list)) {
  cat("Performance for", i, ":\n")
  print(models_list[[i]][["tune.svm"]]$performances)
  print(models_list[[i]][["tune.svm"]]$best.parameters)
  #print(models_list[[i]][["confusion.matrix"]])
  cat("\n")
  cat("------------------------------------------------------------------------------------------")
  cat("\n")
  cat("\n")
}
