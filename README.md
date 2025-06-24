# 🔐 Task : Password Strength or Complexity Checker
---

## 📌 Task Objective

> Build a tool that assesses the strength of a password based on criteria such as:
> - Minimum length
> - Presence of **uppercase** and **lowercase** letters
> - Inclusion of **numbers** and **special characters**
>  
> The tool should provide real-time feedback on the password's complexity.

---

## 🧠 How It Works

This tool evaluates the strength of a password by checking for the following components:

1. 🔢 **Minimum Length** (at least 8 characters)  
2. 🔠 **Uppercase Letters**
3. 🔡 **Lowercase Letters**
4. 🔣 **Digits**
5. ❗ **Special Characters** (`!@#$%^&*()_+{}[]|:;'"<>,.?/`)

A score is calculated out of 5 based on how many of these conditions the password meets.

---

## 🧑‍💻 Features

- ✅ Real-time password strength evaluation
- ⚠️ Feedback with suggestions on how to improve weak passwords
- 📊 Categorizes password as:
  - Strong (5/5)
  - Medium (3–4/5)
  - Weak (below 3)
- 🧠 Educational logic using regular expressions
- 👨‍💻 Command-line interface

---

## 🛠️ Requirements

- Python 3.x 

---

## ▶️ How to Run

1. Clone the repository or download `password_checker.py`
2. Open terminal or command prompt
3. Run the script:

```bash
python password_checker.py

###Enter any password when prompted, e.g.:
```bash
Enter your password: ****@123
