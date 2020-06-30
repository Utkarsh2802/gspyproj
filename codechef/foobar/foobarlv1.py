string = input()
ans=""
for i in string:
    if 97<=ord(i)<=122:
        before_reverse=ord(i)
        ans+=chr(25-(before_reverse-97)+97)
    else:
        ans+=i
print(ans)