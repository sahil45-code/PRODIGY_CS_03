import re

def check_password_strength(password):
    strength = 0
    remarks = []

    # Length check
    if len(password) >= 8:
        strength += 1
    else:
        remarks.append("❌ Password is too short (min 8 characters).")

    # Uppercase check
    if re.search(r"[A-Z]", password):
        strength += 1
    else:
        remarks.append("❌ Add uppercase letters.")

    # Lowercase check
    if re.search(r"[a-z]", password):
        strength += 1
    else:
        remarks.append("❌ Add lowercase letters.")

    # Digit check
    if re.search(r"[0-9]", password):
        strength += 1
    else:
        remarks.append("❌ Add numbers.")

    # Special character check
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        strength += 1
    else:
        remarks.append("❌ Add special characters (!@#$%^&* etc).")

    # Overall feedback
    if strength == 5:
        return "✅ Strong Password!", remarks
    elif 3 <= strength < 5:
        return "⚠️ Medium Strength Password.", remarks
    else:
        return "❌ Weak Password!", remarks

# Main program
if __name__ == "__main__":
    print("🔐 Password Strength Checker")
    pwd = input("Enter your password: ")
    result, feedback = check_password_strength(pwd)
    
    print(f"\nResult: {result}")
    if feedback:
        print("\nSuggestions:")
        for suggestion in feedback:
            print(suggestion)
