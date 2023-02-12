# a function that accepts a word, and a sentence as arguments, and returns the number of times the word occurs in the sentence.
def count_word(word,sentence):                 # This defines a function 'count_word' with parameters 'word' and 'sentence'
    words_in_sentence = sentence.split()       # This turns the string of 'sentence' into a list of words
    return words_in_sentence.count(word)       # this returns the number of occurrences of 'word' in the list of words

count_word("sea", "She sells sea shells on the sea shore when the sea is calm.")

# finding the word that occurs the maximum number of times in a sentence inputted by a user

sentence_input = input("Input a sentence: ")                                      # This asks the user for a sentence input
sentence_input = sentence_input.lower()  # ensures all the words are lowercase so that 'She' and 'she' would be counted together
sentence_split = sentence_input.split()                     # this turns the user input into a list of words that can be counted
list_of_word_counts = []                                    # creates list_of_word_counts

for word in sentence_split:                                        # for each word in the list of words from the user input...
    list_of_word_counts.append(count_word(word, sentence_input))   # adds the word count for each word to list_of_word_counts
    
max_word_count = max(list_of_word_counts)                                         # finds the highest value for word count
max_word_word = sentence_split.pop(list_of_word_counts.index(max_word_count))     # matches the highest word count with its word

print("The word with the maximum number of occurences is", "'"+max_word_word+"'","and it occurs", max_word_count ,"times.")