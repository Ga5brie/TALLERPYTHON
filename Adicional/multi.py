#UNA CALCULADORA CON LOS NUMEROS QUE DA EÑ USUARIO
print("")
num1=int(input("Escribir el 1 numero: "))
num2=int(input("Escribir el 2 numero: "))
oper=input("Introduce la operacion (+, -, *, /): ")

match oper:
    case "+":
        resl=num1+num2
    case "-":
        resl=num1-num2
    case "*":
        resl=num1*num2
    case "/":
        resl=num1/num2
    

print(f"La resultado de {num1} {oper} {num2} es : {resl}")
