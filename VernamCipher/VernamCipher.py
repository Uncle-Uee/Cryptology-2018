"""
Created By: Uee
Modified By:
"""

"""
	NB!!!
	The ASCII values between 0-31 are not represented in a readable format. These ASCII values usually are
	displayed by a 'funny character' Character.

	To Display the "funny character" ASCII Characters in a more Readable manner the Lists Below
	"UNKNOWN ASCII VALUES CHAR" & "UNKNOW ASCII VALUES FUNC" are used to do the correct conversion.
"""

UNKNOWN_ASCII_VALUES_CHAR = [
	"NUL", "SOH", "STX", "ETX", "EOT", "ENQ", "ACK", "BEL", "BS", "HT", "LF", "VT", "FF", "CR", "SO", "SI", "DLE",
	"DC1", "DC2", "DC3", "DC4", "NAK", "SYN", "ETB", "CAN", "EM", "SUB", "ESC", "FS", "GS", "RS", "US"
]

UNKNOWN_ASCII_VALUES_FUNC = ["NULL", "Start of Heading", "Start of Text", "End of Text", "End of Transmit",
                             "Enquiry", "Acknowledge", "Bell", "Backspace", "Horizontal Tab", "Line Feed",
                             "Vertical Tab", "Form Feed", "Carriage Return", "Shift Out", "Shift In",
                             "Data Line Escape", "Device Control 1", "Device Control 2", "Device Control 3",
                             "Device Control 4", "Non Acknowledge", "Synchronous Idle", "End Transmit Block",
                             "Cancel", "End of Medium", "Substitute", "Escape", "File Separator",
                             "Group Separator", "Record Separator", "Unit Separator"]

def VernamCipher(text = "", key = ""):
	"""
	Vernam Cipher Function converts a plain text message to an encrypted message using the XOR Bitwise Function or
	converts an encrypted text message to a plain text message using the XOR Bitwise Function.

	:param text: Plain Text | Encrypted Message
	:param key: Secret Key
	:return: Encrypted | Decrypted Message
	"""

	# Convert Text and Key strings to a list of ASCII Values or Codes.
	KEY_ASCII = list(ord(c) for c in key)
	TEXT_ASCII = list(ord(c) for c in text)

	# Resize the Key ASCII list if the Length of the Text ASCII list is greater.
	if len(text) > len(key):
		ResizeKey(KEY_ASCII, len(text) - len(key))

	# Compute the XOR values using the ASCII values of the Text and Key characters.
	cipherASCII = list(TEXT_ASCII[i] ^ KEY_ASCII[i] for i in range(len(TEXT_ASCII)))

	# Convert the cipher ASCII values to binary values using the 'bin' function.
	cipherBIN = " ".join(str(i) for i in list(bin(i) for i in cipherASCII))

	# Convert the cipher ASCII values to Hexadecimal values using the 'hex' function.
	cipherHEX = " ".join(str(i) for i in list(hex(i) for i in cipherASCII))

	# Convert the cipher ASCII values to readable characters using the 'chr' function.
	cipherTEXT = "".join(chr(c) for c in cipherASCII)

	# return all the computed values
	return cipherASCII, cipherBIN, cipherHEX, cipherTEXT

def MakeCipherReadable(cipherASCII = list(), functionName = False):
	"""
	Used to Convert a list of Cipher Text ASCII codes between 0-31 (inclusive) to a readable ASCII string
	using the UNKNOWN ASCII VALUES CHAR or FUNC lists.

	:param cipherASCII: List of ASCII values of the Cipher Text
	:param functionName: Boolean to compile the readable Cipher String using the UNKNOWN ASCII VALUES FUNC or
	UNKNOWN ASCII VALUES CHAR.
	:return: A readable Cipher String.
	"""

	# concat an UNKNOWN ASCII FUNC | CHAR found at the 'i'th index if the 'i'th index is <= 31, otherwise concat an
	# ASCII chr(i) for every 'i'th index in cipherASCII
	if functionName:
		return ". ".join(UNKNOWN_ASCII_VALUES_FUNC[i] if i <= 31 else chr(i) for i in cipherASCII)

	return ". ".join(UNKNOWN_ASCII_VALUES_CHAR[i] if i <= 31 else chr(i) for i in cipherASCII)

def ResizeKey(keyAscii = list(), length = 0):
	"""
	Resize the KEY ASCII List by appending additional elements to it.
	:param keyAscii: List of ASCII Values or Codes made from the Key string.
	:param length: Difference between the Length of the Text and Key strings
	:return: Resized List of KEY ASCII Values or Codes.
	"""
	for i in range(length):
		keyAscii.append(keyAscii[i])

"""
	Part 1
	In Part 1, we will Encrypt a 'text' using the Vernam Cipher and then display the Cipher Text in Character format.

	NB!!!
	Where 'text', text = "Plain Text" as input from user.
"""

# Store all output received from VernamCipher Function.
# Request user to input Plain Text Message to Encrypt.
# Input a secret Key for the 'key' parameter.
key = str(input("Enter a Secret Key: "))
cipherASCII, cipherBIN, cipherHEX, cipherTEXT = VernamCipher(text = str(input("Enter a Secret Message: ")), key = key)

"""
	Uncomment the Lines Below to display additional information, such as the ASCII, Binary and Hexadecimal Formats 
	of the Encrypted message.
"""

# print("\nThe Encrypted Cipher Text ASCII Codes: ")
# print(" ".join(str(i) for i in cipherASCII) + "\n")

# print("\nThe Encrypted Cipher Text BINARY Codes: ")
# print(cipherBIN + "\n")

# print("\nThe Encrypted Cipher Text HEXADECIMAL Codes: ")
# print(cipherHEX + "\n")

print("\nThe Encrypted Cipher Text: ")
print(cipherTEXT + "\n")

print("\nThe Readable Encrypted Cipher Text: ")
print(MakeCipherReadable(cipherASCII) + "\n")

"""
	Part 2
	In Part 2, we will do the Decryption of the 'cipherTEXT' using the XOR Vernam Cipher and then display the 
	Original Plain Text Message.

	NB!!!
	Where 'cipherTEXT', cipherTEXT = "Encrypted Message"
"""

# Store all output received from VernamCipher Function.
# Input the Encrypted Text for the 'text' parameter.
# Input the pre-made secret Key for the 'key' parameter.
plainTextASCII, plainTextBIN, plainTextHEX, plainTEXT = VernamCipher(text = cipherTEXT, key = key)

"""
	Uncomment the Lines Below to display additional information, such as the ASCII, Binary and Hexadecimal Formats 
	of the Decrypted message.
"""

# print("\nThe Plain Text ASCII Codes: ")
# print(" ".join(str(i) for i in plainTextASCII) + "\n")

# print("\nThe Plain Text BINARY Codes: ")
# print(plainTextBIN + "\n")

# print("\nThe Plain Text HEXADECIMAL Codes: ")
# print(plainTextHEX + "\n")

print("\nThe Decrypted Plain Text Message: ")
print(plainTEXT + "\n")
