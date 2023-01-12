import random
import copy
import numpy as np
def mut(_list,_list2,downresult,randoms1,randoms2,z,upresult,paixuMED):
    ww = []
    ww1 = []
    for i in range(0, z):
        levelmul = [i for i in range(0, downresult[3] + 1)]
        leveladd = [i for i in range(0, downresult[4] + 1)]
        a1 = random.randint(0, len(randoms1) - 1)
        b1 = random.randint(0, len(randoms1[a1]) - 1)
        c1 = random.randint(0, len(randoms1[a1][b1]) - 1)
        jieoajie1 = copy.deepcopy(randoms1[a1][b1])
        jieoajie11 = copy.deepcopy(randoms2[a1][b1])


        zhongjian = []
        if downresult[0] < len(jieoajie1) < upresult[1]:

            a3 = random.randint(0, 1)
            if a3 == 0:

                a2 = random.randint(0, 1)
                if a2 == 0:
                    zhongjian = copy.deepcopy(paixuMED[3])
                    for i in range(0, len(jieoajie1)):
                        zhongjian.remove(jieoajie1[i])
                    aa = random.choice(zhongjian)

                    if aa in paixuMED[1]:
                        ff = random.choice(levelmul)
                    else:
                        ff = random.choice(leveladd)
                    jieoajie1.append(aa)
                    jieoajie11.append(ff)
                else:
                    aa = random.choice(jieoajie1)
                    cc = jieoajie1.index(aa)
                    jieoajie1.remove(aa)
                    jieoajie11.remove(jieoajie11[cc])
            else:
                a4 = random.randint(0, 1)
                if a4 == 0:
                    if jieoajie1[c1] in paixuMED[1]:
                        if 0 <= jieoajie11[c1] < downresult[3]:
                            jieoajie11[c1] = jieoajie11[c1] + 1
                        if jieoajie11[c1] == downresult[3]:
                            jieoajie11[c1] = jieoajie11[c1] - 1
                    else:
                        if 0 <= jieoajie11[c1] < downresult[4]:
                            jieoajie11[c1] = jieoajie11[c1] + 1
                        if jieoajie11[c1] == downresult[4]:
                            jieoajie11[c1] = jieoajie11[c1] - 1

                else:
                    if jieoajie1[c1] in paixuMED[1]:
                        if 0 < jieoajie11[c1] <= downresult[3]:
                            jieoajie11[c1] = jieoajie11[c1] - 1
                        if jieoajie11[c1] == 0:
                            jieoajie11[c1] = jieoajie11[c1] + 1
                    else:
                        if 0 < jieoajie11[c1] <= downresult[4]:
                            jieoajie11[c1] = jieoajie11[c1] - 1
                        if jieoajie11[c1] == 0:
                            jieoajie11[c1] = jieoajie11[c1] + 1
        ww.append(jieoajie1)
        ww1.append(jieoajie11)
    randoms1.append(ww)
    randoms2.append(ww1)
    return randoms1,randoms2


def mut1(_list,_list2,downresult,randoms1,randoms2,z,upresult,paixuMED):
    ww = []
    ww1 = []
    for i in range(0, z):
        levelmul = [i for i in range(0, downresult[3] + 1)]
        leveladd = [i for i in range(0, downresult[4] + 1)]
        a1 = random.randint(0, len(randoms1) - 1)
        b1 = random.randint(0, len(randoms1[a1]) - 1)
        # c1 = random.randint(0, len(randoms1[a1][b1]) - 1)
        jieoajie1 = copy.deepcopy(randoms1[a1])
        jieoajie11 = copy.deepcopy(randoms2[a1])

        # 数量突变
        zhongjian = []
        if downresult[0] < len(jieoajie1) < upresult[1]:

            a3 = random.randint(0, 1)
            if a3 == 0:

                a2 = random.randint(0, 1)
                if a2 == 0:
                    zhongjian = copy.deepcopy(paixuMED[3])
                    for i in range(0, len(jieoajie1)):
                        zhongjian.remove(jieoajie1[i])
                    aa = random.choice(zhongjian)

                    if aa in paixuMED[1]:
                        ff = random.choice(levelmul)
                    else:
                        ff = random.choice(leveladd)
                    jieoajie1.append(aa)
                    jieoajie11.append(ff)
                else:
                    aa = random.choice(jieoajie1)
                    cc = jieoajie1.index(aa)
                    jieoajie1.remove(aa)
                    jieoajie11.remove(jieoajie11[cc])
            else:
                a4 = random.randint(0, 1)
                if a4 == 0:
                    if jieoajie1[b1] in paixuMED[1]:
                        if 0 <= jieoajie11[b1] < downresult[3]:
                            jieoajie11[b1] = jieoajie11[b1] + 1
                        if jieoajie11[b1] == downresult[3]:
                            jieoajie11[b1] = jieoajie11[b1] - 1
                    else:
                        if 0 <= jieoajie11[b1] < downresult[4]:
                            jieoajie11[b1] = jieoajie11[b1] + 1
                        if jieoajie11[b1] == downresult[4]:
                            jieoajie11[b1] = jieoajie11[b1] - 1

                else:
                    if jieoajie1[b1] in paixuMED[1]:
                        if 0 < jieoajie11[b1] <= downresult[3]:
                            jieoajie11[b1] = jieoajie11[b1] - 1
                        if jieoajie11[b1] == 0:
                            jieoajie11[b1] = jieoajie11[b1] + 1
                    else:
                        if 0 < jieoajie11[b1] <= downresult[4]:
                            jieoajie11[b1] = jieoajie11[b1] - 1
                        if jieoajie11[b1] == 0:
                            jieoajie11[b1] = jieoajie11[b1] + 1
        randoms1.append(jieoajie1)
        randoms2.append(jieoajie11)
    return randoms1,randoms2