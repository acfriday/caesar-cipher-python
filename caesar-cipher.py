from typing import Dict
import string

def shift_substitution(shift):
    encoding = {string.ascii_uppercase[i]: string.ascii_uppercase[(i+shift)%len(string.ascii_uppercase)] for i in range(len(string.ascii_uppercase))}
    decoding = {value: key for key, value in encoding.items()}
    return encoding, decoding

def encode(message: str, substitution: Dict[str, str]) -> str:
    return "".join([substitution[letter] if letter in substitution else letter for letter in message.upper()])

def decode(message: str, reverse_substitution: Dict[str, str]) -> str:
    return encode(message.upper(), reverse_substitution)

def print_table(substitution: Dict[str, str]) -> str:
    mapping = sorted(substitution.items())

    alphabet_line = "".join([letter for letter,_ in mapping])
    cipher_line = "".join([substitute_letter for _, substitute_letter in mapping])
    return f"Alphabet: {alphabet_line}\nCipher: {cipher_line}"
def main():
    min_shift = 1
    encoding, decoding = shift_substitution(min_shift)
    while True:
        print("\n   Caesar Cipher | Encoder & Decoder")
        print("   `````````````````````````````````")
        print("1. Print Encoding/Decoding Tables.")
        print("2. Encode Message.")
        print("3. Decode Message.")
        print("4. Change Character Shift.")
        print("5. Exit\n")
        try:
            choice = input("Select an option >> ").strip()
        except ValueError:
            print("Invalid input. Please enter a valid option from the menu.")
            continue

        if choice == '1':
            print("Encoding Table:")
            print(print_table(encoding))
            print("\nDecoding Table:")
            print(print_table(decoding))

        elif choice == '2':
            message = input("\nMessage to encode:")
            if not message.isalpha():
                print("\nError: Message must contain only alphabetic characters.")
            else:
                print(f"Encoded Message: {encode(message.upper(), encoding)}")

        elif choice == '3':
            message = input("\nMessage to decode:")
            if not message.isalpha():
                print("\nError: Message must contain only alphabetic characters.")
            else:
                print(f"Decoded Message: {decode(message.upper(), decoding)}")

        elif choice == '4':
            new_shift = input(f"\nInput new character shift (currently set to ({min_shift})): ")
            try:
                new_shift = int(new_shift)
                if new_shift < 1:
                    print("\nWarning: The character shift must be greater than 0 or your message will not be altered.")
                    shift_substitution(min_shift)
                else:
                    min_shift = new_shift
                    encoding, decoding = shift_substitution(min_shift)
            except ValueError:
                print(f"\nYour input '{new_shift}' is not a valid number.")

        elif choice == '5':
            print("Exiting program...\n")
            break

        else:
            print(f"Unknown option ({choice}) selected.")

if __name__ == "__main__":
    main()