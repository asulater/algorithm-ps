# 14) find palindrome

def palindrome(s):
    qu = [] # queue list
    st = [] # stack list
    
    for x in s:
        if x.isalpha():
            qu.append(x.lower())
            st.append(x.lower())
    while qu:
        if qu.pop(0) != st.pop():
            return False
    return True

print(palindrome("Wow"))
print(palindrome("Madam, I'm Adam."))
print(palindrome("Madam, I am Adam."))



# 14-1) palindrome (not use queue, stack)


def palindrome_s(s):
    i = 0
    j = len(s) - 1
    while i < j:
        if s[i].isalpha() == False:
            i += 1
        elif s[j].isalpha() == False:
            j -= 1
        elif s[i].lower() != s[j].lower():
            return False
        else:
            i += 1
            j -= 1
    return True

print(palindrome_s("Wow"))