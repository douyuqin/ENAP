import random
import numpy as np
import copy
# import errorcomputing
import applications.laplacecomputing
import applications.dctcomputing
import applications.convcomputing
import applications.fircomputing
import applications.sharpencomputing
from applications import laplacecomputing

ADD8LIP=['add8u_5R3','add8u_5SY','add8u_006','add8u_8ES']
ADD8LIP_area=[63.8,28.2,15,8]
MUL8LIP=['mul8u_Y48','mul8u_2P7','mul8u_KEM','mul8u_150Q']
MUL8LIP_area=[390,386,370,360]
ADD16LIP=['add16u_0RN','add16u_0EM','add16u_1JH','add16u_073']
ADD16LIP_area=[60,57,51,43]
Arealank=['mul8u_Y48','add16u_0EM','mul8u_150Q','add16u_073','add16u_00G','add16u_02E','mul8u_185Q','mul8u_13QR']
Area_ADD16JINQUE=72
Area_MUL8JINQUE=391
def GAerror(_list2,PEIZHI1,PEIZHI2,N):
    zhongjianlist = copy.deepcopy(_list2)
    for i in range(0, len(PEIZHI1)):
        if PEIZHI2[i]>=4:
            PEIZHI2[i]=3
        obj = zhongjianlist[PEIZHI1[i]]
        if (obj['functions']['function'] == 'add'):
            obj['functions']['function'] = ADD16LIP[PEIZHI2[i]]
        if (obj['functions']['function'] == 'mul'):
            # print('jisuanleixing',PEIZHI2[i])
            obj['functions']['function'] = MUL8LIP[PEIZHI2[i]]
    MED = laplacecomputing.laplseerrorcomputing(zhongjianlist)
    return MED

def GAerror1(_list):
    MED = laplacecomputing.laplseerrorcomputing(_list)
    return MED