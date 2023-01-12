import GAmedcomputing

MUL8LIP=['mul8u_Y48','mul8u_2P7','mul8u_KEM','mul8u_150Q','mul8u_CK5']
MUL8LIP_area=[390,386,370,360,345]
ADD16LIP=['add16u_0RN','add16u_0EM','add16u_1JH','add16u_073','add16u_0M0']
ADD16LIP_area=[60,57,51,43,36]
Area_ADD16JINQUE=72
Area_MUL8JINQUE=391

def Downlimit(areagain,_list5,N,_list2,_list4,AR,ERR):
    areazhongjian=[0 for i in range(N)]
    Numadd= 0
    Nummul= 0
    freemul=0
    freeadd=0
    for i in range(0,N):
         obj = _list4[i]
         if obj['functions']['function'] == 'add':
             Numadd = Numadd + 1
         if obj['functions']['function'] == 'mul':
             Nummul = Nummul + 1

    for i in range(0,N):
        obj = _list4[i]
        mulloaction = 0
        if obj['functions']['function'] == 'mul':
            mulloaction = i
            freemul=0
            break
        else:freemul=1
        t=0
    for i in range(0, N):
        obj = _list4[i]
        addloaction = 0
        if obj['functions']['function'] == 'add':
            addloaction = i
            freeadd=0
            break
        else:freeadd=1
        t1=0
   #Determine the range of multiplier
    if freemul==0:
        for t in range(4, 0,-1):
            obj1 = _list4[mulloaction]
            obj1['functions']['function'] = MUL8LIP[t]
            MED = GAmedcomputing.GAerror1(_list4)
            if MED <ERR:
                break
    #Determine the range of the adder
    if freeadd == 0:
        for t1 in range(4, 0,-1):
            obj1 = _list4[addloaction]
            # print(addloaction)
            obj1['functions']['function'] = ADD16LIP[t1]
            MED = GAmedcomputing.GAerror1(_list4)
            for i in range(0,N):
                obj1 = _list4[i]
            if MED <ERR:
                break
    # Lower estimate limit
    sign = 0
    sumAC = 0
    summul = 0
    tt=0
    # for i in range(0,Nummul):
    if freemul == 0:
        for tt in range(0,Nummul):
            summul=summul+(Area_MUL8JINQUE-MUL8LIP_area[t])
            if summul > areagain:
                sumAC = tt+1
                sign = 1
                break
    sumadd=0
    sumAC1 = 0
    tt1=0
    if freeadd == 0:
        if sign==0:
            sumAC=Nummul
            sumadd = summul
            for tt1 in range(0, Numadd):
                sumadd = sumadd + (Area_ADD16JINQUE - ADD16LIP_area[t1])
                if sumadd > areagain:
                    sumAC1 = tt1+1
                    # print('4444',sumAC1)
                    sign = 1
                    break


    downresult = [0,0,0,0,0]
    downresult[0] = sumAC+sumAC1
    if sign==0:
        downresult[0]=Nummul+Numadd
    downresult[1] = summul
    downresult[2] = sumadd+summul
    downresult[3] = t
    downresult[4] = t1
    return downresult

