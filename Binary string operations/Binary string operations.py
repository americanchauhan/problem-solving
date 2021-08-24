def OperationsBinaryString(str):
    a = int(str[0])
    i = 1

    # i started from index 1 and increment to += 2 to skip 1 index
    while i < len(str):

        #if A apply & operation
        if str[i] == 'A':
            a &= int(str[i+1])

        #if B apply | (or) operation
        elif str[i] == 'B':
            a |= int(str[i+1])

        #otherwise apply Xor (^) operation
        else:
            a ^= int(str[i + 1])
        i += 2
    
    #final output is stored in a, so return a
    return a

#Binary input
str = input()       
print(OperationsBinaryString(str))