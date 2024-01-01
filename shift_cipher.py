def encrypt_shift(plaintext, shift):
    encrypted_text = ""
    for char in plaintext:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            encrypted_text += chr((ord(char) - start + shift) % 26 + start)
        else:
            encrypted_text += char
    return encrypted_text

def decrypt_shift(ciphertext, shift):
    return encrypt_shift(ciphertext, -shift)

while(True):
	print("Menu:\n1 for encryption\n2 for decryption\n3 to exit")
	ch=int(input())
	if ch==3:
		print("Exiting...")
		exit()
	if ch==1:
		# Encrypt
		print("Enter your message: ")
		plaintext=input()
		print("Enter the shift value to encrypt with: ")
		shift_value = int(input())
		encrypted_text = encrypt_shift(plaintext, shift_value)
		print(f"Encrypted: {encrypted_text}")
	elif ch==2:

		# Decrypt
		print("Enter your message: ")
		plaintext=input()
		print("Enter the shift value to decrypt with: ")
		shift_value = int(input())
		decrypted_text = decrypt_shift(encrypted_text, shift_value)
		print(f"Decrypted: {decrypted_text}")
	else:
		print("invalid choice! Exiting.")
		exit()
