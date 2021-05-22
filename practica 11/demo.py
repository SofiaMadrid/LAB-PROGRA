s= input("Escribe algo : ")
with open("archivo_random.txt", "w") as file:
    file.write(s)
print("\nFelicidades, El archivo ha sido escrito. \n Se llama archivo_random.txt")
input("\npresiona una tecla para continuar...")
