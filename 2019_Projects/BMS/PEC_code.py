
# coding: utf-8

# In[ ]:




while(1):
    try:
        myHex=(input('type in hex. ie c304')).replace(" ", "")
        myBin=bin(int(myHex, 16))[2:]
        data=[]
        for i in range(len(myBin)):
            data.append(int(myBin[i]))

        pec = [0,0,0,0,0,0,0,0,0,0,1,0,0,0,0]#15 bit
        #data = [0,0,0,0,0,0,1,1,0,1,1,1,0,0,0,0]#16bit
        in14=0
        in10=0
        in8=0
        in7=0
        in4=0
        in3=0
        in0=0
        a=len(pec)-1
        for i in range(len(data)):

            in0 = data[i]^pec[a-14]
            in3 = in0^pec[a-2]
            in4 = in0^pec[a-3]
            in7 = in0^pec[a-6]
            in8 = in0^pec[a-7]
            in10 = in0^pec[a-9]
            in14 = in0^pec[a-13]
            pec[a-14] = in14
            pec[a-13] = pec[a-12]
            pec[a-12] = pec[a-11]
            pec[a-11] = pec[a-10]
            pec[a-10] = in10
            pec[a-9] = pec[a-8]
            pec[a-8] = in8
            pec[a-7] = in7
            pec[a-6] = pec[a-5]
            pec[a-5] = pec[a-4]
            pec[a-4] = in4
            pec[a-3] = in3
            pec[a-2] = pec[a-1]
            pec[a-1] = pec[a-0]
            pec[a-0] = in0


        pec=pec+[0]
        temp=''.join(str(x) for x in pec)
        print ("binary is: "+temp)
        print("hex is: " + hex(int(temp, 2)))
    except:
        pass
