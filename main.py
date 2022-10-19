from exceptions import WrongMatrix


def find_determinant_of_two_size(matrix: list) -> int:
    return matrix[0][0] * matrix[1][1] - matrix[0][1]*matrix[1][0]


def get_column(matrix: list, column_number: int) -> list:
    result = []
    for line in matrix:
        result.append(line[column_number])
    return result


def calculate_element_of_matrix(list1: list, list2: list) -> int:
    result = 0
    for i in range(len(list1)):
        result += list1[i] * list2[i]
    return result


def multiply_matrix(first_matrix: list, second_matrix: list) -> list:
    if len(matrix1[0]) != len(matrix2):
        raise WrongMatrix
    lines = len(matrix1)
    columns = len(matrix2[0])
    result_matrix = []
    for i in range(lines):
        result_matrix.append([0]*columns)
    for i in range(lines):
        for j in range(columns):
            result_matrix[i][j] = calculate_element_of_matrix(first_matrix[i], get_column(second_matrix, j))
    return result_matrix


def sum_matrix(matrix1, matrix2) -> list:
    if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
        raise WrongMatrix
    lines = len(matrix1)
    columns = len(matrix1[0])
    result_matrix = []
    for i in range(lines):
        result_matrix.append([0]*columns)
    for i in range(len(result_matrix)):
        for j in range(len(result_matrix[i])):
            result_matrix[i][j] = matrix1[i][j] + matrix2[i][j]
    return result_matrix


def find_determinant_of_three_size(matrix: list) -> int:
    if len(matrix) == 3 and len(matrix[0]) == 3:
        return matrix[0][0]*matrix[1][1]*matrix[2][2] + matrix[0][1]*matrix[1][2]*matrix[2][0] + matrix[0][2]*matrix[1][0]*matrix[2][1] - matrix[0][2]*matrix[1][1]*matrix[2][0] - matrix[0][1]*matrix[1][0]*matrix[2][2] - matrix[0][0]*matrix[1][2]*matrix[2][1]
    raise WrongMatrix


if __name__ == '__main__':
    '''Write here your matrix and what to do with them'''
    pass
