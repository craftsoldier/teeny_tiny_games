import hashlib

def main():
    strname = ['password123', 'snuffles456']
    
    for name in strname:
        hasher = hashlib.md5(name.encode('utf-8')).hexdigest()
        hashman = hashlib.sha256(name.encode('utf-8')).hexdigest()

        print(name)
        print(hasher)
        print(hashman)

if __name__ == '__main__':
    main()
