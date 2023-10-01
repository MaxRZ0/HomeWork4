# Напишите функцию для транспонирования матрицы

user_input = input('Введите матрицу в виде a1,b1...c1/a2,b2...c2/...: ').split('/')

matrix = [idx.split(',') for idx in user_input]

trans_matrix = [[0 for idx1 in range(len(matrix))] for idx2 in range(len(matrix[0]))]
for idx1 in range(len(matrix)):
    for idx2 in range(len(matrix[0])):
        try:
            trans_matrix[idx2][idx1] = matrix[idx1][idx2]
        except:
            exit('Вы ввели несуществующую митрицу')

print(matrix, trans_matrix, sep='\n')
