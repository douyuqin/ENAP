import time

import GAmedcomputing
import copy
import random
import rank


MUL8LIP=['mul8u_Y48','mul8u_2P7','mul8u_KEM','mul8u_150Q','mul8u_CK5']
MUL8LIP_area=[390,386,370,360,345]
ADD16LIP=['add16u_0RN','add16u_0EM','add16u_1JH','add16u_073','add16u_0M0']
ADD16LIP_area=[60,57,51,43,36]

Area_ADD16JINQUE=72
Area_MUL8JINQUE=391



# 判断是否超过错误需求
def Upperlimit(_list,_list2,N,area,ERR):
    paixu = rank.rank(_list, _list2, N)  # 排序用于确定节点对于错误的敏感性
    paixu[3].extend(paixu[1])
    ER = 1
    for i in range(0,N):
        obj = _list[i]
        if obj['functions']['function'] == 'add':
            obj['functions']['function']='add16u_0RN'
        if obj['functions']['function'] == 'mul':
            obj['functions']['function']='mul8u_Y48'
    MED = GAmedcomputing.GAerror1(_list)
    # print(MED,ERR)
    if MED<=ERR:
        for t in range(1,5):
            if ER==1:
             for i in range(0,len(paixu[3])):
                    obj = _list[paixu[3][i]]
                    previouslist= copy.deepcopy(_list)
                    if (obj['functions']['function'] == 'add')|(obj['functions']['function']==ADD16LIP[t-1]):
                        obj['functions']['function'] = ADD16LIP[t]
                        previousarea=copy.deepcopy(area)
                        area[paixu[3][i]] = ADD16LIP_area[t]
                        MED = GAmedcomputing.GAerror1(_list)
                        if MED > ERR:
                            ER=2
                            break
                    previouslist = copy.deepcopy(_list)
                    if (obj['functions']['function'] == 'mul8u_Y48')|(obj['functions']['function'] == MUL8LIP[t-1]):
                        obj['functions']['function'] = MUL8LIP[t]
                        previousarea = copy.deepcopy(area)
                        area[paixu[3][i]] = MUL8LIP_area[t]
                        MED = GAmedcomputing.GAerror1(_list)
                        if MED > ERR:
                            ER = 2
                            # print(MED)
                            break
    if ER==1:
        if MED>ERR:
            for i in range(len(paixu[3])-1, 0,-1):
                # print(paixu[3][i])
                obj = _list[paixu[3][i]]

                if obj['functions']['function'] == 'add16u_0RN':
                    obj['functions']['function'] = 'add'
                    previousarea = copy.deepcopy(area)
                    area[paixu[3][i]] = 72
                    MED = GAmedcomputing.GAerror1(_list)
                    # print(MED)
                    if MED < ERR:
                        previouslist = copy.deepcopy(_list)
                        ER = 2
                        break

                if obj['functions']['function'] == 'mul8u_Y48':
                    obj['functions']['function'] = 'mul'
                    previousarea = copy.deepcopy(area)
                    area[paixu[3][i]] = 391
                    MED = GAmedcomputing.GAerror1(_list)
                    print(MED)
                    if MED < ERR:
                        previouslist = copy.deepcopy(_list)
                        ER = 2
                        # print(MED)
                        break

    sumarea=0
    sumAC=0
    upresult=[0,0]
    for i in range(0,N):
        sumarea=sumarea+previousarea[i]
    for i in range(0,N):
        obj1 = previouslist[i]
        obj2 = _list2[i]
        if obj1['functions']['function']!= obj2['functions']['function']:
            sumAC=sumAC+1

    upresult[0] = sumarea
    upresult[1] = sumAC
    upresult.append(previousarea)
    return upresult,paixu
