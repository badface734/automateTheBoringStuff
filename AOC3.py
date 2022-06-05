file = open('diagnostics.txt','r')
content = file.read().splitlines()
diagbin = [ str(x) for x in content  ]

# print(diagbin)
bin0 = 0
bin1 = 0
gamma = ''
delta = ''

for i in range(len(diagbin[1])):
    for x in range(len(diagbin)):
        line = str(diagbin[x])
        if line[i] == '1':
            bin1 += 1
        else:
            bin0 += 1

    if bin1 > bin0:
        gamma = gamma + '1'
        delta = delta + '0'
    else:
        gamma = gamma + '0'
        delta = delta + '1'
    bin1 = 0
    bin0 = 0
print(len(diagbin))
print(gamma)
print(delta)


#511 wrong