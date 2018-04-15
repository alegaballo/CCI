# given a string, check if it is a permutation of a palindrome (not just dictionary words)

def pal_perm(string):
    cnt={}
    string = string.lower() 
    for c in string:
        if c=='':
            continue

        if c in cnt:
            cnt[c]+=1
        else:
            cnt[c]=1
    print(cnt)
    odds=0
    for k in cnt:
        if cnt[k]%2==1:
            odds+=1
            if odds>1:
                return -1
    return 1


def main():
    string='tact  coa'
    print(pal_perm(string))


if __name__=="__main__":
    main()
