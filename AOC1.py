#todo count the number of times a depth measurement increases from the previous measurement. (There is no measurement before the first measurement.)
depthfile = open('sonar.txt','r')
depths = depthfile.read().splitlines()
depthlist = [ int(x) for x in depths ]



# depthlist = depths.split("\n")
# depthlist = depths
def partone():
    increase = 0

    prev = depthlist[0]
    for i in depthlist[1:]:
        if i > prev:
            increase += 1
        prev = i
    return increase





#sum numbers before and after current number
#compare to previous sum unless its the first sum
increase = 0
iter = 1
for i in depthlist[1:(len(depthlist) - 1)]:
    window = depthlist[iter-1] + i + depthlist[iter+1]
    try:
        if window > prevwindow:
            increase += 1
    except:
        print('skip first compare')
    prevwindow = window
    print(window)
    iter +=1
print(increase)
print('part one: ' + str(partone()))
# if True:
#     partone()