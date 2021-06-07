---
permalink: /Docs.html
---
# File System
### The File System Of EnroCrypt Contain Three Main Files
  * encryption
  * hashing
  * basic
## Encryption
#### Contains All The Encryptions-Decryption Methods Packed In Functions
#### There Are 2 Functions Of Encryption And 3 Functions Of Decryption
### Encryption Functions
  * Encrypt
  * FileEncryption
### Decryption Functions
  * Decrypt
  * Decrypt_List
  * FileDecryption
### Encrypt
```python
import enrocrypt
encrypted_value = enrocrypt.encryption.Encrypt('secret')
print(encrypted_value)
```
Warning: The List Returned Must Not Be Modified!
Note: The Keys Are For One-Time-Use And Cannot Be Used Again and Again
#### Data Must Be In Bytes Format And The Value Returned Will Be A List
### FileEncryption
```python 
import enrocrypt
enrocrypt.encryption.FileEncryption("C://User//whatever//test.txt","keyFile.key")
```
Note: The Only Way To Decrypt The File Is By Using The Key Provided. DONT LOSE THE KEY!!!
Note: The Key File Can Contain Many Keys But 2 Keys For The Same File Is Not Allowed
### Decrypt
```python
import enrocrypt
decrypted_value = enrocrypt.encryption.Decrypt("MyKey","Encrypted Data")
print(decrypted_value)
```
With This Function You Can Decrypt The Encrypted Value But You Have To Extract The Key And The Value From The Returned List. To Avoid This We Created A New Function That Only Takes The Returned List
### Decrypt_List
```python
import enrocrypt
decrypted_value = enrocrypt.encryption.Decrypt_List(MyList)
print(decrypted_value)
```
### File_Decryption
```python
import enrocrypt
enrocrypt.encryption.File_Decrypt("C://User//whatever//test.txt","keyFile.key")
```
## Hashing
#### Contains All The Hashing Functions
(Not Yet Published)
