file = open('diagnostics.txt','r')
content = file.read().splitlines()
diagbin = [ str(x) for x in content  ]

# print(diagbin)
bin1= 0
gamma = ''

for i in range(11):
    for x in range(len(diagbin)):
        line = str(diagbin[x])
        if line[i] == '1':
            bin1 += 1
    if bin1 > 1000:
        gamma = gamma + '1'
    else:
        gamma = gamma + '0'

print(gamma)


#511 wrong