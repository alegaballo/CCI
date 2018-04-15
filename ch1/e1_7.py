def rotate(matrix):
    new = [[] for i in range(len(matrix))]

    for i in reversed(range(len(matrix))):
        row = matrix[i]
        for j,elem in enumerate(row):
            new[j].append(elem)

    return new


# following solution,  in place rotation
def rotate_sol(matrix):
    for layer in range(len(matrix)/2):
        last = len(matrix)-layer -1
        for i in range(layer,last):
            top = matrix[layer][i]
            offset = i - layer

            # left -> top 
            matrix[layer][i]=matrix[last-offset][layer]
            # bottom -> left 
            matrix[last-offset][layer]=matrix[last][last-offset]
            # right -> bottom 
            matrix[last][last-offset]=matrix[i][last]
            # top -> right
            matrix[i][last]=top
    return matrix

def print_matrix(matrix):
    for row in matrix:
        for elem in row:
            print '{:3d}'.format(elem),
        print


def main():
    mx = [[1,2,3,4], [5,6,7,8], [9,10,11,12],[13,14,15,16]]
    print_matrix(mx)
    print "Rotated matrix:"
    print_matrix(rotate_sol(mx))



if __name__=='__main__':
    main()
            
