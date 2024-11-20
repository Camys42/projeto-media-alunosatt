

1. Criar o repositório e clonar no computador
Primeiro, crie um repositório no GitHub chamado projeto-media-alunos e clone-o no seu computador:

bash
Copiar código
git clone https://github.com/seu_usuario/projeto-media-alunos.git
cd projeto-media-alunos
2. Implementação inicial - Cálculo da média simples (branch: main)
No repositório local, crie um arquivo media.py e implemente a lógica para calcular a média simples de 3 notas.

Código:
python
Copiar código
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
Commit da implementação inicial:
bash
Copiar código
git add media.py
git commit -m "Implementação inicial: cálculo da média simples"
git push origin main
3. Criar a branch feature/verificacao-aprovacao
Agora, crie uma nova branch para adicionar a funcionalidade de verificação de aprovação:

bash
Copiar código
git checkout -b feature/verificacao-aprovacao
Modifique o código para incluir a verificação de aprovação:
python
Copiar código
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
Commit da funcionalidade de aprovação:

git add media.py
git commit -m "Adicionada verificação de aprovação"
git push origin feature/verificacao-aprovacao
4. Mesclar a branch feature/verificacao-aprovacao na branch main
Após testar a funcionalidade, mescle a branch feature/verificacao-aprovacao na branch main:


5. Criar a branch feature/verificacao-recuperacao
Crie uma nova branch para adicionar a funcionalidade de verificação de recuperação:


git checkout -b feature/verificacao-recuperacao
Modifique o código para incluir a verificação de recuperação:
python
Copiar código
# media.py

def calcular_media(nota1, nota2, nota3):
    return (nota1 + nota2 + nota3) / 3

def verificar_aprovacao(media):
    if media >= 6:
        return "Aprovado"
    else:
        return "Reprovado"

def verificar_recuperacao(media):
    if 5.0 <= media < 6.0:
        return "Recuperação"
    return ""

# Recebe as notas do aluno
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

# Calcula a média
media = calcular_media(nota1, nota2, nota3)

# Exibe o resultado
print(f"A média do aluno é: {media:.2f}")
print(verificar_aprovacao(media))  # Mensagem de aprovação ou reprovação
print(verificar_recuperacao(media))  # Mensagem de recuperação
Commit da funcionalidade de recuperação:

git add media.py
git commit -m "Adicionada verificação de recuperação"
git push origin feature/verificacao-recuperacao
6. Mesclar a branch feature/verificacao-recuperacao na branch main
Após testar a funcionalidade de recuperação, mescle a branch feature/verificacao-recuperacao na branch principal:


git checkout main
git merge feature/verificacao-recuperacao
git push origin main
7. Criar a branch feature/pesos
Crie uma nova branch para implementar a média ponderada:


git checkout -b feature/pesos
Modifique o código para calcular a média ponderada, onde a primeira e a segunda nota têm peso 1 e a terceira nota tem peso 2:
python
Copiar código
# media.py

def calcular_media_pesada(nota1, nota2, nota3):
    return (nota1 + nota2 + 2 * nota3) / 4  # Média ponderada

def verificar_aprovacao(media):
    if media >= 6:
        return "Aprovado"
    else:
        return "Reprovado"

def verificar_recuperacao(media):
    if 5.0 <= media < 6.0:
        return "Recuperação"
    return ""

# Recebe as notas do aluno
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

# Calcula a média ponderada
media = calcular_media_pesada(nota1, nota2, nota3)

# Exibe o resultado
print(f"A média ponderada do aluno é: {media:.2f}")
print(verificar_aprovacao(media))  # Mensagem de aprovação ou reprovação
print(verificar_recuperacao(media))  # Mensagem de recuperação
