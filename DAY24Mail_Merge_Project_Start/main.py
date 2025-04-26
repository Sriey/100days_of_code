#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

file_letter = open("./Input/Letters/starting_letter.txt", mode="r")
letter = file_letter.readlines()
print(letter)
file_letter.close()

file_name = open("./Input/Names/invited_names.txt", mode="r")
name = list(map(str, file_name.read().split()))
file_name.close()

prev = "[name]"
for i in name:
    j = prev
    prev = i
    letter[0] = letter[0].replace(j, i)
    file_new = open(f"./Output/ReadyToSend/letter_for_{i}.txt", mode="w")
    file_new.write("".join(letter))
    file_new.close()
