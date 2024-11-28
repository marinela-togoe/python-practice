import itertools
from collections import Counter

def decrypt_substitution(ciphertext, language_freq_order):
    # Remove spaces and punctuations for frequency analysis
    letters_only = ''.join(filter(str.isalpha, ciphertext.replace(' ', '').upper()))
    
    # Count frequency of each letter and sort by most common
    frequency_order_ciphertext = [item[0] for item in Counter(letters_only).most_common()]
    
    # Assume the most common letter in ciphertext is the most common letter in the Dutch language
    # This is a starting assumption and the actual solution will require more detailed frequency analysis
    translation_table = str.maketrans(''.join(frequency_order_ciphertext), ''.join(language_freq_order))
    
    # Decrypt the ciphertext with the assumed translation table
    return ciphertext.translate(translation_table)

# The ciphertext to decrypt
ciphertext = "NVPPBZ MZHHZQ LEZD AZTO LZPZWZTD QEWB IEDZ OTGOZTC"

# The most frequent letters in the Dutch language in order
# Replace this with the actual frequency order if available
dutch_freq_order = 'EANTRIOKDLMSGVHUWBCFJPXYZQ'

# Decrypt the ciphertext with the initial frequency mapping
decrypted_text = decrypt_substitution(ciphertext, dutch_freq_order)

print(decrypted_text)

