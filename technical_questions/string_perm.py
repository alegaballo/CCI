# cracking the coding interview, optimize&solve#4
# recursively compute all permutations of a string
def string_perm(string):
    if len(string)==1:
        return [string]
    
    base = string_perm(string[:-1])
    l=[] # list of permutations
    next_char = string[-1]
    for b in base: 
        for i in range(len(b)+1):
            l.append(b[0:i] + next_char + b[i:])
    return l


def main():
    test='ciao'
    permutations = string_perm(test)
    print(permutations)


if __name__== '__main__':
    main()
