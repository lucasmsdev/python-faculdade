#tarefa 1: Escreva um programa que leia 3 notas de um aluno e a média das notas dos exercícios realizados
#por ele. Calcular a média de aproveitamento, usando a fórmula: MA = (N1 + N2*2 + N3*3 + ME)/7. A
#partir da média, informar o conceito de acordo com os itens abaixo:
#maior ou igual a 9 // menor que 4

#Entrando com as variáveis 
nota1 = float(input("Entre com sua primeira nota: "))
nota2 = float(input("Entre com sua segunda nota: "))
nota3 = float(input("Entre com sua terceira nota: "))
#calculos da média e média aproveitamento
media = nota1 + nota2 + nota3/3
mediaA = (nota1 + nota2*2 + nota3*3 + media)/7
#Sistema booleano para a validação da média e print de resutaldos
if mediaA >= 9:
    print("Você está acima da média com a nota: ", mediaA)
elif mediaA < 4:
    print("Você está abaixo da média com a nota: ", mediaA)    
else:
    print("você está na média com a nota: ", mediaA)
    
#/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/

#Tarefa 2: Elabore um programa que solicita: nome, endereço, CEP e telefone. Imprima na tela os
#valores conforme abaixo: nome na primeira linha, endereço na segunda linha, CEP e telefone na terceira linha.

#entrando com as variáveis 
nome = input("Digite o seu nome: ")
endereco = input("Digite seu endereço: ")
cep = int(input("Digite seu CEP: "))
num = int(input("digite seu número de telefone: "))
#printando os dados
print("nome: ",nome,"\nEndereço: ",endereco,"\nCEP: ",cep," Telefone: ",num)

#/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/

#Tarefa3: Escreva um programa que imprima na tala a figura abaixo:
#XXXXX
#X   X
#X   X
#X   X
#XXXXX

#imprimindo a figura
print("XXXXX\nX   X\nX   X\nX   X\nXXXXX")

#/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/

#tarefa 4: Escreva um programa que o usuário deva entrar com o nome do aluno e sua nota. Exiba o valor
#conforme abaixo:
#ALUNO(A) NOTA
#======== =====
#ALINE 9.0

#Entrando com variáveis
nome = input("Digite o nome do aluno: ")
nota = int(input("Digite a nota do aluno: "))
#imprimindo os dados
print("Aluno       Nota\n=======    =====\n",nome,'   ',nota)

#/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/

#Tarefa 5: 5 - Elabore um programa que mostre o seguinte menu na tela: Cadastro de Clientes
#0 - Fim
#1 - Inclui
#2 - Altera
#3 - Exclui
#4 - Consulta
#Quando o usuário entrar com uma opção exibir o item. Se entrar com um valor diferente do menu exibir item não encontrado.

#printando o menu
print("Menu do cliente:")
print("0 - Fim\n1 - Inclui\n2 - Altera\n3 - Exclui\n4 - Consulta")
#declarando a variável de escolha do cliente
escolha = int(input("Escolha a opção deseja: "))

#Sistema booleano para a escolha do cliente
if escolha == 0:
    print("Você escolheu sair")

elif escolha == 1:
    print("Bem-vindo ao sistema")
    cadastro = input("Informe seu nome para cadastrar: ")
    print("Cliente ",cadastro," cadastrado com sucesso!")

elif escolha == 2:
    print("Ainda não há cadastros feitos")

elif escolha == 3:
    delete = input("Tem certeza que deseja excluir seu cadastro?(Y para sim // N para não) ")
    if delete == "Y" or delete == "y":
        print("Cadastro excluído com sucesso")
    else:
        print("Cadastro não excluído")

elif escolha == 4:
    print("Aguarde por gentileza, checando os dados...")   

else:
    print("Item não encontrado")  

#/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/

#Tarefa 6: Implemente um programa que desenhe um "pinheiro" na tela,similar ao abaixo. O valor de Xdeve ser fornecido pelo usuário.  

#Pegando o que o usuário deseja fazer o pinheiro
p = input("Digite UM caractere: ")   
#imprimindo o pinheiro
print('      ',p)
print('     ',p+p+p)
print('    ',p+p+p+p+p)
print('   ',p+p+p+p+p+p+p)
print('  ',p+p+p+p+p+p+p+p+p)
print(' ',p+p+p+p+p+p+p+p+p+p+p)
print('',p+p+p+p+p+p+p+p+p+p+p+p+p)
print(p+p+p+p+p+p+p+p+p+p+p+p+p+p+p)
print('     ',p+p)
print('     ',p+p)
print('    ',p+p+p+p)

#/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/

#Tarefa 7: Sendo x uma variável do tipo int com valor 17 e y uma variável float com valor 3.2, calcule o
#valor das seguintes expressões em python:
#a) x / 4 + y
#b) x * y ** 6
#c) (x % 4) , (((int) y * 10) // 4)
#d) (x / 6 // x / 3) + 4

#declarando as variáveis
x = 17
y = 3.2

