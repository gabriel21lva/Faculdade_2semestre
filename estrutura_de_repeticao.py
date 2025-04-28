texto = input("Informe um texto: ")
VOGAIS = "AEIOU"

for letras in texto:
    if letras.upper() in VOGAIS:
        print(letras, end ="")
else:
    print("")
    print("Finalizado o laço")