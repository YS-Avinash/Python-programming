"""Python function which accepts a sentence and finds the number of letters and digits in the sentence.
It should return a list in which the first value should be letter count and second value should be digit count. 
Ignore the spaces or any other special character in the sentence."""


def count_digits_letters(sentence):
    #start writing your code here
    num_count , char_count = 0 , 0
    for char in sentence:
        if char.isdigit():
            num_count += 1
        elif char.isalpha():
            char_count += 1
    
    return [char_count,num_count]

sentence="Infosys Mysore 570027"
print(count_digits_letters(sentence))
