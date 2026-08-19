# Decodelab_Random-Passward-Generator
# 🔐 Random Password Generator

A secure and user-friendly **Random Password Generator** built with **Python and Tkinter**. The application generates strong passwords using Python's cryptographically secure `secrets` module and provides password strength, entropy, and character pool information.

The project features a clean graphical user interface that allows users to customize password length and character types, generate secure passwords, copy them to the clipboard, and clear the generated results.

## 📌 Project Overview

The **Random Password Generator** is designed to help users create strong and unpredictable passwords quickly.

Users can:

* Select password length from **4 to 128 characters**
* Include uppercase letters
* Include lowercase letters
* Include numbers
* Optionally include special symbols
* Generate cryptographically secure passwords
* View password strength
* View estimated entropy
* View character pool size
* Copy passwords to the clipboard
* Generate another password
* Clear all generated information

## ✨ Features

### 🔑 Secure Password Generation

The project uses Python's built-in `secrets` module instead of the standard `random` module.

```python
secrets.choice()
secrets.randbelow()
```

The `secrets` module is designed for generating values suitable for security-sensitive applications.

### 📏 Custom Password Length

Users can select a password length between:

**4 and 128 characters**

The application validates the entered length and displays a warning when an invalid value is provided.

### 🔠 Character Selection

Users can customize the password by selecting:

| Character Type | Characters      |
| -------------- | --------------- |
| Uppercase      | A-Z             |
| Lowercase      | a-z             |
| Numbers        | 0-9             |
| Symbols        | ! @ # $ % ^ & * |

### 📊 Password Strength

The application calculates password strength based on:

* Password length
* Uppercase characters
* Lowercase characters
* Numbers
* Special symbols
* Estimated entropy

The strength levels are:

* **Weak**
* **Good**
* **Strong**
* **Very Strong**

A visual seven-bar strength meter is also displayed.

### 🧮 Entropy Calculation

The application estimates password entropy using:

```text
Entropy = Length × log₂(Character Pool Size)
```

This provides an approximate measurement of how difficult a password would be to guess through brute-force attempts.

### 📋 Character Pool Information

The application displays the number of possible characters available for password generation.

For example:

```text
Character Pool: 62
```

### 📋 Copy to Clipboard

Users can copy the generated password directly to the clipboard using the **Copy** button.

### 🧹 Clear All

The **Clear All** button removes:

* Generated password
* Strength result
* Entropy information
* Character pool information
* Status message

### ⚠️ Input Validation

The application checks for:

* Invalid password length
* Password length below 4
* Password length above 128
* No selected character types
* Password length shorter than the number of required character categories
* Numbers being selected as required by the project design

## 🛠️ Technologies Used

* **Python 3**
* **Tkinter** – Graphical User Interface
* **secrets** – Secure random password generation
* **string** – Character sets
* **math** – Entropy calculation

## 📦 Python Modules

The project uses the following built-in Python modules:

```python
import tkinter as tk
from tkinter import messagebox
import secrets
import string
import math
```

No external Python packages are required.

## 🖥️ User Interface

The application contains the following major sections:

### 1. Header

Displays the project title:

**Random Password Generator**

along with a short description.

### 2. Password Settings

Allows the user to select the desired password length.

### 3. Include Characters

Provides four character options:

* ABC — Uppercase
* abc — Lowercase
* 123 — Numbers
* !@# — Symbols

### 4. Generate Password

Generates a secure password according to the selected settings.

### 5. Generated Password

Displays:

* Generated password
* Password strength
* Entropy
* Character pool size
* Strength meter

### 6. Actions

Provides:

* Generate Another
* Clear All

## 🔒 Security

Security is an important part of this project.

Instead of using:

```python
random
```

the application uses:

```python
secrets
```

The `secrets` module is more appropriate for generating passwords because it is designed for security-sensitive random values.

The password characters are also shuffled using:

```python
secrets.randbelow()
```

This prevents relying on predictable pseudo-random behavior.

## 🚀 Installation

### Step 1: Install Python

Download and install Python 3 from the official Python website.

### Step 2: Clone the Repository

```bash
git clone https://github.com/your-username/random-password-generator.git
```

### Step 3: Open the Project Folder

```bash
cd random-password-generator
```

### Step 4: Run the Program

```bash
python password_generator.py
```

The graphical password generator will open automatically.

## ▶️ How to Use

1. Launch the application.
2. Select the desired password length.
3. Select the character types you want to include.
4. Click **Generate Password**.
5. View the generated password.
6. Check the password strength and entropy.
7. Click **Copy** to copy the password.
8. Click **Generate Another** to create a new password.
9. Click **Clear All** to reset the result.

## 📂 Project Structure

```text
random-password-generator/
│
├──  Random-Password-Generator.py
├── README.md
└── screenshot.png
```

## 🧠 Main Functions

### `build_character_pool()`

Creates the available character pool based on the user's selected options.

### `generate_secure_password(length)`

Generates the password using `secrets.choice()` and securely shuffles the generated characters using `secrets.randbelow()`.

### `calculate_entropy(length, pool_size)`

Calculates the estimated password entropy.

### `calculate_strength(password, entropy)`

Evaluates the password and returns a strength level and score.

### `update_strength_bars(score)`

Updates the visual password-strength meter.

### `generate_password()`

Controls the main password-generation process and performs input validation.

### `copy_password()`

Copies the generated password to the clipboard.

### `clear_all()`

Resets the application results.

## ✅ Validation Rules

The application follows these validation rules:

```text
Minimum password length: 4
Maximum password length: 128

At least one letter type:
    Uppercase OR Lowercase

Numbers:
    Required

Selected character categories:
    Must fit within the requested password length
```

## 📈 Strength Levels

| Score | Strength    |
| ----: | ----------- |
|   0–3 | Weak        |
|   4–5 | Good        |
|   6–7 | Strong      |
|    8+ | Very Strong |

The application also considers entropy when calculating the overall strength.

## 🎯 Learning Objectives

This project demonstrates practical use of:

* Python functions
* Conditional statements
* Loops
* Exception handling
* Tkinter GUI development
* `StringVar` and `BooleanVar`
* Secure random generation
* Character-set manipulation
* Mathematical calculations
* Password entropy
* Input validation
* Clipboard functionality
* GUI event handling

## 🔮 Future Improvements

Possible future improvements include:

* Password history
* Password visibility toggle
* More special-character options
* Password strength recommendations
* Dark mode
* Export password functionality
* Automatic password expiration reminders
* More advanced entropy analysis
* Customizable security rules

## 👩‍💻 Author
Mahnoor Shaikh Yaseen

BS Software Engineering

## 📄 License

This project is created for educational and learning purposes.

You may modify and improve the project for your own educational use.

## ⭐ Acknowledgment

This project was developed as a Python GUI project to demonstrate secure password generation, user input validation, and graphical user interface development using Tkinter.


### 🔐 Stay Safe — Use Strong Passwords!
