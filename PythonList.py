words = open('romeo.txt')
while True:
    for line in words:
        line = line.split()
        romeo = (line)
        romeo.sort()
        print(romeo)
        exit()



