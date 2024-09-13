from random import shuffle, choice
from customtkinter import CTkImage, CTkFrame, CTkLabel, CTkFont, CTkButton, CTkOptionMenu, CTk
from PIL import Image
from os import path

lowercase_letters = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "n",
    "m",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
]
uppercase_letters = [
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "N",
    "M",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
]
numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]


class App(CTk):
    def __init__(self):
        super().__init__()
        self.password_char_list = []
        self.number_lowercase_letters = 0
        self.number_uppercase_letters = 0
        self.number_symbols = 0
        self.number_numbers = 0
        self.width = 900
        self.height = 600

        # configure window
        self.title("PyPassword App")
        self.geometry(f"{self.width}x{self.height}")
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.resizable(False, False)

        # load and create background image, logo
        current_path = path.dirname(path.realpath(__file__))
        self.logo_image = CTkImage(
            Image.open(path.join(current_path + "\\images\\pixelcut-export.jpg")),
            size=(400, 100),
        )
        self.bg_image = CTkImage(
            Image.open(path.join(current_path + "\\images\\bg_gradient.jpg")),
            size=(self.width, self.height),
        )
        self.bg_image_label = CTkLabel(self, image=self.bg_image)
        self.bg_image_label.grid(row=0, column=1)

        # create sidebar frame with widgets
        self.sidebar_frame = CTkFrame(self)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsw")
        self.sidebar_frame.grid_rowconfigure(9, weight=1)
        self.sidebar_logo = CTkLabel(
            self.sidebar_frame,
            text="",
            image=self.logo_image,
        )
        self.sidebar_logo.grid(row=0, column=0, padx=20, pady=10)
        self.logo_label_lowercase = CTkLabel(
            self.sidebar_frame,
            text="How many lower case letters would you like in your password?",
            font=CTkFont(size=15, weight="normal"),
        )
        self.logo_label_lowercase.grid(row=1, column=0, padx=20, pady=(20, 10))
        self.lowercase_optionemenu = CTkOptionMenu(
            self.sidebar_frame,
            values=["1", "2", "3", "4", "5", "6", "7", "8", "9"],
            command=self.save_lowercase,
        )
        self.lowercase_optionemenu.grid(row=2, column=0, padx=20, pady=(10, 10))
        self.logo_label_uppercase = CTkLabel(
            self.sidebar_frame,
            text="How many upper case letters would you like in your password?",
            font=CTkFont(size=15, weight="normal"),
        )
        self.logo_label_uppercase.grid(row=3, column=0, padx=20, pady=(20, 10))
        self.uppercase_optionemenu = CTkOptionMenu(
            self.sidebar_frame,
            values=["1", "2", "3", "4", "5", "6", "7", "8", "9"],
            command=self.save_uppercase,
        )
        self.uppercase_optionemenu.grid(row=4, column=0, padx=20, pady=(10, 10))
        self.logo_label_symbols = CTkLabel(
            self.sidebar_frame,
            text="How many symbols would you like in your password?",
            font=CTkFont(size=15, weight="normal"),
        )
        self.logo_label_symbols.grid(row=5, column=0, padx=20, pady=(20, 10))
        self.symbols_optionemenu = CTkOptionMenu(
            self.sidebar_frame,
            values=["1", "2", "3", "4", "5", "6", "7", "8", "9"],
            command=self.save_symbols,
        )
        self.symbols_optionemenu.grid(row=6, column=0, padx=20, pady=(10, 10))
        self.logo_label_numbers = CTkLabel(
            self.sidebar_frame,
            text="How many numbers would you like in your password?",
            font=CTkFont(size=15, weight="normal"),
        )
        self.logo_label_numbers.grid(row=7, column=0, padx=20, pady=(20, 10))
        self.numbers_optionemenu = CTkOptionMenu(
            self.sidebar_frame,
            values=["1", "2", "3", "4", "5", "6", "7", "8", "9"],
            command=self.save_numbers,
        )
        self.numbers_optionemenu.grid(row=8, column=0, padx=20, pady=(10, 10))

        # create mid-frame for button and result
        self.mid_frame = CTkFrame(self)
        self.mid_frame.grid(row=0, column=1, pady=75, sticky="ewns")
        self.mid_frame.grid_rowconfigure(2, weight=1)
        self.mid_frame.grid_columnconfigure(0, weight=1)

        # button on mid-frame
        self.generate_button = CTkButton(
            self.mid_frame,
            text="Generate Password",
            command=self.generate_password,
            width=200,
            height=50,
        )
        self.generate_button.grid(row=0, column=0, pady=50)

        # label for password
        self.password_label = CTkLabel(
            self.mid_frame,
            text="",
            fg_color="#FFEFD5",
            text_color="black",
            font=("Helvetica", 20),
            height=200,
        )
        self.password_label.grid(row=1, column=0, sticky="ew")

    def save_lowercase(self, number):
        self.number_lowercase_letters = int(number)

    def save_uppercase(self, number):
        self.number_uppercase_letters = int(number)

    def save_symbols(self, number):
        self.number_symbols = int(number)

    def save_numbers(self, number):
        self.number_numbers = int(number)

    def generate_password(self):
        self.password_char_list = []
        for _ in range(0, self.number_lowercase_letters):
            self.password_char_list.append(choice(lowercase_letters))
        for _ in range(0, self.number_uppercase_letters):
            self.password_char_list.append(choice(uppercase_letters))
        for _ in range(0, self.number_numbers):
            self.password_char_list.append(choice(numbers))
        for _ in range(0, self.number_symbols):
            self.password_char_list.append(choice(symbols))
        shuffle(self.password_char_list)
        self.update_label()

    def update_label(self):
        self.password_label.configure(
            text=f"Your password is:\n\n {''.join(self.password_char_list)}"
        )


if __name__ == "__main__":
    app = App()
    app.mainloop()
