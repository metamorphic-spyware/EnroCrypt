# EnroCrypt
This is a Python Module For Encryption, Hashing And Other Basic Stuff You Need, With Secure Encryption And Strong Salted Hashing You Can Do Whatever You Want To  
## Installation
EnroCrypt Is Avaliable On <a style="text-decoration:none;" herf="https://pypi.org/projects/enrocrypt">PyPi </a>You Can Install It As Follows:<br>
```` pip install -U enrocrypt````
## Manual Installation 
If For Some Reason You Can't Install EnroCrypt From PyPi You Can Download It Manually Too:
* Clone This Repo 
* Cut-Paste This Repo In Your Python Scripts Path
* Enter In The Folder Where You See "setup.py" file
* shift+right click in the Folder And Click On "Open Powershell window Here"
* Type `python setup.py install`<br>
After Following All The Steps Mentioned Above (If You Don't Get An Error) EnroCrypt Is Installed, Now You Can Import It Right Away
## Features
* Strong Encryption
* Strong Salted Hashing
* File Encryption-Decryption
* Some Basic Functions
## Usage 
```python
    # For Encryption
    import enrocrypt
    value = enrocrypt.encryption.Encrypt(b'text')
    print(value)
    # For Decryption
    original_value = enrocrypt.encryption.DecryptList(value)
    print(original_value)
```
There Is Also a `Decrypt`Function, But In This Function You Have To Enter The Key And The Data Seperatly
