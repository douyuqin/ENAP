import random
import numpy as np
def ini(_list,_list2,downresult,upresult,paixuMED,o):
    randoms1 = []
    randoms2 = []
    for q in range(0, o):
        samplesnode = []
        i=int(random.uniform(downresult[0], upresult[1] + 1))
        gg = random.sample(paixuMED[3], i)
        samplesnode.append(gg)
        randoms1.append(samplesnode)
        randoms1.append(samplesnode)

        sampleslevel = []
        sampleslevel1=[]
        levelmul = [i for i in range(0, downresult[3] + 1)]
        leveladd = [i for i in range(0, downresult[4] + 1)]
        for i in range(0, len(samplesnode)):
            pinjie = []
            pinjie1 = []
            for j in range(0, len(samplesnode[i])):
                if samplesnode[i][j] in paixuMED[1]:
                    ff = random.sample(leveladd, 1)
                    pinjie.append(ff)
                    pinjie1.append(0)
                else:
                    ff = random.sample(levelmul, 1)
                    pinjie.append(ff)
                    pinjie1.append(0)
            # sum(pinjie, [])
            pinjie = list(np.array(pinjie).flatten())
            sampleslevel.append(pinjie)
            sampleslevel1.append(pinjie1)
            # print(sampleslevel)
        # print(sampleslevel)

        randoms2.append(sampleslevel)
        randoms2.append(sampleslevel1)


    return randoms1,randoms2


