from cryptography.fernet import Fernet
import os



with open("thekey.key","rb") as lock:
   key= lock.read()
   keys=Fernet(key)

for files in  os.listdir("ransomeware"):
    if files.endswith("txt") or files.endswith("py"):
        path=os.path.join("ransomeware",files)
        print(path)
        try:

            with open(path,"rb") as red:
                content= red.read()

            files_encrypted=keys.decrypt(content)
            with open(path,"wb") as enc:
                enc.write(files_encrypted)    
        except Exception as e:
                print(f"Failed to encrypt {files}: {e}")