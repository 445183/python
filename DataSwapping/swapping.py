def swapData():
    r1=open("text1.txt",'r')
    r2=open("text2.txt",'r')

    dataVal1=r1.read()
    dataVal2=r2.read()

    print(dataVal2)
    print(dataVal1)

    w1=open("text1.txt",'w')
    w2=open("text2.txt",'w')

    w1.write(dataVal2)
    w2.write(dataVal1)

swapData()