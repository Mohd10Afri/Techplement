import random

def generate_password(length=12, level=3):
    lowercase = 'abcdefghijklmnopqrstuvwxyz'
    uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    digits = '0123456789'
    punctuation = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'

    characters = lowercase + uppercase + digits + punctuation

    if level == 1:
        characters = lowercase + digits
    elif level == 2:
        characters = lowercase + uppercase + digits

    return ''.join(random.choice(characters) for _ in range(length))

def main():
    try:
        length = int(input("Length of the pass: "))
        if length <= 0:
            raise ValueError("Password length must be a positive integer.")
    except ValueError as ve:
        print(ve)
        return

    try:
        level = int(input("Pass complexity level (1/2/3): "))
        if level not in [1, 2, 3]:
            raise ValueError("Invalid level. Defaulting to level 3.")
    except ValueError as ve:
        print(ve)
        level = 3

    password = generate_password(length, level)
    print(f"Your Password: {password}")

if __name__ == "__main__":
    main()
