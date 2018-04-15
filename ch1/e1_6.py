# implement a method to perform basic string compression using the count of repeated characters
# aabcccccaaa -> a2b1c5a3

def string_compression(string):
    compressed = []
    cnt = 1
    char = string[0]

    for i in string[1:]:
        if i==char:
            cnt += 1
        else:
            compressed.append(char+str(cnt))
            cnt = 1
            char = i
    compressed.append(char+str(cnt))
    new = ''.join(compressed)
    
    return min([new, string], key=len)

# alternative: compute the compressed string length before actually creating it

def main():
    string = 'aabcccccaaa'
    string = 'abcde'
    print(string_compression(string))



if __name__=='__main__':
    main()
