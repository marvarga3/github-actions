import os

def main():
    lenguaje_favorito=os.getenv("LANGUAGE")
    print(f"Hola, mi lenguaje favoritoes {lenguaje_favorito}")

if __name__=="__main__":
    main()