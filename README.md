# Caesar Cipher

Python implementation of the Caesar cipher crafted while following along with the Practical Cryptography in Python book by Seth Nielson and Christopher K. Monson.

## Shift Substitution

The shift_substitution function generates a Caesar cipher encoding and decoding dictionary based on a given character shift value.

```py
def shift_substitution(shift):
    encoding = {string.ascii_uppercase[i]: string.ascii_uppercase[(i+shift)%len(string.ascii_uppercase)] for i in range(len(string.ascii_uppercase))}
    decoding = {value: key for key, value in encoding.items()}
    return encoding, decoding
```

#### Inputs

shift (int): The character shift value to be applied for encoding and decoding.

#### Flow

* Initialize the empty dictionaries: encoding and decoding.
* Calculate the length of the uppercase alphabet.
* Iterate over each letter in the uppercase alphabet.
* Create a substitution pair by shifting the letter by the response value.
* Populate the encoding and decoding dictionaries with the letter and its corresponding shifted letter.

#### Outputs

Two dictionaries: encoding and decoding, containing the mappings for encoding and decoding Caesar cipher respectively.

* encoding (dict): A dictionary mapping each letter of the alphabet to its substituted letter based on the provided character shift.
* decoding (dict): A dictionary mapping each substituted letter back to its original letter.

## Encoding

The encode function takes a message and a substitution dictionary as inputs, and returns a ciphered message based on the substitution mapping.

```py
def encode(message: str, substitution: Dict[str, str]) -> str:
    return "".join([substitution[letter] if letter in substitution else letter for letter in message.upper()])
```

#### Inputs

message: a string representing the message to be encoded.

substitution: a dictionary containing the mapping of characters to their substituted values.

#### Flow

* Initialize an empty string cipher to store the encoded message.
* Iterate over each letter in the message.
* If the letter is found in the substitution dictionary, append the corresponding value to the cipher.
* If the letter is not in the substitution dictionary, simply append the letter to the cipher.
* Return the final cipher message.

#### Outputs

A string representing the encoded message based on the substitution mapping provided.

## Decoding

The decode function calls the encode function with the provided message and substitution parameters.

```py
def decode(message: str, reverse_substitution: Dict[str, str]) -> str:
    return encode(message.upper(), reverse_substitution)
```

#### Inputs

message: a string representing the message to be decoded.
substitution: a dictionary containing the mapping for decoding the message.

#### Flow

* The decode function takes in a message and a substitution dictionary as input.
* It then calls the encode function with the message and substitution as arguments.
* The encode function processes the message using the provided substitution dictionary.
* The result of the encode function, which is the decoded message, is returned by the decode function.

#### Outputs

The output of the decode function is the decoded message obtained by applying the provided substitution to the original input message.

## Print Table

The print_table function generates and returns a formatted string representing the full alphabet and its corresponding cipher based on the program's current shift value (which would be the minimum of 1 unless manually changed in the menu).

```py
def print_table(substitution: Dict[str, str]) -> str:
    mapping = sorted(substitution.items())

    alphabet_line = "".join([letter for letter,_ in mapping])
    cipher_line = "".join([substitute_letter for _, substitute_letter in mapping])
    return f"Alphabet: {alphabet_line}\nCipher: {cipher_line}"
```

#### Inputs

substitution: A dictionary containing the mapping between alphabet letters and their cipher counterparts.

#### Flow

* Sort the characters of the alphabet provided by the substitution dictionary.
* Generate a string representing the alphabet by concatenating the keys of the sorted dictionary items.
* Generate a string representing the cipher by concatenating the values of the sorted dictionary items.
* Return a formatted string showing the alphabet and cipher mappings based on the current shift value.

#### Outputs

A formatted string showing the alphabet and cipher mappings based on the input substitution dictionary and its current shift value.

## Main

The main section of the program implements a Caesar Cipher encoder and decoder providing a menu-driven interface for the user to interact with the encoding and decoding functionalities.

```py
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
```

#### Inputs

* User's choice selected from the menu options.
* Message input for encoding or decoding.
* New character shift value if the user chooses to change it.

#### Flow

* Initialize a default shift value of 1 as the user's response and generate initial encoding and decoding dictionaries using shift_substitution.
* Displays a menu with options to print encoding/decoding tables, encode a message, decode a message, change character shift, or exit
* Based on the user's choice:

  * Print the encoding and decoding dictionary tables.
  * Encode a user-input message using the current encoding rules.
  * Decode a user-input message using the current decoding rules.
  * Allow the user to input a new character shift value and update the encoding and decoding rules accordingly.
  * Exit the program.
* Repeat the menu display and user interaction until the user chooses to exit.

#### Usage Example & Outputs

**Select an option >> 1**

Display the current encoding and decoding tables with the default shift value of 1.

```py
        if choice == '1':
            print("Encoding Table:")
            print(print_table(encoding))
            print("\nDecoding Table:")
            print(print_table(decoding))
```

![image](https://github.com/acfriday/caesar-cipher-python/assets/82184168/9ec4daae-e0f9-48b2-bfb9-31c7ab75e713)

**Select an option >> 2**

Encoded a message based on user input.

```py
        elif choice == '2':
            message = input("\nMessage to encode:")
            if not message.isalpha():
                print("\nError: Message must contain only alphabetic characters.")
            else:
                print(f"Encoded Message: {encode(message.upper(), encoding)}")
```

![image](https://github.com/acfriday/caesar-cipher-python/assets/82184168/38c229cb-a792-4ba9-b468-1a39c2f2addb)

**Select an option >> 3**

Decoded a message based on user input.

```py
        elif choice == '3':
            message = input("\nMessage to decode:")
            if not message.isalpha():
                print("\nError: Message must contain only alphabetic characters.")
            else:
                print(f"Decoded Message: {decode(message.upper(), decoding)}")
```

![image](https://github.com/acfriday/caesar-cipher-python/assets/82184168/e1e942ba-e5d6-4309-97e1-9897f7940645)

**Select an option >> 4**

Allow the user to input a new character shift value and update the encoding and decoding accordingly. Display a warning message if an invalid character shift value is entered.

```py
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
```

![image](https://github.com/acfriday/caesar-cipher-python/assets/82184168/90ad53d2-aa63-4279-98f8-58ebd1349578)

### Verification of Shift Change

![image](https://github.com/acfriday/caesar-cipher-python/assets/82184168/ae1a8477-5523-4ae9-8771-f3fe2d8a2316)

**Select an option >> 5**

Display an exit message when the user chooses to exit the program.

```py
        elif choice == '5':
            print("Exiting program...\n")
            break
```

![image](https://github.com/acfriday/caesar-cipher-python/assets/82184168/4dd8b105-9b61-4772-90f5-4480f5a8a5d7)

