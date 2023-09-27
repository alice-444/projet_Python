import tkinter as tk
from tkinter import messagebox, Scrollbar, Text
from PyDictionary import PyDictionary
import pyttsx3

def get_word_details():
    word = entry.get().strip()
    if not word:
        result_text.config(state=tk.NORMAL)
        result_text.delete("1.0", tk.END)
        result_text.insert(tk.END, "Choose a word")
        result_text.config(state=tk.DISABLED)
        return

    try:
        meaning = dictionary.meaning(word)
        synonyms = dictionary.synonym(word)
        antonyms = dictionary.antonym(word)

        result_text.config(state=tk.NORMAL)
        result_text.delete("1.0", tk.END)

        result_text.insert(tk.END, f"{'='*15} Results for '{word}' {'='*15}\n\n")

        if meaning:
            result_text.insert(tk.END, f"{'-'*10} Signification {'-'*10}\n")
            formatted_meaning = "\n".join([f"    {word_type}: {', '.join(definitions)}" for word_type, definitions in meaning.items()])
            result_text.insert(tk.END, f"{formatted_meaning}\n\n")

        if synonyms:
            result_text.insert(tk.END, f"{'-'*10} Synonyms {'-'*10}\n")
            result_text.insert(tk.END, f"{', '.join(synonyms)}\n\n")

        if antonyms:
            result_text.insert(tk.END, f"{'-'*10} Antonyms {'-'*10}\n")
            result_text.insert(tk.END, f"{', '.join(antonyms)}\n")

        if not (meaning or synonyms or antonyms):
            result_text.insert(tk.END, "No information found")

        # Prononciation
        engine = pyttsx3.init()
        engine.say(word)
        engine.runAndWait()

        result_text.config(state=tk.DISABLED)

    except Exception as e:
        result_text.config(state=tk.NORMAL)
        result_text.delete("1.0", tk.END)
        result_text.insert(tk.END, f"An error has occurred. Please check your Internet connection and try again.")
        result_text.config(state=tk.DISABLED)
        messagebox.showerror("Error", f"An error has occurred:\n{str(e)}")

fenetre = tk.Tk()
fenetre.title("Dictionary")
fenetre.geometry("500x400")
fenetre.configure(bg='#f0f0f0')

label = tk.Label(fenetre, text="Choose a word :", bg='#f0f0f0', font=("Arial", 12))
label.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="w")

entry = tk.Entry(fenetre, font=("Arial", 12))
entry.grid(row=1, column=0, padx=10, pady=(0, 10), sticky="we")

button = tk.Button(fenetre, text="Get details", command=get_word_details, font=("Arial", 12))
button.grid(row=2, column=0, padx=10, pady=10, sticky="we")

result_text = Text(fenetre, wrap="word", height=10, width=60, font=("Arial", 12))
result_text.grid(row=3, column=0, padx=10, pady=(0, 10), sticky="news")

scrollbar = Scrollbar(fenetre, command=result_text.yview)
scrollbar.grid(row=3, column=1, pady=(0, 10), sticky="ns")
result_text.config(yscrollcommand=scrollbar.set)

dictionary = PyDictionary()

fenetre.mainloop()
