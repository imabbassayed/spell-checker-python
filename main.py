import os.path #Python built in library used here to check if the filename user enters, exists or does not exist.
import re #Python built in library used here to remove numbers, apostrophes, commas.
from difflib import SequenceMatcher # Python built in library used here to give the suggested word.
from datetime import datetime # Python built in library used here to get the date, time and to calculate the elpased time.

restart = True

def getUserChoice(): # Start of the program and the funtion that gets the user choice whether they want to check a sentence or file
    restart = False
    try:
        print("-------------------------------------------------------")
        print("|                    SPELL CHECKER !                   |")
        print("-------------------------------------------------------")
        print("|   I can SPELL CHECK any sentence or file for you :)  |")
        print("-------------------------------------------------------")
        print("|Enter 1 if you want me to spell check a sentence      |")
        print("|Enter 2 if you want me to spell check a file          |")
        print("|Enter 0 if you want me to quit :(                     |")
        print("-------------------------------------------------------")
        tasknum = int(input("Lets get started ! Choose one of the options : "))
        print("-------------------------------------------------------")

        if tasknum < 0 or tasknum > 3: # If function to make sure the input is either 0, 1, 2
            print("")
            print("Oops!  Try again...")
            print("Please enter 0, 1 or 2 and nothing else !")
            print("")
            restart = True
        elif tasknum == 1:
            print("Hmm... So you want me to spell check a sentence      ")
            print("-------------------------------------------------------")
            sentence = input("So what's your sentence ?! ")
            print("-------------------------------------------------------")
            preSpellCheck1(sentence); # Go to the function that splits the sentence into words and removes everything from the words other than the characters and makes all the characters lowercase
        elif tasknum == 2:
            print("Hmm... So you want me to spell check a file      ")
            print("-------------------------------------------------------")
            while True:
                fname = input("So what's your filename ? ")
                print("-------------------------------------------------------")
                if os.path.isfile(fname)== True:
                    preSpellCheck2(fname); # Go to the function that reads the file and then splits the sentence into words and removes everything from the words other than the characters and makes all the characters lowercase
                    break
                else:
                    print("")
                    print("Thats so sad , the files does not exist !")
                    print("Oops!  Try again...")
                    print("Enter 1 if you want to try again...")
                    print("Enter 2 if you want to me to go to the initial menu !")
                    print("")
                    print("-------------------------------------------------------")
                    while True: # Loop with try and except to validate the user input if they typed something inappopriate
                        try:
                            userChoice = int(input("So, please choose one of the options : "))
                            print("-------------------------------------------------------")
                            if userChoice == 2:
                                restart = True
                                break

                            elif userChoice == 1:
                                break
                            else:
                                print("")
                                print("Oops!  Try again...")
                                print("Please enter 1 or 2 and nothing else !")
                                print("")

                        except ValueError:
                            print("")
                            print("Oops!  Try again...")
                            print("Please enter 1 or 2 and nothing else !")
                            print("")
                            continue
                        break
                if userChoice == 2:
                    break
        elif tasknum == 0:
            print("-------------------------------------------------------")
            print("Hoping to see you soon :-)")
            print("-------------------------------------------------------")
            quit()

    except ValueError: #Expect to start the program again if the users enter anything other than integer
        print("")
        print("Oops!  Try again...")
        print("Please enter 0, 1 or 2 and nothing else !")
        print("")
        restart = True

def preSpellCheck1(sentence): #Function that splits the user sentence into words and removes everything from the words other than the characters and make all the characters lowercase
    starttime = datetime.now() # Varibale to the store the date and time the program started spell checking
    print("Below are the words you provided me -->")
    print(sentence)
    print("-------------------------------------------------------")
    print("|       I will start now and spell check for you !    |")
    print("-------------------------------------------------------")
    lowerCaseSentece = sentence.lower() # Makes the sentence lower case
    wordsToSpellCheck = [re.sub(r"[^a-z]+", '', k) for k in lowerCaseSentece.split(" ")] # Splits the sentence by the whitespace into list of words and keeps the characters from a-z and removes the rest
    spellcheck(wordsToSpellCheck,starttime,sentence) # Calls the main spell check function

