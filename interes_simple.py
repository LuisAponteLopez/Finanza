print("************************************************************************")
print("Este programa calcula el principa con cierto interes a un cierto periodo")
print("************************************************************************")
def main():
    principal = eval(input("Ingrese la cantidad principal en dolares: $"))
    apr = eval(input("Ingrese la cantidad de interes en decimal: "))
    year = eval(input("Ingrese la cantidad de year "))
    for i in range(year):
        principal=principal*(1+apr)# va cambiando en valor principal durante va repitiendo el ciclo
    
    print("\nSu cantidad futura es $",round(principal,2)) #nos da la cantidad final de principal , luego de calcularlo 10 veces 
                                                           # el round(primcipal,2) nos redondea a 2 espacio decimal
    print("\nGracias por usar el programa. Regresa pronto.")
main()
    
