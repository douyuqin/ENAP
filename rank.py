import GAmedcomputing
import copy


MUL8LIP=['mul8u_Y48','mul8u_2P7','mul8u_KEM','mul8u_150Q','mul8u_CK5']
MUL8LIP_area=[390,386,370,360,345]
ADD16LIP=['add16u_0RN','add16u_0EM','add16u_1JH','add16u_073','add16u_0M0']
ADD16LIP_area=[60,57,51,43,36]


Area_ADD16JINQUE = 72
Area_MUL8JINQUE = 391

paixuMUL = []
paixuaddloa = []
paixuADD = []
paixumulloa = []
PaixuResult = []
paixuadd = 0
paixumul = 0
sum = 0
zhongjian = 0


def rank(_list, _list2, N):
    paixuadd = 0
    paixumul = 0
    for i in range(0, N):
        _listpaixu = copy.deepcopy(_list)
        PX = _listpaixu[i]
        if (PX['functions']['function'] == 'add'):
            PX['functions']['function'] = ADD16LIP[1]
            MED = GAmedcomputing.GAerror1(_listpaixu)
            paixuADD.append(MED)
            paixuaddloa.append(i)
            paixuadd = paixuadd + 1
        if (PX['functions']['function'] == 'mul'):
            PX['functions']['function'] = MUL8LIP[1]
            MED = GAmedcomputing.GAerror1(_listpaixu)
            paixuMUL.append(MED)
            paixumulloa.append(i)
            paixumul = paixumul + 1
    if paixuadd > 1:
        for j in range(0, paixuadd):
            for i in range(1, paixuadd):
                if (paixuADD[i] >= paixuADD[i - 1]):
                    zhongjian = paixuADD[i]
                    paixuADD[i] = paixuADD[i - 1]
                    paixuADD[i - 1] = zhongjian
                    zhongjian = paixuaddloa[i]
                    paixuaddloa[i] = paixuaddloa[i - 1]
                    paixuaddloa[i - 1] = zhongjian
    if paixumul > 1:
        for j in range(0, paixumul):
            for i in range(1, paixumul):
                if (paixuMUL[i] >= paixuMUL[i - 1]):
                    zhongjian = paixuMUL[i]
                    paixuMUL[i] = paixuMUL[i - 1]
                    paixuMUL[i - 1] = zhongjian
                    zhongjian = paixumulloa[i]
                    paixumulloa[i] = paixumulloa[i - 1]
                    paixumulloa[i - 1] = zhongjian
    PaixuResult.append(paixuADD)
    PaixuResult.append(paixuaddloa)
    PaixuResult.append(paixuMUL)
    PaixuResult.append(paixumulloa)

    return PaixuResult
