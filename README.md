# Caesar Cipher

Python implementation of the Caesar cipher generated while following along with the Practical Cryptography in Python book by Seth Nielson and Christopher K. Monson.

## Shift Substitution

The shift_substitution function generates a Caesar cipher encoding and decoding dictionary based on a given character shift value.

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

#### Usage Example

`shift = 3`

`encoding, decoding = shift_substitution(response)`

`print(encoding) == {'A': 'D','B': 'E','C': 'F'}`

`print(decoding) ==  {'D': 'A','E': 'B','F': 'C'}`

## Encoding

The encode function takes a message and a substitution dictionary as inputs, and returns a ciphered message based on the substitution mapping.

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

#### Usage Example

`message = "SECRET"`

`input dictionary = {'S','E','C','R','E','T'}`

`substitution = {'T', 'F', 'D', 'S', 'F', 'U'}`

`encoded_message = encode(message, substitution)`

`print(encoded_message) == "TFDSFU"`

## Decoding

The decode function calls the encode function with the provided message and substitution parameters.

#### Inputs

message: a string representing the message to be decoded.
substitution: a dictionary containing the mapping for decoding the message.

#### Flow

* The decode function takes in a message and a substitution dictionary as input.
* It then calls the encode function with the message and substitution as arguments.
* The encode function processes the message using the provided substitution dictionary.
* The result of the encode function, which is the decoded message, is returned by the decode function.

#### Outputs

The output of the decode function is the decoded message obtained by applying the provided substitution to the input message.

#### Usage Example

`message = "TFDSFU"`

`input dictionary = {'T', 'F', 'D', 'S', 'F', 'U'}`

`substitution = {'S','E','C','R','E','T'}`

`dencoded_message = dencode(message, substitution)`

`print(dencoded_message) == "SECRET"`

## Print Table

The print_table function generates and returns a formatted string representing the full alphabet and its corresponding cipher based on the programs currently provided shift value.

#### Inputs

substitution: A dictionary containing the mapping between alphabet letters and their cipher counterparts.

#### Flow

* Sort the characters of the alphabet provided by the substitution dictionary.
* Generate a string representing the alphabet by concatenating the keys of the sorted dictionary items.
* Generate a string representing the cipher by concatenating the values of the sorted dictionary items.
* Return a formatted string showing the alphabet and cipher mappings based on the current shift value.

#### Outputs

A formatted string showing the alphabet and cipher mappings based on the input substitution dictionary and its current shift value.

#### Usage Example

`shift = 2`

`substitution = {'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'}`

`cipher =  {'Y','Z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X'}`

`print(print_table(substitution)) == Decoding Table:`

`alphabet: ABCDEFGHIJKLMNOPQRSTUVWXYZ`

`cipher: YZABCDEFGHIJKLMNOPQRSTUVWX`

## Main

The main section of the program implements a Caesar Cipher encoder and decoder providing a menu-driven interface for the user to interact with the encoding and decoding functionalities.

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

`Encoding Table:`
`Alphabet: ABCDEFGHIJKLMNOPQRSTUVWXYZ`
`Cipher: BCDEFGHIJKLMNOPQRSTUVWXYZA`

`Decoding Table:`
`Alphabet: BCDEFGHIJKLMNOPQRSTUVWXYZA`
`Cipher: ABCDEFGHIJKLMNOPQRSTUVWXYZ`

**Select an option >> 2**

Encoded a message based on user input.

`Message to encode: Hello`
`Encoded Message: IFMMP`

**Select an option >> 3**

Decoded a message based on user input.

`Message to decode: IFMMP`
`Decoded Message: HELLO`

**Select an option >> 4**

Allow the user to input a new character shift value and update the encoding and decoding accordingly. Display a warning message if an invalid character shift value is entered.

`Input new character shift (currently set to (1)): 3`

**Select an option >> 5**

Display an exit message when the user chooses to exit the program.

`Exiting program...`