def preSpellCheck2(fname): #Function that reads the file and then splits  sentence into words and removes everything from the words other than the characters and make all the characters lowercase
    starttime = datetime.now() # Varibale to the store the date and time the program started spell checking
    file = open(fname) # Opens the file
    sentence = file.read() # Reads the file and assigns it to the varibale
    file.close() # Closes the file
    print("Below are the words you provided me -->")
    print(sentence)
    print("-------------------------------------------------------")
    print("|       I will start now and spell check for you !    |")
    print("-------------------------------------------------------")
    lowerCaseSentece = sentence.lower() # Makes the sentence lower case
    wordsToSpellCheck = [re.sub(r"[^a-z]+", '', k) for k in lowerCaseSentece.split(" ")] # Splits the sentence by the whitespace into list of words and keeps the characters from a-z and removes the rest
    spellcheck(wordsToSpellCheck,starttime,sentence) # Calls the main spell check function

def spellcheck(wordsToSpellCheck,starttime,sentence): # Main spell checking Function
    totalWords = len(wordsToSpellCheck) # Counts the total number of words
    correctWords = 0 # Variable for correct words
    incorrectWords = 0 # Variable for incorrect words
    with open('EnglishWords.txt') as file: # Opens the dictionary file
        dictionaryContents = file.read() # Reads the dictionary file
        dictionaryContentsList = dictionaryContents.splitlines() # Splits the sentence by the whitespace into list of words and keeps the characters from a-z and removes the rest
        markedWordsList = []; # List to store the words that we marked
        addedToDic = 0 # Varibale to store the number of words added to the dictionary
        accepetedSuggestion = 0  # Varibale to store the number of words added to the dictionary
        for eachword in wordsToSpellCheck:  # For loop to check if the word exists in dictionary
            if eachword in dictionaryContents:
                print (eachword)
                correctWords += 1
            else:
                while True:
                    try: # Ask the user what to do when a wrong word is encountered !
                        print(eachword)
                        print("-------------------------------------------------------")
                        print("|           Ops ! Incorrecly spelled word found       |")
                        print("-------------------------------------------------------")
                        print ('The word "'+eachword+'" was not found in the dictionary !')
                        print("Enter 1 if you want me to ignore the word")
                        print("Enter 2 if want me to mark the word with a question mark in the end")
                        print("Enter 3 if you want to add the word to the dictionary")
                        print("Enter 4 if you want me to give you a possible suggestion")
                        print("-------------------------------------------------------")
                        userChoice = int(input("Enter the desired number :  "))
                        print("-------------------------------------------------------")

                        if userChoice == 1: # if functions that gets executed based on the user choice
                            incorrectWords +=1
                            break
                        elif userChoice == 2:
                            incorrectWords +=1
                            markedWordsList.append(eachword+"?")
                            break
                        elif userChoice == 3:
                            correctWords += 1
                            addedToDic +=1
                            dictionaryFile = open("EnglishWords.txt","a")
                            dictionaryFile.write("\n")
                            dictionaryFile.write(eachword)
                            break
                        elif userChoice == 4:

                            ratiolist=[]
                            for eachsuggestion in dictionaryContentsList: # for loop to find the suggestion word
                                 ratio = SequenceMatcher(None, eachword, eachsuggestion).ratio() # A function that compares everyword in the dictionary with the wrong word to see which one is the closest
                                 ratiolist.append(ratio)
                            print(dictionaryContentsList[ratiolist.index(max(ratiolist))]) # DIsplaying the suggested word
                            while True:
                                try:
                                    print("Enter 1 if you want to accept the suggested word")
                                    print("Enter 2 if dont want to accept")
                                    suggestionChoice = int(input("Enter the desired number :  "))
                                    if suggestionChoice == 1:
                                        correctWords += 1
                                        accepetedSuggestion +=1
                                        break
                                    elif suggestionChoice == 2:
                                        incorrectWords += 1
                                        break
                                    else:
                                        print("")
                                        print("Oops!  Try again...")
                                        print("Please enter 1 or 2 and nothing else !")
                                        print("")
                                except ValueError: # Try and except to validate the user input
                                        print("")
                                        print("Oops!  Try again...")
                                        print("Please enter 1 or 2 and nothing else !")
                                        print("")

                            break
                        else:
                            print("")
                            print("Oops!  Try again...")
                            print("Please enter 1, 2, 3, 4 and nothing else !")
                            print("")

                    except ValueError:# Try and except to validate the user input
                        print("")
                        print("Oops!  Try again...")
                        print("Please enter 1, 2, 3, 4 and nothing else !")
                        print("")
                        continue


        endtime = datetime.now() # Store the time and date when the spell check was completed
        print("-------------------------------------------------------") # Printing the statistics
        print("-------------------------------------------------------")
        print("|                    SPELL CHECKER !                   |")
        print("-------------------------------------------------------")
        print("               Spell Checking done :-)               ")
        print("-------------------------------------------------------")
        print("Total number of words spell checked -> "+str(totalWords))
        print("Total number of correct words -> "+str(correctWords))
        print("Total number of incorrect words -> "+str(incorrectWords))
        print("Total number of words added to dictionary -> "+str(addedToDic))
        print("Total number of accepted word suggestions -> "+str(accepetedSuggestion))
        print("-------------------------------------------------------")
        print("Spell checked at -> "+str (datetime.now()))
        print("Time elpased -> "+ str((endtime - starttime))) # Calculating the elapsed time by finding the time difference between the starttime and endtime variable
        print("-------------------------------------------------------")

        newfilename = input("Please enter the filename you want me to save the results :") # Ask the user the filename that they want the results to be saved

        resultFile = open(newfilename,"w+") # Creating the file and writing the data into it

        resultFile.write("SPELL CHECKER !\n")
        resultFile.write("---------------------\n")
        resultFile.write("Total number of words spell checked -> "+str(totalWords)+"\n")
        resultFile.write("Total number of correct words -> "+str(correctWords)+"\n")
        resultFile.write("Total number of incorrect words -> "+str(incorrectWords)+"\n")
        resultFile.write("Total number of words added to dictionary -> "+str(addedToDic)+"\n")
        resultFile.write("Total number of accepted word suggestions -> "+str(accepetedSuggestion)+"\n")
        resultFile.write("---------------------\n")
        resultFile.write("Spell checked at -> "+str (datetime.now())+"\n")
        resultFile.write("Time elapsed -> "+ str((endtime - starttime))+"\n")
        resultFile.write("---------------------\n")
        markedWords="";
        for markedWord in markedWordsList:
            markedWords = markedWords+" "+markedWord
        resultFile.write("The words that were marked -> "+str(markedWords+"\n"))
        resultFile.write("---------------------\n")
        resultFile.write("Your input -> "+sentence+"\n")

        print("-------------------------------------------------------")
        print("|                    SPELL CHECKER !                   |")
        print("-------------------------------------------------------")
        print("File created :-)")
        print("-------------------------------------------------------")
        print("Enter 1 if you want me to return to the initail menu :)") # Asking the user if they want to return back to the initial menu or to exit
        print("Enter 0 if you want me to quit :(                     ")

        while True:
            try: # Try and except to validate the input
                userEndChoice = int(input("Enter the desired number :  "))
                if userEndChoice == 1:
                    break
                elif userEndChoice == 0:
                    print("-------------------------------------------------------")
                    print("Hoping to see you soon :-)")
                    print("-------------------------------------------------------")
                    quit()
                else:
                    print("")
                    print("Oops!  Try again...")
                    print("Please enter 0 or 1 and nothing else !")
                    print("")
                    continue
            except ValueError:
                print("")
                print("Oops!  Try again...")
                print("Please enter 0 or 1 and nothing else !")
                print("")
                continue

while restart : #While loop to restart the program when needed
    getUserChoice()
