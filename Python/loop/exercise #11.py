#Escribir un programa que pida al usuario una palabra y luego muestre por pantalla 
# una a una las letras de la palabra introducida empezando por la última.

word = input("write a word: ")

word_reversed = word[::-1]
letters= list(word_reversed)

l = len(word)
for i in range(l):
    i = letters[i]
    print(i)