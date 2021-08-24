def CheckPassword(s, n):
    #To check if password having atleast 4 characters
    if n<4:             
        return 0
    
    #To check if first character is digit or not
    if s[0].isdigit():      
        return 0
    cap = 0
    nu = 0

    for i in range(n):

        #return 0 if there is any space or slash
        if s[i] == ' ' or s[i] == '/':      
            return 0
        
        #increment to cap if there is any capital letter
        elif s[i] >= 'A' and s[i]<= 'Z':     
            cap += 1
        
        #increment nu if there is atleast 1 digit
        elif s[i].isdigit():        
            nu += 1

    #if there is capital letter and atleast one digit return 1
    if cap > 0 and nu > 0:      
        return 1
    
    #else password criteria is not met
    else:
        return 0            


s = input()
a = len(s)
print(CheckPassword(s, a))