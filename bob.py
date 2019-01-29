count, i = 0, 0
s = "obobobbobbyxao"
while i < len(s)-2:
    if(s[i] == 'b' and s[i+1] == 'o' and s[i+2] == 'b'): count += 1
    i += 1
print(count)
