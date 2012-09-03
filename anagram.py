import fileinput
import collections

def list_anagrams(word_file):
    word_index = collections.defaultdict(list)
    anagram_index = {}
    for word in fileinput.input([word_file]):
        word = word[:-1]
        i = ''.join(sorted(word))
        word_index[i].append(word)
        if len(word_index[i]) > 1:
            anagram_index[i] = i
            
    for i in anagram_index:
        print ' '.join(map(str,  word_index[i]))

if __name__ == "__main__":
    list_anagrams('wordlist.txt')

