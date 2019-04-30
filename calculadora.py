
operacion_matematica = input("¿Que operacion, quieres realizar? (Multiplicar / Dividir / Sumar / Restar")

primer_numero = int(input( "Introduce primer numero"))
segundo_numero = int(input( "Introduce el segundo numero"))

if operacion_matematica == "Multiplicar":
    Resultado = primer_numero * segundo_numero

elif operacion_matematica == "Dividir":
    Resultado = primer_numero / segundo_numero

elif operacion_matematica == "Sumar":
    Resultado = primer_numero + segundo_numero

elif operacion_matematica == "Restar":
    Resultado = primer_numero - segundo_numero

print("Resultado {}".format(Resultado))













