import random
import string
import tkinter

def generate_password(length=12):
    # Definisci i caratteri che saranno utilizzati per generare la password
    characters = string.ascii_letters + string.digits + string.punctuation

    # Mescola i caratteri in modo casuale
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

if __name__ == "__main__":
    password_length = 12  # Puoi specificare la lunghezza desiderata della password
    generated_password = generate_password(password_length)
    print("Password generata:", generated_password)

root = tkinter.Tk()
root.title("Password generator by Luca Canali")

root.mainloop()