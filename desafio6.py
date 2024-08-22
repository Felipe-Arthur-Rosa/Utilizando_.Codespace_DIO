def is_palindrome(word):
    # Remove espaços em branco e converte para letras minúsculas
    word = word.replace(" ", "").lower()
    
    # Verifica se a palavra é igual à sua inversão
    if word == word[::-1]:
        return True
    else:
        return False

# Exemplo de uso
word = input("Digite uma palavra: ")
if is_palindrome(word):
    print("A palavra é um palíndromo.")
else:
    print("A palavra não é um palíndromo.")