# user inputs any number
number = input("Enter a number")
# a dictionary containing the word equivalent for numbers ranging from 0 to 9
numbers = {
    "0": "zero",
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four",
    "5": "five",
    "6": "six",
    "7": "seven",
    "8": "eight",
    "9": "nine",
}
# an empty list is created
answer = []
# iterates through the number the user inputs and fins the word equivalent for each in the dictionary
for i in number:
    result = numbers.get(i)
    # word equivalent of the number is put in the empty list
    answer.append(result)
# outputs word list of numbers inputted
print(answer)


