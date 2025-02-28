operasjon = input("Velg en operasjon som er + - * /: ")
num1 = float(input("Skriv et tall: "))
num2= float(input("Skriv et tall til:"))

resultat = None

if (operasjon == "+"):
    resultat = num1 + num2
    
elif (operasjon == "-"):
    if num1 < num2:
        print("num1 må være større en sum2")
        
    else: 
     resultat = num1 - num2
     
     
elif(operasjon == "*"):
    resultat =num1 * num2
    
elif (operasjon == "/"):
    if num2 == 0:
        print("Det er en umulig oprasjon")
       
    else:
     resultat = num1 / num2
     
else:
    print ("Det funker ikke")  
   
if resultat is not None:
 print(f"Resultat: {resultat}")
