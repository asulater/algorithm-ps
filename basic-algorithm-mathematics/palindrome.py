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
    if s.isalpha():
        while s:
            for i in range(0, len(s) - 1):
                if s[i] != s[-1]:
                    return False
        return True

print(palindrome_s("Wow"))