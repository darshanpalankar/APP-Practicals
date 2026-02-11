import os

def create(filename):
    try:
        with open(filename,"w") as f:
            pass
        print(f"File {filename} is created successfully.")
    except Exception as e:
        print("File can't be created.")

def write(filename, content):
    try:
        with open(filename,"w") as f:
            f.write(content)
            print(f"File {filename} is written successfully.")
    except Exception as e:
        print("File can't be written.")

def read(filename):
    try:
        with open(filename,"r") as f:
            content =  f.read()
            print(content)   
    except Exception as e:
        print("Error while reading.")  
    
def append_file(filename, content):
    try:
        with open(filename,"a") as f:
            f.write(content)
        print(f"File {filename} is written successfully.")
    except Exception as e:
        print("File can't be written.")

def delete(filename):
    try:
        os.remove(filename)
        print(f"File {filename} is removed successfully.")
    except Exception as e:
        print("File can't be removed.")
    filename = "42_47.txt"

def main():
    while True:
        print("1. Create File\n2. Write in File\n3. Read file\n4. Append in File\n5. Delete File\n6. Exit")
        choice = int(input("Enter your Choice : "))
        filename = input("Enter file name : ")
        if choice == 1:
            create(filename)
        elif choice == 2:
            content = input("Enter content : ")
            write(filename, content)
        elif choice == 3:
            read(filename)
        elif choice == 4:
            content = input("Enter content : ")
            append_file(filename,content)
        elif choice == 5:
            delete(filename)
        elif choice == 6:
            break
        else:
            print("Invalid Choice")

if __name__ == "__main__":
    main()
