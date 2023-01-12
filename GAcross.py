import random
import copy
import numpy as np

def cross(_list,_list2,downresult,randoms1,randoms2,z,upresult):

    for i in range(0, z):
        a1 = random.randint(0, len(randoms1) - 1)
        b1 = random.randint(0, len(randoms1[a1]) - 1)
        a2 = random.randint(0, len(randoms1) - 1)
        b2 = random.randint(0, len(randoms1[a2]) - 1)

        jieoajie1 = copy.deepcopy(randoms1[a1])
        jieoajie11 = copy.deepcopy(randoms2[a1])
        jieoajie2 = copy.deepcopy(randoms1[a2])
        jieoajie22 = copy.deepcopy(randoms2[a2])

        if len(jieoajie1) >= len(jieoajie2):
            if jieoajie1[b1] in jieoajie2:
                cc = jieoajie2.index(jieoajie1[b1])
                zz = jieoajie11[cc]
                jieoajie11[b1] = jieoajie22[cc]
                jieoajie22[cc] = zz
            else:
                jieoajie2.append(jieoajie1[b1])
                jieoajie22.append(jieoajie11[b1])
                zhongjianqq=copy.deepcopy(jieoajie1)
                jieoajie1.remove(jieoajie1[b1])
                jieoajie11.remove(jieoajie11[b1])
                if len(jieoajie2) > upresult[1]:
                    for r in range(0, len(jieoajie2) - 1):
                        c2=r
                        if (~(jieoajie2[c2] in jieoajie1)) & (jieoajie2[c2] != zhongjianqq[b1]):
                            jieoajie2.remove(jieoajie2[c2])
                            jieoajie22.remove(jieoajie22[c2])
                            break
                    jieoajie1.append(jieoajie2[c2])
                    jieoajie11.append(jieoajie22[c2])
                if len(jieoajie1) < downresult[0]:
                    for r in range(0, len(jieoajie2) - 1):
                        c2 = r
                        if (~(jieoajie2[c2] in jieoajie1)) & (jieoajie2[c2] != zhongjianqq[b1]):
                            break
                    jieoajie1.append(jieoajie2[c2])
                    jieoajie11.append(jieoajie22[c2])
            if jieoajie1 is not None:
                randoms1.append(jieoajie1)
                randoms2.append(jieoajie11)
            if jieoajie2 is not None:
                randoms1.append(jieoajie2)
                randoms2.append(jieoajie22)


        if len(jieoajie1) < len(jieoajie2):
            zhongjian1 = jieoajie1
            zhongjian2 = jieoajie11
            jieoajie1 = jieoajie2
            jieoajie11 = jieoajie22
            jieoajie2 = zhongjian1
            jieoajie22 = zhongjian2
            if jieoajie1[b1] in jieoajie2:
                cc = jieoajie2.index(jieoajie1[b1])
                zz = jieoajie11[cc]
                jieoajie11[b1] = jieoajie22[cc]
                jieoajie22[cc] = zz
            else:
                jieoajie2.append(jieoajie1[b1])
                jieoajie22.append(jieoajie11[b1])
                zhongjianqq = copy.deepcopy(jieoajie1)
                jieoajie1.remove(jieoajie1[b1])
                jieoajie11.remove(jieoajie11[b1])
                if len(jieoajie2) > upresult[1]:
                    for r in range(0, len(jieoajie2) - 1):
                        c2 = r
                        if (~(jieoajie2[c2] in jieoajie1)) & (jieoajie2[c2] != zhongjianqq[b1]):
                            jieoajie2.remove(jieoajie2[c2])
                            jieoajie22.remove(jieoajie22[c2])
                            break
                    jieoajie1.append(jieoajie2[c2])
                    jieoajie11.append(jieoajie22[c2])
                if len(jieoajie1) < downresult[0]:
                    for r in range(0, len(jieoajie2) - 1):
                        c2 = r
                        if (~(jieoajie2[c2] in jieoajie1)) & (jieoajie2[c2] != zhongjianqq[b1]):
                            break
                    jieoajie1.append(jieoajie2[c2])
                    jieoajie11.append(jieoajie22[c2])
            if jieoajie1 is not None:
                randoms1.append(jieoajie1)
                randoms2.append(jieoajie11)
            if jieoajie2 is not None:
                randoms1.append(jieoajie2)
                randoms2.append(jieoajie22)


    return randoms1,randoms2