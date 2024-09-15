def cripto(caractere):
	num = ord(caractere)
	num += 1
	return chr(num)

def decripto(caractere):
	num = ord(caractere)
	num -= 1
	return chr(num)

frase_original = "Testando projeto de criptográfica em Python - Back End"

frase_cripto = map(cripto, frase_original)
frase_cripto = ''.join(frase_cripto)
print(frase_cripto)

