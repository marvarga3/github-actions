import os

def main():
    nombre=os.getenv("USERNAME")
    edad=32
    print(f"Hola, {nombre} desde Github")

if __name__=="__main__":
    main()