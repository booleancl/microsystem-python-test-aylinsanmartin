import time 

print("Bienvenido a tu horoscopo")

def menu():
    print("#########")
    print("Selecciona el numero correspondiente")
    print("1","Aquarius")
    print("2","Aries")
    print("3","Cancer")
    print("4","Capricornus")
    print("5","Gemini")
    print("6","Leo")
    print("7","Libra")
    print("8","Pisces")
    print("9","Sagittarius")
    print("10","Scorpio")
    print("11","Taurus")
    print("12","Virgo")
    print("color de la suerte")
    print("0","Salir")
    print("###########")

user_input =""

def read_file(texto):
    file = open("signs/"+ texto,"r", encoding="UTF-8")
    for line in file:
        print(line)

while user_input !="exit":
    menu()

    user_input = input()
    if user_input == "1":
         read_file("aquarius.txt")
    elif user_input == "2":
        read_file("aries.txt")
    elif user_input == "3":
        read_file("cancer.txt")   
    elif user_input == "4":
        read_file("capricornus.txt") 
    elif user_input == "5":
        read_file("gemini.txt")
    elif user_input == "6":
        read_file("leo.txt")
    elif user_input == "7":
        read_file("libra.txt")
    elif user_input == "8":
        read_file("pisces.txt") 
    elif user_input == "9":
        read_file("sagitario.txt")
    elif user_input == "10":
        read_file("scorpio.txt")
    elif user_input == "11":
        read_file("taurus,txt")  
    elif user_input == "12":
        read_file("virgo.txt")
    else:
        print("opcion incorrecta")
            





                   



