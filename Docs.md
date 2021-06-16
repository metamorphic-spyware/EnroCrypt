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
#### There Are 3 Functions Of Encryption And 4 Functions Of Decryption
### Encryption Functions
  * Encrypt
  * FileEncryption
  * Auth_Encryption
### Decryption Functions
  * Decrypt
  * Decrypt_List
  * FileDecryption
  * Auth_Decryption
### Encrypt
```python
import enrocrypt
encrypted_value = enrocrypt.encryption.Encrypt('secret')
print(encrypted_value)
```
Warning: The List Returned Must Not Be Modified! <br>
Note: The Keys Are For One-Time-Use And Cannot Be Used Again and Again
Arguments: Takes Only One Argument, The Type Must Be string(str)

#### Data Must Be In String Format And The Value Returned Will Be A List
  
### FileEncryption
```python 
import enrocrypt
enrocrypt.encryption.FileEncryption("C://User//whatever//test.txt","keyFile.key")
```
Note: The Only Way To Decrypt The File Is By Using The Key Provided. DONT LOSE THE KEY!!! <br>
Note: The Key File Can Contain Many Keys But 2 Keys For The Same File Is Not Allowed
Arguments: Takes Two Arguments
Path: The Path Of The File you Wnat To Encrypt.
KeyFilePath: The File Path Where You Want To Store The Key.
### Decrypt
```python
import enrocrypt
decrypted_value = enrocrypt.encryption.Decrypt("MyKey","Encrypted Data")
print(decrypted_value)
```
Arguments: Takes Two Arguments 
Key: The Decryption Key
Encrypted_Data: The Encrypted Data
With This Function You Can Decrypt The Encrypted Value But You Have To Extract The Key And The Value From The Returned List. To Avoid This We Created A New Function That Only Takes The Returned List
### Decrypt_List
```python
import enrocrypt
decrypted_value = enrocrypt.encryption.Decrypt_List(MyList)
print(decrypted_value)
```
Arguments: Takes The List Returned By The Encrypt Function
### File_Decryption
```python
import enrocrypt
enrocrypt.encryption.File_Decrypt("C://User//whatever//test.txt","keyFile.key")
```
Arguments: Takes Two Arguments
Path: The Path Of The Encrypted File You Want To Decrypt
KeyFilePath: The File That Has The Decryption Key Of The File
WARNING: If You Change The Location Of The Encrypted File, Even If You Give The Path And KeyFilePath Correct Your File Will Not Be Decrypted As The Key File Remembers The Key To Each File By Its Path (The Path Of The File When You Ran The File_Encryption Function). We Recommend Not To Change The Location Of The Encrypted File
(We Are Working On Updates That Will Return The Key Back Once The File Was Encrypted When File_Encryption Encrypts Any File, Make Sure To Grab It After The Update)
## Hashing
#### Contains All The Hashing Functions
#### There Are 7 Hashing Functions
* Standard_Multi_Hash
* SHA256
* SHA512
* SHA244
* SHA348
* MD5
* BLAKE2
### Standard_Multi_Hash
As You Have Gussed By The Name, This Hashing Function Combines Many Hashing Function And Add Salt In The And Return The Data.
Note: This Function Is Marked Safe-For-Password-Hashing As In Other Functions Two Values Are Never The Same, Which Means That If I Hash b'hello' 2 Times Using The Same Function The Returned Values Will Not Be The Same This Is Because Of The Salt(Changes Everytime the Function Runs)
WARNING: It Is Possible To Guess The Salt As It Is Written In The Source Code, In Future Versions We Will Add A Option To Add Your Own Salt So This Problem Will Be Gone
```python
import enrocrypt
value = enrocrypt.hashing.Standard_Multi_Hash('password')
print(value)
```
(END)
