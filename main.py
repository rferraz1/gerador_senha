import random
import string

def gerar_senha(tamanho, maiusculas=True, minusculas=True, numeros=True, especiais=True):
    caracteres = ''
    if maiusculas:
        caracteres += string.ascii_uppercase
    if minusculas:
        caracteres += string.ascii_lowercase
    if numeros:
        caracteres += string.digits
    if especiais:
        caracteres += string.punctuation
    if not caracteres:
        raise ValueError("Selecione ao menos um tipo de caractere.")
    return ''.join(random.choice(caracteres) for _ in range(tamanho))

def main():
    print("Gerador de Senhas")
    tamanho = int(input("Tamanho da senha: "))
    senha = gerar_senha(tamanho)
    print(f"Senha gerada: {senha}")

if __name__ == "__main__":
    main()
