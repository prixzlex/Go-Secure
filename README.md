Pxtoolx Encryptor/Decryptor Script Documentation
This script provides an easy way for users to encrypt a folder and all its subdirectories, making the files inaccessible to anyone without the decryption key. The decryption key is sent to the user's email address and stored in a database for backup purposes.

Features
Encrypts/Decrypts files and directories with a secret key
Encrypts/Decrypts files using the XOR operator and a secret key
Renames encrypted files with a .3vil extension
Sends encryption/decryption key to user's email address
Backs up encryption/decryption key and system information to a database
Multi-threaded for faster encryption/decryption


Requirements
Python 3.x
Requests module (for sending system information to remote server)
tkinter module (for selecting directories)
hashlib module (for generating SHA-256 hash of secret key)
secrets and string modules (for generating random letters for secret key)
queue module (for multi-threading)
PHP version 7 or higher
dotenv library
MySQL database
Email server (SMTP)


Usage
Run the Python script
Choose whether to encrypt or decrypt files by typing 1 or 2.
Choose the directory to encrypt/decrypt by clicking the OK button in the file dialog box.
Enter an confirm a valid email address when prompted (for encryption only).
Enter the decryption key (for decryption only).
Wait for the encryption/decryption process to complete.

Security
The script uses a symmetric encryption algorithm based on the XOR operator and a secret key. The secret key is generated from the user's computer name and a random letter, which makes it difficult for an attacker to guess the key. The script also sends the encryption/decryption key to the user's email address, which ensures that only the user has access to the key.

Limitations ***
The script is designed to encrypt/decrypt only one directory at a time. It does not support encryption/decryption of multiple directories or files.
This script is not meant to provide military-grade encryption and should not be used as such.


Disclaimer
The Pxtoolx Encryptor/Decryptor script is provided for educational purposes only. The author does not condone or encourage the use of this script for illegal activities. The user of this script assumes all responsibility for any consequences resulting from malicious use of this script.
