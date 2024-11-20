# projeto-media-alunosatt
# Projeto: Cálculo de Média de Alunos

Este repositório contém um simples programa Python desenvolvido para calcular a média das notas de um aluno. O programa foi projetado com algumas funcionalidades adicionais, como verificação de aprovação, recuperação e cálculo da média ponderada.

## Objetivo

O objetivo deste projeto é calcular a média das 3 notas fornecidas por um aluno, verificar sua situação (aprovado, reprovado ou em recuperação) e calcular uma média ponderada com pesos diferentes para cada nota.

## Funcionalidades

O programa possui as seguintes funcionalidades:

1. **Cálculo da Média Simples**:
   - Recebe as 3 notas do aluno e calcula a média aritmética simples.
   
2. **Verificação de Aprovação**:
   - Se a média for **maior ou igual a 6**, o aluno é considerado **aprovado**.
   - Caso contrário, o aluno é considerado **reprovado**.

3. **Verificação de Recuperação**:
   - Se a média for **maior ou igual a 5.0 e menor que 6.0**, o aluno está em **recuperação**.

4. **Cálculo da Média Ponderada**:
   - A média ponderada é calculada levando em consideração pesos diferentes para as notas:
     - Primeira e segunda nota têm **peso 1**.
     - A terceira nota tem **peso 2**.

## Como Rodar o Projeto

Para rodar o projeto, siga os seguintes passos:

### 1. **Clone o Repositório**

Clone este repositório para sua máquina local usando o Git:

```bash
git clone https://github.com/seu_usuario/projeto-media-alunos.git
cd projeto-media-alunos
