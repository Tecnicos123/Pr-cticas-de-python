'''
The following code sorts words in alphabetical order
'''
# Taking user input
sentence = input("Enter a sentence: ")
# Splitting the sentence into words
words = sentence.split()
# Sorting the words in alphabetical order
words.sort()
# Printing the sorted words
print("Sorted words in alphabetical order:")        
for word in words:
    print(word)
# Output the sorted words