def swap_case(s):
    word=[]
    for i in s:
        if i.isupper():
            i=i.lower()
        elif i.islower():
            i=i.upper()
        word.append(i)
    return "".join(word)

