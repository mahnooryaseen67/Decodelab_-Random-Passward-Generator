import tkinter as tk
from tkinter import messagebox
import secrets
import string
import math

NAVY = "#07163F"
PURPLE = "#7627F5"
PURPLE_DARK = "#6419DD"
BLUE = "#1677D2"
GREEN = "#20B476"
ORANGE = "#F29A32"

WHITE = "#FFFFFF"
BACKGROUND = "#F5F7FC"
TEXT = "#162650"
GRAY = "#7D879D"
BORDER = "#DCE2EC"

GREEN_BG = "#F1FCF7"
PURPLE_BG = "#F2EAFE"
RED_BG = "#FFF0F3"
BLUE_BG = "#EDF5FF"


root = tk.Tk()
root.title("Random Password Generator")
root.configure(bg=BACKGROUND)


screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()


try:
    root.state("zoomed")
except:
    root.geometry(
        f"{screen_width}x{screen_height - 70}+0+0"
    )


length_var = tk.IntVar(value=10)

uppercase_var = tk.BooleanVar(value=True)
lowercase_var = tk.BooleanVar(value=True)
numbers_var = tk.BooleanVar(value=True)
symbols_var = tk.BooleanVar(value=False)

password_var = tk.StringVar()
strength_var = tk.StringVar(value="—")

entropy_var = tk.StringVar(value="Entropy: — bits")
pool_var = tk.StringVar(value="Character Pool: —")

status_var = tk.StringVar(
    value="Generate a password to see the result."
)

strength_bars = []


def build_character_pool():

    uppercase = string.ascii_uppercase
    lowercase = string.ascii_lowercase
    numbers = string.digits

    # Special characters
    symbols = "!@#$%^&*"

    pool = ""

    if uppercase_var.get():
        pool += uppercase

    if lowercase_var.get():
        pool += lowercase

    if numbers_var.get():
        pool += numbers

    if symbols_var.get():
        pool += symbols

    return pool


def generate_secure_password(length):

    uppercase = string.ascii_uppercase
    lowercase = string.ascii_lowercase
    numbers = string.digits
    symbols = "!@#$%^&*"


    character_pool = build_character_pool()


    password_list = []


    if uppercase_var.get():
        password_list.append(
            secrets.choice(uppercase)
        )

    if lowercase_var.get():
        password_list.append(
            secrets.choice(lowercase)
        )

    if numbers_var.get():
        password_list.append(
            secrets.choice(numbers)
        )

    if symbols_var.get():
        password_list.append(
            secrets.choice(symbols)
        )


    while len(password_list) < length:

        password_list.append(
            secrets.choice(character_pool)
        )

    

    for i in range(len(password_list) - 1, 0, -1):

        j = secrets.randbelow(i + 1)

        password_list[i], password_list[j] = (
            password_list[j],
            password_list[i]
        )

    

    password = "".join(password_list)

    return password


def calculate_entropy(length, pool_size):

    if pool_size <= 0:
        return 0

    entropy = length * math.log2(pool_size)

    return entropy



def calculate_strength(password, entropy):

    score = 0

    # Length
    if len(password) >= 8:
        score += 1

    if len(password) >= 12:
        score += 1

    if len(password) >= 16:
        score += 1

    # Character diversity
    if any(c.isupper() for c in password):
        score += 1

    if any(c.islower() for c in password):
        score += 1

    if any(c.isdigit() for c in password):
        score += 1

    if any(c in "!@#$%^&*" for c in password):
        score += 1

    # Entropy
    if entropy >= 60:
        score += 1

    if entropy >= 80:
        score += 1

    # Strength label
    if score <= 3:
        return "Weak", 2

    elif score <= 5:
        return "Good", 4

    elif score <= 7:
        return "Strong", 6

    else:
        return "Very Strong", 7



