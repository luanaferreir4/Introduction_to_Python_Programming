# Dados os nomes e as notas de cada aluno em uma classe de N alunos, armazene-os em uma lista aninhada
# e imprima o(s) nome(s) de qualquer aluno(s) com a segunda nota mais baixa.
# Observação: Se houver vários alunos com a segunda nota mais baixa, ordene seus nomes em ordem alfabética
# e imprima cada nome em uma nova linha.

if __name__ == '__main__':
    records = []
    scores = []
    new_max = int
    for _ in range(int(input())):
        list = []
        name = input()
        score = float(input())
        list.append(name)
        list.append(score)
        records.append(list)
        scores.append(score)

    if len(scores) > 1:
        sorted_scores = sorted(scores)
        for j in range(len(sorted_scores)):
            if sorted_scores[j] != sorted_scores[0]:
                new_max = sorted_scores[j]

                second_worst_students = []
                for record in records:
                    if record[1] == new_max:
                        second_worst_students.append(record[0])

                for students in second_worst_students:
                    print(students)


