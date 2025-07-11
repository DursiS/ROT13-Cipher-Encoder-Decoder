from Alphabet import alphabet

# Asks what to encode, then moves each letter 13 characters in the alphabet
def encode(alphabet):
    encoded = []
    
    # Asks to what to encode
    text_input = input("Enter Text: ").lower()
       
    # Decodes
    for char in text_input:
        if char in alphabet:
            alpha_index = alphabet.index(char)
            encoded.append(alphabet[(alpha_index + 13) % 26])
        else:
            encoded.append(char)
        
    encoded = ''.join(encoded)
    return encoded
    