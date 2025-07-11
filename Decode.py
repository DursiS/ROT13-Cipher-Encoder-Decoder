from Alphabet import alphabet

# Asks what to decode, then moves each letter 13 characters BACK in the alphabet
def decode(alphabet):
    decoded = []
    
    # Asks to what to decode
    text_input = input("Enter Text: ").lower()
    
    # Encodes
    for char in text_input:
        if char in alphabet:
            alpha_index = alphabet.index(char)
            decoded.append(alphabet[((alpha_index - 13) % 26)])
        else:
            encoded.append(char)
                
    decoded = ''.join(decoded)
    return decoded