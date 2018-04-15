# write an algorithm such tht if an element in an MxN matrix is 0, its entire row and column are set to 0

def zero_matrix(matrix):

    zero_first_r = False
    zero_first_c = False
    for elem in matrix[0]:
        if elem == 0:
            zero_first_r = True
            break

    for row in matrix:
        if row[0] == 0:
            zero_first_c = True
            break          

    for i, row in enumerate(matrix[1:]):
        for j, elem in enumerate(row[1:]):
            if elem == 0:
                # +1 needed because enumerate starts from 0 
                # but the first rows and columns were already checked
                matrix[0][j+1]=0
                matrix[i+1][0]=0

    # zeroing cols
    for i, el in enumerate(matrix[0]):
        if el == 0:
            zero_col(matrix, i)

    
    # zeroing rows
    for j, el in enumerate(matrix):
        if el[0] == 0:
            zero_row(matrix, j)


    if zero_first_r:
        zero_row(matrix, 0)

    if zero_first_c:
        zero_col(matrix, 0)


def zero_row(matrix, row):
    for i in range(len(matrix[row])):
        matrix[row][i]=0


def zero_col(matrix, col):
    for i in range(len(matrix)):
        matrix[i][col]=0


def main():
    matrix = [[1,0,3], 
              [4,1,5],
              [6,7,0]]
    print(matrix)
    zero_matrix(matrix)
    print(matrix)


if __name__ == "__main__":
    main()
