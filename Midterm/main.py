def isPana(s):
    for i in range(len(s)):
        for j in range(i, s.len):
            if s[j] == s[i]:
                return False
    return True


n = int(input())

string = input()
letter = ""

if string.islower():
    if isPana(string):
        print("YES")
    else:
        print("NO")
else:
    check = False
    for character in string:
        letter += character
        if letter.isupper() and check == False:
            continue
        elif letter.isupper() and check == True:
            if isPana(letter) == False:
                print("NO")
                break
        
    print("YES")
            





    
    