# write a function to find the count of word in a sentence
def count_words():
    sentence = input("Enter a sentence: ")
    words = sentence.split()
    print("Number of words in the sentence:", len(words))

count_words()
