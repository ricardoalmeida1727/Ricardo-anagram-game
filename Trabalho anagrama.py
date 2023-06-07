import json
import random
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk


def word_prompt(data, length):
    all_words = list(data.keys())
    while True:
        word = random.choice(all_words)
        if len(word) < length and len(word) > 2:
            return word

def shuffle_word(word):
    array = list(word)
    shuffled = word
    while True:
        random.shuffle(array)
        shuffled = ''.join(array)
        if shuffled != word:
            return shuffled

def calculate_score(attempts):
    max_score = number_tent * 5
    if attempts == 1:
        return 5
    elif attempts > 1:
        return 5 - (attempts - 1)
    else:
        return 0

def check_guess():
    guess = guess_entry.get().lower().strip()
    if len(guess) != len(word):
        messagebox.showerror("Invalid Guess", "Your guess should have the same length as the word.")
    elif guess == word:
        score = calculate_score(number_tent - remaining_attempts.get() + 1)
        messagebox.showinfo("Correct!", f"Congratulations, you guessed correctly!\nScore: {score}")
        scores.append(score)
        correct.set(correct.get() + 1)
        next_word()
    else:
        remaining_attempts.set(remaining_attempts.get() - 1)
        if remaining_attempts.get() == 0:
            messagebox.showinfo("Incorrect", "Sorry, you've run out of attempts. The correct word was: " + word)
            next_word()
        else:
            messagebox.showinfo("Incorrect", "Sorry, that's not the correct answer. Try again. Remaining attempts: " + str(remaining_attempts.get()))

def next_word():
    global word, meaning
    played.set(played.get() + 1)
    remaining_attempts.set(number_tent)
    word = word_prompt(data, 5)
    question = shuffle_word(word)
    meaning = data[word]
    print(len(meaning))
    if len(meaning) > 3000:
        meaning = meaning[:3000]
    question_label.config(text=question)
    hint_label.config(text=meaning,wraplength=500)
    guess_entry.delete(0, tk.END)

def stats():
    score = sum(scores)
    corrects = correct.get()
    stats_text = f"Stats\n{'-'*50}\nScore: {score}\nPlayed: {played.get()}\nCorrect Answers: {corrects}/{played.get()}\n{'-'*50}"
    messagebox.showinfo("Stats", stats_text)

if __name__ == "__main__":
    number_tent = 5
    scores = []

    filename = 'dictionary.json'
    with open(filename) as file:
        data = json.load(file)

    root = tk.Tk()
    root.geometry("1920x1080")
    root.title("Anagram Game")
  

    played = tk.IntVar()
    played.set(0)

    welcome_label = tk.Label(root, text="Welcome to the Anagram Game!",font = ('calibre',32,'bold'))
    welcome_label.pack(pady=15)
    
    #image = Image.open("nome_da_imagem.png")  # Substitua "nome_da_imagem.png" pelo nome do seu arquivo de imagem

    # Crie um objeto 'ImageTk' para exibir a imagem no widget 'tkinter'
    # image_tk = ImageTk.PhotoImage(image)

    # Crie um widget 'tkinter.Label' para exibir a imagem
    # image_label = tkinter.Label(root, image=image_tk)
    # image_label.pack()

    question_label = tk.Label(root, text="",font = ('calibre',16,'bold'))
    question_label.pack()

    hint_label = tk.Label(root, text="",font = ('calibre',8,'bold'))
    hint_label.pack()

    guess_entry = tk.Entry(root, width=30, font = ('calibre',10,'bold'))
    guess_entry.pack(pady=10)

    check_button = tk.Button(root, text="Check", command = check_guess)
    check_button.pack()

    continue_button = tk.Button(root, text="Next Word", command= next_word)
    continue_button.pack(pady=10)

    correct = tk.IntVar()
    correct.set(0)

    stats_button = tk.Button(root, text="Stats", command=stats)
    stats_button.pack()

    remaining_attempts = tk.IntVar()
    remaining_attempts.set(number_tent)

    root.mainloop()