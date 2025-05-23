"""
Solutions to assignment 3
"""

"""
1.Write a Python program to reverse the string "Programming". Print the reversed string.
Hint: Use string slicing or a loop.
"""
string1 = "Programming"
reversed_string = string1[::-1]
print("Reversed string:", reversed_string)



"""
2.Create a Python program that takes a user’s full name as input and prints the initials in uppercase.
Example: Input: "john doe", Output: "J.D."
"""
full_name = input("Enter your full name: ")
initials = '.'.join([name[0].upper() for name in full_name.split()]) + '.'
print("Initials:", initials)




"""
3.Write a Python program to check if a given string is a palindrome. A palindrome reads the same forwards
and backward (e.g., "radar", "level"). Hint: Compare the string with its reverse.
"""
string2 = input("Enter a string to check for palindrome: ")
if string2 == string2[::-1]:
    print("It is a palindrome.")
else:
    print("It is not a palindrome.")



"""
4.Create a Python program that asks the user to enter a sentence and counts the number of words in the sentence.
Hint: Use the split() method to break the string into words.
"""
sentence = input("Enter a sentence: ")
word_count = len(sentence.split())	
print("Number of words:", word_count)




"""
5.Write a Python program to replace all occurrences of "is" with "was" in the string "This is a string and it
is an example." Print the modified string.
"""
string3 = "This is a string and it is an example."
modified_string = string3.replace(" is", " was")
print("Modified string:", modified_string)