#Calculando as equações
a= x / 4 + y 
b= x * y ** 6
c= (x % 4) , ((int(y) * 10) //4)
d= (x / 6 // x / 3) + 4
#Imprimindo os valores
print("O valor de A é: ",a,'\n',"O valor de B é: ",b,'\n',"O valor de C é: ",c,'\n',"O valor de D é: ",d,)

#/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/

#Tarefa 8: Considere a fórmula S = n*(a1 + an)/2. É a soma de termos de uma PA. Faça um programa onde o usuário deva entrar com o número
#de termos (n), valor inicial (a1) e valor final (an). O resultado da soma deve ser mostrado na tela.

#declaração de variáveis
n= float(input('Entre com o número de termos: \n'))
i= float(input('Entre com o valor inicial: \n'))
f= float(input('Entre com o valor final: \n'))

s = n*(i + f)/2

print('O resultado é: ',s)

#/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/

#tarefa 9: Considere a fórmula Sn = a1*(q**n -1) / (q-1). Faça um programa onde o usuário deva entrar com o valor inicial
#(a1), a quantidade de termos (n) e a razão (q). Para nosso exercício a razão deve ser maior ou igual a 2.

#declarando as variáveis
n= float(input('Entre com a quantidade de termos: '))
i= float(input('Entre com o valor inicial: '))
q= float(input('Entre com a razão: '))
#Sitema booleano para identificar se a razão é maior ou igual a dois
if q >= 2:
    sn = i*(q**n -1) / (q-1)
    print("O resultado é: ",sn)
else:
    print("insira uma razão válida") 

#/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/

#Tarefa 10:Escrva um programa para ler o ano de nascimento de uma pessoa e escrever uma mensagem que diga
#se ela poderá ou não votar este ano (não é necessário considerar o mês em que ela nasceu).   

#Declarando variável
ano = int(input("Digite seu ano de nascimento: "))

#Sistema booleano para descobrir se a pessoa pode votar ou não
if ano <= 2007:
    print("Este ano você pode votar")
else:
    print("Você ainda é muito jovem para votar")    

#/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/

#Tarefa 11: Escreva um programa que verifique a validade de uma senha fornecida pelo usuário. A senha
#válida é o número 8765. Devem ser impressas as  seguintes mensagens:
#ACESSO PERMITIDO caso a senha seja válida. ACESSO NEGADO caso a senha seja inválida. 

#declaração de variável
senha = int(input("Digite sua senha: "))   
#Sistema booleano para descobrir se a senha digitada está correta
if senha == 8765:
    print('ACESSO PERMITIDO.')

else:
    print('ACESSO NEGADO.')

#/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/

#Tarefa 12: Tendo como entrada a altura e o sexo (codificado da seguinte forma:
#1:feminino 2:masculino) de uma pessoa, construa um programa que calcule e imprima seu peso ideal, utilizando as seguintes
#Fórmulas: - para homens: (72.7 * Altura) – 58 - para mulheres: (62.1 * Altura) – 44.7

s= int(input('Informe o seu sexo: \n 1 - Feminino \n 2 - Masculino \n' ))

if s == 1:
    altura= float(input('Informe sua altura: '))
    f= (62.1 * altura) - 44.7
    print('Seu peso ideal é aproximadamente:', f)

elif s == 2:
    altura= float(input('Informe sua altura: '))
    m= (72.7 * altura) - 58
    print('Seu peso ideal é aproximadamente:', m)

else:
    print('ERRO, DIGITE UM VALOR VÁLIDO')

#/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/

#Tarefa 13 e 14: Escreva um programa para ler o número de lados de um polígono regular. Calcular e imprimir oseguinte:
#− Se o número de lados for igual a 3 escrever TRIÂNGULO e o valor da área
#− Se o número de lados for igual a 4 escrever QUADRADO e o valor da sua área.
#− Se o número de lados for igual a 5 escrever PENTÁGONO.
#- Acrescente as seguintes mensagens à solução doexercício anterior conforme o caso.
#− Caso o número de lados seja inferior a 3 escrever NÃO É UM POLÍGONO.
#− Caso o número de lados seja superior a 5 escrever POLÍGONO NÃO IDENTIFICADO

#Declaração de variáveis
p= int(input('Quantos ladoso seu poligono possui?'))

if p < 3:
    print("Não é um poligono!.")

elif p == 3:
    print("O poligono é um triangulo (A = b*h/2)")
    b= float(input('Entre com o valor da base'))
    h= float(input('Entre com o valor da altura'))
    a= b * h / 2
    print('A área do triangulo vale: ',a )
    

elif p == 4:
    print("O poligono é um quadrado (A= a **2)")
    lado= float(input("Entre com o valor do lado" ))
    a = lado ** 2
    print("The square area is:",a)


elif p == 5:
    print("O poligono é um pentagono (A= p * a/2)")
    pe = float(input("Entre com o valor do perimetro: "))
    ap= float(input("Entre com o valor da apótema: "))
    a = p * ap / 2 
    print("The pentagon area is:", a)


else:
    print("Poligono não identificado")