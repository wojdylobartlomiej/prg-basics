###
# String manipulation
#

movie = "The Lord of the Rings: The Return of the King"

# print number of characters
print('Number of characters: ', len(movie))

# print title in capital letters
print("Duze litery " ,movie.upper())

# print title in small letters
print("Male litery " ,movie.lower())

# print how many times the vowel "e" appears in the title
print("znajdz ile e   ",movie.count('e'))
# print where in the text is the word "Lord"
print("znajdz lord  ",movie.find("Lord"))

# print where in the text is the word "dragon"
print("znakjdz dragon    : ",movie.find("dragon"))