def update_strength_bars(score):

    for index, bar in enumerate(strength_bars):

        if index < score:

            if score <= 2:
                bar.config(bg=ORANGE)

            elif score <= 4:
                bar.config(bg=BLUE)

            else:
                bar.config(bg=GREEN)

        else:
            bar.config(bg="#DDE3ED")



def generate_password():

    try:
        length = int(length_var.get())

    except ValueError:

        messagebox.showwarning(
            "Invalid Length",
            "Please enter a valid password length."
        )

        return


    if length < 4:

        messagebox.showwarning(
            "Invalid Length",
            "Password length must be at least 4 characters."
        )

        return

    if length > 128:

        messagebox.showwarning(
            "Invalid Length",
            "Password length cannot exceed 128 characters."
        )

        return


    if not (
        uppercase_var.get()
        or lowercase_var.get()
    ):

        messagebox.showwarning(
            "Character Selection",
            "Please select at least one letter type."
        )

        return

    

    if not numbers_var.get():

        messagebox.showwarning(
            "Number Required",
            "Numbers must be selected for this password generator."
        )

        numbers_var.set(True)

        return


    required_count = 0

    if uppercase_var.get():
        required_count += 1

    if lowercase_var.get():
        required_count += 1

    if numbers_var.get():
        required_count += 1

    if symbols_var.get():
        required_count += 1

    if length < required_count:

        messagebox.showwarning(
            "Length Too Short",
            "Password length is too short for the selected "
            "character categories."
        )

        return

   

    character_pool = build_character_pool()

    if not character_pool:

        messagebox.showwarning(
            "No Characters",
            "Please select at least one character type."
        )

        return


    password = generate_secure_password(length)

    password_var.set(password)


    pool_size = len(character_pool)

    pool_var.set(
        f"Character Pool: {pool_size}"
    )

   

    entropy = calculate_entropy(
        length,
        pool_size
    )

    entropy_var.set(
        f"Entropy: {entropy:.1f} bits"
    )

   

    strength, score = calculate_strength(
        password,
        entropy
    )

    strength_var.set(strength)

    update_strength_bars(score)

    status_var.set(
        "Strong password generated successfully!"
    )



def copy_password():

    password = password_var.get()

    if not password:

        messagebox.showinfo(
            "No Password",
            "Please generate a password first."
        )

        return

    root.clipboard_clear()
    root.clipboard_append(password)
    root.update()

    status_var.set(
        "Password copied to clipboard!"
    )



def clear_all():

    password_var.set("")

    strength_var.set("—")

    entropy_var.set(
        "Entropy: — bits"
    )

    pool_var.set(
        "Character Pool: —"
    )

    status_var.set(
        "Generate a password to see the result."
    )

    for bar in strength_bars:
        bar.config(bg="#DDE3ED")



HEADER_HEIGHT = 150

header = tk.Canvas(
    root,
    height=HEADER_HEIGHT,
    bg=NAVY,
    highlightthickness=0
)

header.pack(
    fill="x"
)


# Decorative circles
cx = screen_width - 340

header.create_oval(
    cx,
    -170,
    cx + 340,
    170,
    outline="#8437FF",
    width=2
)

header.create_oval(
    cx + 55,
    -115,
    cx + 285,
    115,
    outline="#A35CFF",
    width=2
)

header.create_oval(
    cx + 110,
    -60,
    cx + 230,
    60,
    outline="#C084FF",
    width=2
)


# Lock
header.create_text(
    85,
    73,
    text="🔐",
    font=("Segoe UI Emoji", 45),
    fill=WHITE
)


# Main title
header.create_text(
    185,
    55,
    text="Random",
    anchor="w",
    fill=WHITE,
    font=("Segoe UI", 28, "bold")
)

header.create_text(
    185,
    92,
    text="Password Generator",
    anchor="w",
    fill="#B75CFF",
    font=("Segoe UI", 28, "bold")
)

header.create_text(
    187,
    122,
    text="Generate strong, secure and random passwords instantly",
    anchor="w",
    fill="#E4E7F4",
    font=("Segoe UI", 10)
)



