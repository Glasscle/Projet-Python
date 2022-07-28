"""
Graphic interface for an app
"""

#### Modifier la taille de l'image password.png

### Section Impot.
from tkinter import *
import string
from random import randint, choice
from functools import partial

class Myapp:
    """ Main class of the app. All the program is created inside it. """

    def __init__(self):
        self.window = Tk()
        self.window.title("Générateur de mot de passe")
        self.window.geometry("720x480")
        self.window.minsize(480, 360)
        self.window.iconbitmap('green-cross.ico')
        self.window.config(background='#4065A4')
        # Components initialisation
        self.frame = Frame(self.window, bg='#4065A4')
        self.right_frame = Frame(self.frame, bg='#4065A4')
        self.right_frame.grid(row=0, column=1)
        # Components creation
        self.create_visual_elements()
        # Pack the frame
        self.frame.pack(expand=YES)

    def create_visual_elements(self):
        # Regrouping 3 fonctions
        self.create_bloc_picture_left()
        self.create_bloc_generate_right()
        self.create_buttons()
        self.create_menu()

    def generate_password(self, nbr_password_caract):
        """ Generate a password whom leng depends on the argument 'nbr_password_caract'. """
        all_chars = string.ascii_letters + string.punctuation + string.digits
        password = "".join(choice(all_chars) for x in range(int(nbr_password_caract)))
        self.password_entry.delete(0, END)
        self.password_entry.insert(0, password)

    def create_bloc_picture_left(self):
        """ Create the main bloc on the left with the picture of the app. """
        width_main_picture = 300
        height_main_picture = 300
        self.picture = PhotoImage(file="password.png")
        self.canvas = Canvas(self.frame, width=width_main_picture, height=height_main_picture, bg='#4065A4', bd=0, highlightthickness=0)
        self.canvas.create_image(width_main_picture/2, height_main_picture/2, image=self.picture)
        self.canvas.grid(row=0, column=0)

    def create_bloc_generate_right(self):
        """ Create the bloc which contains the label, input and 2 buttons. """
        self.label_title = Label(self.right_frame, text="Mot de passe", font=("Helvetica", 20), bg='#4065A4', fg='white')
        self.label_title.pack()
        # Create input
        self.password_entry = Entry(self.right_frame, text="Mot de passe", font=("Helvetica", 20), bg='#4065A4', fg='white')
        self.password_entry.pack()

    def create_buttons(self):
        """ Create the 2 buttons to generate a 6 or a 12 character password. """
        generate_password_button_6c = Button(self.right_frame, text="Mdp 6 caractères", font=("Helvetica", 15), bg='#4065A4', fg='white', command=partial(self.generate_password, 6))
        generate_password_button_12c = Button(self.right_frame, text="Mdp 12 caractères", font=("Helvetica", 15), bg='#4065A4', fg='white', command=partial(self.generate_password, 12))
        # Display buttons
        generate_password_button_6c.pack(side=LEFT, expand=YES, fill=X)
        generate_password_button_12c.pack(side=RIGHT, expand=YES, fill=X)

    def create_menu(self):
        """ Create the menu bar on the top. """
        # Creation d'une barre de menu.
        menu_bar = Menu(self.window)
        # Creer un menu 'Fichier'.
        file_menu = Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="Quitter", command=self.window.quit)
        menu_bar.add_cascade(label="Fichier", menu=file_menu)
        # Creer un menu 'Générer'.
        generate_menu = Menu(menu_bar, tearoff=0)
        generate_menu.add_command(label="Psw 6 caractères", command=partial(self.generate_password, 6))
        generate_menu.add_command(label="Psw 12 caractères", command=partial(self.generate_password, 12))
        menu_bar.add_cascade(label="Génerer", menu=generate_menu)
        # Configurer notre fenetre pour ajouter la menu_bar.
        self.window.config(menu=menu_bar)




######## Main Section

app = Myapp()
app.window.mainloop()
