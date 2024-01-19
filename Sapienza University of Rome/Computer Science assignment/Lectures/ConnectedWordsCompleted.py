with open('words.txt') as my_words:
    words = set(my_words.read().split())
from tqdm import tqdm

def check_word(start, this_word):
    counter = 0
    for pos in range(len(start)):
        if start[pos] != this_word[pos]:
            counter += 1
    return counter

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

compare_words('head','tail')

#n possible candidate words
#l lenght of our word
#k number of times we have to create a now list of words that differ by one more letters
# n^k is the number of operation we need to do, it is called complexity