main = tk.Frame(
    root,
    bg=BACKGROUND
)

main.pack(
    fill="both",
    expand=True,
    padx=10,
    pady=7
)


settings = tk.Frame(
    main,
    bg=WHITE,
    highlightbackground=BORDER,
    highlightthickness=1
)

settings.pack(
    fill="x",
    pady=(0, 7)
)


settings_header = tk.Frame(
    settings,
    bg=WHITE
)

settings_header.pack(
    fill="x",
    padx=18,
    pady=(7, 2)
)


tk.Label(
    settings_header,
    text="⚙",
    bg=PURPLE,
    fg=WHITE,
    font=("Segoe UI Symbol", 16, "bold"),
    width=3,
    pady=3
).pack(
    side="left",
    padx=(0, 12)
)


settings_text = tk.Frame(
    settings_header,
    bg=WHITE
)

settings_text.pack(
    side="left"
)


tk.Label(
    settings_text,
    text="Password Settings",
    bg=WHITE,
    fg=TEXT,
    font=("Segoe UI", 16, "bold")
).pack(
    anchor="w"
)

tk.Label(
    settings_text,
    text="Choose the length and options for your password",
    bg=WHITE,
    fg=GRAY,
    font=("Segoe UI", 8)
).pack(
    anchor="w"
)


length_row = tk.Frame(
    settings,
    bg=WHITE
)

length_row.pack(
    fill="x",
    padx=18,
    pady=(2, 8)
)


tk.Label(
    length_row,
    text="⌁",
    bg=PURPLE,
    fg=WHITE,
    font=("Segoe UI Symbol", 16, "bold"),
    width=3,
    pady=3
).pack(
    side="left",
    padx=(0, 12)
)


length_text = tk.Frame(
    length_row,
    bg=WHITE
)

length_text.pack(
    side="left",
    fill="x",
    expand=True
)


tk.Label(
    length_text,
    text="Password Length",
    bg=WHITE,
    fg=TEXT,
    font=("Segoe UI", 12, "bold")
).pack(
    anchor="w"
)

tk.Label(
    length_text,
    text="Enter the desired length of your password",
    bg=WHITE,
    fg=GRAY,
    font=("Segoe UI", 8)
).pack(
    anchor="w"
)


tk.Spinbox(
    length_row,
    from_=4,
    to=128,
    textvariable=length_var,
    width=5,
    justify="center",
    font=("Segoe UI", 15, "bold"),
    fg=TEXT,
    bg=WHITE,
    relief="solid",
    bd=1
).pack(
    side="right",
    ipady=3
)


characters = tk.Frame(
    main,
    bg=WHITE,
    highlightbackground=BORDER,
    highlightthickness=1
)

characters.pack(
    fill="x",
    pady=7
)


character_header = tk.Frame(
    characters,
    bg=WHITE
)

character_header.pack(
    fill="x",
    padx=18,
    pady=(7, 2)
)


tk.Label(
    character_header,
    text="✓",
    bg=BLUE,
    fg=WHITE,
    font=("Segoe UI", 16, "bold"),
    width=3,
    pady=3
).pack(
    side="left",
    padx=(0, 12)
)


character_title = tk.Frame(
    character_header,
    bg=WHITE
)

character_title.pack(
    side="left"
)


tk.Label(
    character_title,
    text="Include Characters",
    bg=WHITE,
    fg=TEXT,
    font=("Segoe UI", 16, "bold")
).pack(
    anchor="w"
)

tk.Label(
    character_title,
    text="Select which characters to include in your password",
    bg=WHITE,
    fg=GRAY,
    font=("Segoe UI", 8)
).pack(
    anchor="w"
)


options = tk.Frame(
    characters,
    bg=WHITE
)

options.pack(
    fill="x",
    padx=18,
    pady=(4, 9)
)

for col in range(4):
    options.columnconfigure(
        col,
        weight=1
    )


