import Encode
import Decode
from Alphabet import alphabet
prompt = ""
output_text = ""

# Asks weather to encode or decode
while prompt not in ["encode", "decode"]:
    prompt = input("ROT 13 Encode or Decode: ").lower()
    
# Encodes
if prompt == "encode":
    output_text = Encode.encode(alphabet)
    print(f">>{output_text}")
    
# Decodes
if prompt == "decode":
    output_text = Decode.decode(alphabet)   
    print(f">>{output_text}")