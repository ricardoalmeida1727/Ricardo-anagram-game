import json
import random
 
def word_prompt(data, length):
    all_words = list(data.keys())
    while True:
        word = random.choice(all_words)
        if len(word) < length and len(word) > 2:
            print(word)
            return word
 
def shuffle_word(word):
    array = list(word)
    shuffled = word
    while True:
        random.shuffle(array)
        shuffled = ''.join(array)
        if shuffled != word:
            return shuffled
        
def stats(scores,played,number_tent,corrects):
    max_score = number_tent * played
    score = sum(scores)
    print("Stats")
    print('-'*50)
    print("Score:",score)
    print("Played:", played)
    print("Corrects Answers "+ f"{corrects}" + "/" + f"{played}")
    print('-'*50)
    
        
if __name__ == "__main__":
    
    number_tent = 5
    played = 0
    correct = 0
    scores = []
    
    filename = 'dictionary.json'
    file = open(filename)
    data = json.load(file)
    
    print("Welcome to the Anagram Game!")
    while(True):
        played+=1
        word = word_prompt(data, 5)
        question = shuffle_word(word)
        meaning = data[word]
        
        question = question.lower()
        word = word.lower()
        
        print("\nSolve:", question)
        print("Hint:", meaning)
        
        for i in range(number_tent, 0, -1):
            print("\nAttempts Left:", i)
            guess = input('Make a guess: ').lower().strip()
            if len(guess)!=len(word):
                print("Erro")
            if guess == word:
                print("Correct!")
                scores.append(i)
                correct+=1
                break
            if i == 1:
                scores.append(0)
                print("\nCorrect Answer:", word)
        
        choice = input("\nContinue? [y/n]: ")
        print('-'*50)
        if choice == 'n':
            stats(scores,played,number_tent,correct)
            print("\nThank you for playing!")
            break