def create_character_card(
    column,
    variable,
    title,
    subtitle,
    color
):

    card = tk.Frame(
        options,
        bg=WHITE,
        highlightbackground=BORDER,
        highlightthickness=1
    )

    card.grid(
        row=0,
        column=column,
        padx=4,
        sticky="nsew"
    )

    tk.Checkbutton(
        card,
        text="✓",
        variable=variable,
        bg=WHITE,
        activebackground=WHITE,
        fg=color,
        activeforeground=color,
        selectcolor=WHITE,
        font=("Segoe UI", 14, "bold"),
        relief="flat",
        bd=0,
        cursor="hand2"
    ).pack(
        side="left",
        padx=(5, 1),
        pady=6
    )

    text_frame = tk.Frame(
        card,
        bg=WHITE
    )

    text_frame.pack(
        side="left",
        pady=5
    )

    tk.Label(
        text_frame,
        text=title,
        bg=WHITE,
        fg=color,
        font=("Segoe UI", 14, "bold")
    ).pack(
        anchor="w"
    )

    tk.Label(
        text_frame,
        text=subtitle,
        bg=WHITE,
        fg=TEXT,
        font=("Segoe UI", 7)
    ).pack(
        anchor="w"
    )


create_character_card(
    0,
    uppercase_var,
    "ABC",
    "Uppercase (A-Z)",
    PURPLE
)

create_character_card(
    1,
    lowercase_var,
    "abc",
    "Lowercase (a-z)",
    BLUE
)

create_character_card(
    2,
    numbers_var,
    "123",
    "Numbers (0-9)",
    GREEN
)

create_character_card(
    3,
    symbols_var,
    "!@#",
    "Optional Symbols",
    ORANGE
)


tk.Button(
    main,
    text="✨   Generate Password",
    command=generate_password,
    bg=PURPLE,
    fg=WHITE,
    activebackground=PURPLE_DARK,
    activeforeground=WHITE,
    font=("Segoe UI", 13, "bold"),
    relief="flat",
    bd=0,
    cursor="hand2",
    pady=8
).pack(
    fill="x",
    pady=3
)

result = tk.Frame(
    main,
    bg=GREEN_BG,
    highlightbackground="#C9E9D8",
    highlightthickness=1
)

result.pack(
    fill="x",
    pady=6
)


# Result heading
result_header = tk.Frame(
    result,
    bg=GREEN_BG
)

result_header.pack(
    fill="x",
    padx=18,
    pady=(7, 2)
)


tk.Label(
    result_header,
    text="✓",
    bg=GREEN,
    fg=WHITE,
    font=("Segoe UI", 16, "bold"),
    width=3,
    pady=3
).pack(
    side="left",
    padx=(0, 12)
)


result_text = tk.Frame(
    result_header,
    bg=GREEN_BG
)

result_text.pack(
    side="left"
)


tk.Label(
    result_text,
    text="Your Generated Password",
    bg=GREEN_BG,
    fg="#15945A",
    font=("Segoe UI", 16, "bold")
).pack(
    anchor="w"
)

tk.Label(
    result_text,
    textvariable=status_var,
    bg=GREEN_BG,
    fg=GRAY,
    font=("Segoe UI", 8)
).pack(
    anchor="w"
)


tk.Label(
    result_header,
    textvariable=strength_var,
    bg="#E5F8EE",
    fg=GREEN,
    font=("Segoe UI", 8, "bold"),
    padx=10,
    pady=4
).pack(
    side="right"
)


password_box = tk.Frame(
    result,
    bg=WHITE,
    highlightbackground="#BFE2D0",
    highlightthickness=1
)

password_box.pack(
    fill="x",
    padx=18,
    pady=3
)

password_box.columnconfigure(
    0,
    weight=1
)


tk.Entry(
    password_box,
    textvariable=password_var,
    state="readonly",
    justify="center",
    font=("Consolas", 17, "bold"),
    fg=PURPLE,
    bg="#F3F3F3",
    relief="flat",
    bd=0
).grid(
    row=0,
    column=0,
    padx=5,
    pady=6,
    sticky="ew"
)


