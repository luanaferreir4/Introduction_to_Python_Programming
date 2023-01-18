# 12) Escreva um algoritmo que leia o número de identificação, as 3 notas obtidas por um aluno nas
# 3 verificações e a média dos exercícios que fazem parte da avaliação, e calcule a média de
# aproveitamento, usando a fórmula:
# MA := (nota1 + nota 2 * 2 + nota 3 * 3 + ME)/7
# A atribuição dos conceitos obedece a tabela abaixo. O algoritmo deve escrever o número do aluno,
# suas notas, a média dos exercícios, a média de aproveitamento, o conceito correspondente e a
# mensagem 'Aprovado' se o conceito for A, B ou C, e 'Reprovado' se o conceito for D ou E.
# Média de aproveitamento Conceito
# >= 90 A
# >= 75 e < 90 B
# >= 60 e < 75 C
# >= 40 e < 60 D
# < 40 E


num_identificacao = int(input('Número de identificação: '))
nota1, nota2, nota3 = float(input('Nota 1: ')), float(input('Nota 2: ')), float(input('Nota 3: '))
media_exercicios = float(input('Média dos exercícios: '))

media_aproveitamento = (nota1 + nota2*2 + nota3*3 + media_exercicios) / 7

if media_aproveitamento < 40:
    result = 'Aluno {},\nNota 1: {}, Nota 2: {}, Nota 3: {}\nMédia dos exercícios: {}\nMédia de aproveitamento: {}' \
             '- E - REPROVADO'.format(num_identificacao, nota1, nota2, nota3, media_exercicios, media_aproveitamento)
elif media_aproveitamento < 60:
    result = 'Aluno {},\nNota 1: {}, Nota 2: {}, Nota 3: {}\nMédia dos exercícios: {}\nMédia de aproveitamento: {}' \
             '- D - REPROVADO'.format(num_identificacao, nota1, nota2, nota3, media_exercicios, media_aproveitamento)
elif media_aproveitamento < 75:
    result = 'Aluno {},\nNota 1: {}, Nota 2: {}, Nota 3: {}\nMédia dos exercícios: {}\nMédia de aproveitamento: {}' \
             '- C - APROVADO'.format(num_identificacao, nota1, nota2, nota3, media_exercicios, media_aproveitamento)
elif media_aproveitamento < 90:
    result = 'Aluno {},\nNota 1: {}, Nota 2: {}, Nota 3: {}\nMédia dos exercícios: {}\nMédia de aproveitamento: {}' \
             '- B - APROVADO'.format(num_identificacao, nota1, nota2, nota3, media_exercicios, media_aproveitamento)
else:
    result = 'Aluno {},\nNota 1: {}, Nota 2: {}, Nota 3: {}\nMédia dos exercícios: {}\nMédia de aproveitamento: {}' \
             '- A - APROVADO'.format(num_identificacao, nota1, nota2, nota3, media_exercicios, media_aproveitamento)

print(result)