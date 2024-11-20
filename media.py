# media.py

# Função para calcular a média simples das 3 notas
def calcular_media(nota1, nota2, nota3):
    return (nota1 + nota2 + nota3) / 3

# Recebe as notas do aluno
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

# Calcula a média
media = calcular_media(nota1, nota2, nota3)

# Exibe o resultado
print(f"A média do aluno é: {media:.2f}")