#02 Licencia
def main():
#escribe tu código abajo de esta línea
    edad = int(input("Ingresa tu edad: "))

    if edad>=18:
        
        id_oficial = str(input("¿Tienes identificación oficial? (s/n): "))
    
        if id_oficial=='s' or id_oficial=='n':
            
            if id_oficial=='s':
                print("Trámite de licencia concedido")
            else:
                print("No cumples requisitos")
        else:
            print("Respuesta incorrecta")
    
    elif edad>0 and edad<18:
        print('No cumples requisitos')

    else:
        print("Respuesta incorrecta")

if __name__=='__main__':
    main()