# media.py

def calcular_media(nota1, nota2, nota3):
    return (nota1 + nota2 + nota3) / 3

def verificar_aprovacao(media):
    if media >= 6:
        return "Aprovado"
    else:
        return "Reprovado"

# Recebe as notas do aluno
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

# Calcula a média
media = calcular_media(nota1, nota2, nota3)

# Exibe o resultado
print(f"A média do aluno é: {media:.2f}")
print(verificar_aprovacao(media))  # Mensagem de aprovação ou reprovação