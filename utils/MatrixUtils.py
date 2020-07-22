def transpose(matrix):
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix))]


def extract_diagonal(matrix, k, upper, reverse=False):
    """
    Extract the diagonal of a square matrix
    :param matrix: the matrix on which to extract the diagonal
    :param k: the diagonal to extract (0 is the middle diagonal)
    :param upper: if true extract the upper side of the matrix, otherwise the lower side
    :return: the diagonal
    """
    diagonal = []
    matrix_length = len(matrix)

    for i in range(0, matrix_length - k):
        if not reverse:
            if upper:
                diagonal.insert(i, matrix[i][i + k])
            else:
                diagonal.insert(i, matrix[i + k][i])
        else:
            if upper:
                diagonal.insert(i, matrix[matrix_length - 1 - i][i + k])
            else:
                diagonal.insert(i, matrix[matrix_length - 1 - k - i][i])

    return diagonal
