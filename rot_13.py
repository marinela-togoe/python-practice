import codecs

# The encoded message
encoded_message = "Va gur snpr bs trarengvba gur vaivgr pbqr, znxr n CBFG erdhrfg gb /ncv/ii/vaivgr/trarengv"

# Decoding the message using the codecs library which supports ROT13 encoding/decoding
decoded_message = codecs.decode(encoded_message, 'rot_13')

print(decoded_message)
