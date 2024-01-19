
with open('words.txt') as my_words:
    words = set(my_words.read().split())
from tqdm import tqdm #da una barra per vedere il completamento del programma quando avvii
#importare il dizionario
start_word='head'
end_word='tail'
candidate_words=[]
#add to candidate_words all the words that have th esame lenght
for word in words:
    if len(word)==4:
        candidate_words.appened(word)
set_of_words = []

#Function that return how many letters the words differ
def check_word(start, this_word):
    counter = 0
    for pos in range(len(start)):
        if start[pos] != this_word[pos]:
            counter += 1
    return counter

#now cereate  list of words that contain all words of same lenght differing just by one letter
for words in candidate_words:
    if check_word(start_word, word) == 1:
        set_of_words.append(word)
#now i have a list of all words that differ by one letter
#i should check if the world is inside but it isnt so i go on

#do the same as beafore but for words in set_of_words
new_set_of_words=[]
for new_start_word in set_of_words:
    for words in candidate_words:
        if check_word(new_start_word, word) == 1:
            new_set_of_words.append(word)
#so this is the list of words that differ by two letters from start_word
#but end_words is not inside

def compare_words(start_word, end_word):
    if len(start_word) != len(end_word):
        return False
    
    candidate_words = []
    for word in words:
        if len(word) == len(start_word):
            candidate_words.append(word)
        
    set_of_words = [start_word]
    while end_word not in set_of_words and len(set_of_words) < len(candidate_words):
        print('---- new round ---- words to check ', len(set_of_words))
        new_set_of_words = []
        for new_start_word in tqdm(set_of_words):
            for word in candidate_words:
                if check_word(new_start_word, word) == 1:
                    new_set_of_words.append(word)

        set_of_words = new_set_of_words

    return end_word in set_of_words

#n possible candidate words
#l lenght of our word
#k number of times we have to create a now list of words that differ by one more letters
# n^k is the number of operation we need to do, it is called complexity
