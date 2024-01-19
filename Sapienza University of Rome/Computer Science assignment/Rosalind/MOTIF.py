import urllib.request
with open('C:/Users/nicco/Downloads/rosalind_mprt.txt') as txt:
    record_dict = {}
    for pid in txt:
        protid = pid.replace('\n', '')
        url = "https://www.uniprot.org/uniprot/"+ protid +'.fasta' 
        #  read directly from the url of the txt the amminoacid sequences
        data = urllib.request.urlopen(url).readlines()[1:]  # cut first line so only the amminoacid seq
        n = 0
        while n < len(data):
            data[n] = data[n].decode("utf-8", "ignore")  # correctly convert it in str
            data[n] = data[n].replace('\n', '')
            n += 1
        fasta = ''.join(data) 
          # probably is not the best way to do it but that's what I was able to do

        record_dict[protid] = fasta

# fing glycosidic motif
solution_dict = {}
for protid in record_dict:
    n = 0
    solution_dict[protid] = [] # dict that has as key the protein id and as value
    while n < (len(record_dict[protid])-4): # a list with position of the motif
        if record_dict[protid][n] == 'N':
            if record_dict[protid][n+1] != 'P':                
                if record_dict[protid][n+2] == 'S' or record_dict[protid][n+2] == 'T':
                    if record_dict[protid][n+3] != 'P':                        
                        solution_dict[protid].append(str(n+1))
        n += 1

for protid in solution_dict:
    if solution_dict[protid] != []:  # printing solutions
        print(protid)
        print(' '.join([i for i in solution_dict[protid]]))