tk.Button(
    password_box,
    text="▣ Copy",
    command=copy_password,
    bg="#E7F8EF",
    fg=GREEN,
    activebackground="#D3F1E1",
    activeforeground=GREEN,
    font=("Segoe UI", 8, "bold"),
    relief="flat",
    bd=0,
    padx=9,
    pady=4,
    cursor="hand2"
).grid(
    row=0,
    column=1,
    padx=2
)


tk.Button(
    password_box,
    text="↻",
    command=generate_password,
    bg=BLUE_BG,
    fg=BLUE,
    activebackground="#DCEBFF",
    activeforeground=BLUE,
    font=("Segoe UI", 13, "bold"),
    relief="flat",
    bd=0,
    padx=8,
    pady=2,
    cursor="hand2"
).grid(
    row=0,
    column=2,
    padx=(0, 5)
)



info_row = tk.Frame(
    result,
    bg=GREEN_BG
)

info_row.pack(
    fill="x",
    padx=18,
    pady=(2, 1)
)


tk.Label(
    info_row,
    textvariable=entropy_var,
    bg=GREEN_BG,
    fg=TEXT,
    font=("Segoe UI", 8, "bold")
).pack(
    side="left"
)


tk.Label(
    info_row,
    textvariable=pool_var,
    bg=GREEN_BG,
    fg=GRAY,
    font=("Segoe UI", 8)
).pack(
    side="right"
)


strength_line = tk.Frame(
    result,
    bg=GREEN_BG
)

strength_line.pack(
    fill="x",
    padx=18,
    pady=(1, 1)
)


tk.Label(
    strength_line,
    text="Password Strength",
    bg=GREEN_BG,
    fg=TEXT,
    font=("Segoe UI", 8, "bold")
).pack(
    side="left"
)


tk.Label(
    strength_line,
    textvariable=strength_var,
    bg=GREEN_BG,
    fg=GREEN,
    font=("Segoe UI", 8, "bold")
).pack(
    side="right"
)


# Strength bars
meter = tk.Frame(
    result,
    bg=GREEN_BG
)

meter.pack(
    fill="x",
    padx=18,
    pady=(0, 8)
)


for i in range(7):

    bar = tk.Frame(
        meter,
        bg="#DDE3ED",
        height=5
    )

    bar.pack(
        side="left",
        fill="x",
        expand=True,
        padx=2
    )

    strength_bars.append(bar)


actions = tk.Frame(
    main,
    bg=BACKGROUND
)

actions.pack(
    fill="x",
    pady=(0, 1)
)

actions.columnconfigure(0, weight=1)
actions.columnconfigure(1, weight=1)


tk.Button(
    actions,
    text="↻   Generate Another",
    command=generate_password,
    bg=PURPLE_BG,
    fg="#6824D9",
    activebackground="#E0D1FF",
    activeforeground="#6824D9",
    font=("Segoe UI", 9, "bold"),
    relief="flat",
    bd=0,
    cursor="hand2",
    pady=6
).grid(
    row=0,
    column=0,
    padx=(0, 4),
    sticky="ew"
)


tk.Button(
    actions,
    text="▢   Clear All",
    command=clear_all,
    bg=RED_BG,
    fg="#E0445D",
    activebackground="#FFDCE2",
    activeforeground="#E0445D",
    font=("Segoe UI", 9, "bold"),
    relief="flat",
    bd=0,
    cursor="hand2",
    pady=6
).grid(
    row=0,
    column=1,
    padx=(4, 0),
    sticky="ew"
)



tk.Label(
    main,
    text="🔒  Stay safe. Use strong passwords!",
    bg=BACKGROUND,
    fg=PURPLE,
    font=("Segoe UI", 8)
).pack(
    pady=(1, 0)
)


root.mainloop()