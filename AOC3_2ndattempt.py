def readfile():
    file = open('diagnostics.txt', 'r')
    content = file.read().splitlines()
    # diagbin = [str(x) for x in content]
    return content

# print(readfile())


content = readfile()
num=0

for i in range(len(content[1])-1):

    for x in range(len(content)):
        bin = content[x]
        num += int(bin[i])
    if num > 500:
        print(num)
        print('over 500')

    num=0



