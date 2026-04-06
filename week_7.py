import re
def main():
    email = input("What's your email? ").strip()
    if re.search(r"^\w+@(\w+\.)?\w+\.edu$", email, re.IGNORECASE):
        print("Valid edu email!")
    else:
        print("Invalid email.")
if __name__ == "__main__":
    main()
