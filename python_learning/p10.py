# Program to check if the alphabet is Vowel or Consonant

alphabet = input('Enter an alphabet to check if the alphabet is Vowel or Consonant: ')

alpha = alphabet.lower()

if alpha in ('a','e','i','o','u') :
    print(alphabet,'is a Vowel')
else:
    print(alphabet,'is a Consonant')