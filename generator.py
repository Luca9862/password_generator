import random
import string
import tkinter
import threading

def generate_password(length):
    # Definisci i caratteri che saranno utilizzati per generare la password
    characters = string.ascii_letters + string.digits + string.punctuation

    # Mescola i caratteri in modo casuale
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def start():
    selected_number = int(input.get())
    password = generate_password(selected_number)
    output.delete(1.0, tkinter.END)  # Cancella il testo precedente nell'elemento di testo
    output.insert(tkinter.END, password)  # Inserisci la password generata nell'elemento di testo

root = tkinter.Tk()
root.title("Password generator by Luca Canali")

input = tkinter.Entry()
input.grid(row='0', column='0')

output = tkinter.Text()
output.grid(row='1', column='0')

button = tkinter.Button(text="Generate", command=start)
button.grid(row='0', column='1')

root.mainloop()