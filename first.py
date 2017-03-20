
for j in "Test Case":
    if j=='R':
        #continue
        break
    #print(j*2, end='')
else:
    print('Exit simbol')


lis = [1, 56, 'x', 34, 2.34, ['S', 't', 'r', 'o', 'k', 'a']]
print(lis)

a = [a+b for a in 'list' if a!='s' for b in 'soup' if b!='u']
print(a)

i=0
l=[111,222,333,444]
while i<l.count():
    print(l[i])
    i += 1
