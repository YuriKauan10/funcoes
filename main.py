import biblioteca
text = "yurizin"
cont = 0

print("Seu texto ao contrario: ", end = "")
for i in range(len(text) - 1, -1, -1):
    cont += 1
    if text[i] in " ":
        cont -= 1

    print(text[i], end = "")


print(f"\nSeu texto tem {cont} letras")