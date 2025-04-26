import pandas

file = pandas.read_csv("nato_phonetic_alphabet.csv")

temp_dict = {code.letter:code.code for (letter,code) in file.iterrows()}

def B():
    try:
        word = (input("Enter a Word :")).upper()
        result = [temp_dict[x] for x in word]
    except KeyError:
        print("Sorry, Only Letters in the Word Please.")
        B()
    else:
        print(result)

B()