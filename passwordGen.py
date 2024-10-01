import random
alph_count,num_count,spchr_count = 0,0,0
alphabets = ['a','b','c','d','e','f','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','Q','W','E','R','T','Y','U','I','O','P','A','S','D','F','H','J','K','L','Z','X','C','V','B','N','M']
numbers = ['1','2','3','4','5','6','7','8','9','0']
special_char = ['@','_','!','~','^','#','-','.','|']
options = [alphabets,numbers,special_char]
password = []
n = int(input("Enter the length of password:"))
ques = str(input("Want to customize password?(Y/N):")).lower()
def checkCount():
    if alph_count == x:
        if num_count == y:
            new_opt = [special_char]
        elif spchr_count == z:
            new_opt = [numbers]
        else:
            new_opt = [numbers, special_char]
    elif num_count == y:
        if alph_count == x:
            new_opt = [special_char]
        elif spchr_count == z:
            new_opt = [alphabets]
        else:
            new_opt = [alphabets, special_char]
    elif spchr_count == z:
        if alph_count == x:
            new_opt = [numbers]
        elif num_count == y:
            new_opt = [alphabets]
        else:
            new_opt = [alphabets, numbers]
    else:
        new_opt = [alphabets, numbers, special_char]
    return  new_opt
if ques == "y" or ques == "yes":
    x = int(input("Enter the number of letters in password:"))
    y = int(input("Enter the number of numeric values in password:"))
    z = int(input("Enter the number of special character password:"))
    if x+y+z == n:
        for i in range(n):
            l = checkCount()
            a = random.choice(l)
            if a == alphabets:
                alph_count += 1
            elif a == numbers:
                num_count +=1
            else:
                spchr_count +=1
            b = random.choice(a)
            password.append(b)
    else:
        print("!!!Length Of Password dont match with description!!!")
    for k in password:
        print(k,end="")
elif ques == "n" or ques == "no":
    for i in range(n):
        a = random.choice(options)
        b = random.choice(a)
        password.append(b)
        for k in password:
            print(k, end="")
        password.clear()
else:
    print("!!!Enter valid answer!!!")
