# Caesar Cipher

Python implementation of the Caesar cipher generated while following along with the Practical Cryptography in Python book by Seth Nielson and Christopher K. Monson.

#### Parameters

* Response (int): The character shift value to be applied for encoding and decoding.

#### Returns

A tuple containing two dictionaries - Encoding and Decoding.

* Encoding (dict): A dictionary mapping each letter of the alphabet to its substituted letter based on the provided character shift.
* Decoding (dict): A dictionary mapping each substituted letter back to its original letter.

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

`print(encoded_message)`

`Output: "TFDSFU"`

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

`print(dencoded_message)`

`Output: "SECRET"`

## Print Table

The print_table function generates and returns a formatted string representing the full alphabet and its corresponding cipher based on the programs current shift value.

#### Inputs

substitution: A dictionary containing the mapping between alphabet letters and their cipher counterparts.

#### Flow

* Sort the characters of the alphabet provided by the substitution dictionary.
* Generate a string representing the alphabet by concatenating the keys of the sorted dictionary items.
* Generate a string representing the cipher by concatenating the values of the sorted dictionary items.
* Return a formatted string showing the alphabet and cipher mappings based on the current shift value.

#### Outputs

A formatted string showing the alphabet and cipher mappings based on the input substitution dictionary and its shift value.

#### Usage Example

`shift = 2`

`substitution = {'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'}`

`cipher =  {'Y','Z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X'}`

`print(print_table(substitution))`

`output: Decoding Table:`

`alphabet: ABCDEFGHIJKLMNOPQRSTUVWXYZ`

`cipher: YZABCDEFGHIJKLMNOPQRSTUVWX`