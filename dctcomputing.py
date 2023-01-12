# import pandas as pd
import math
from ctypes import *
import numpy as np
from decimal import *
import random

import DFGparsing

ADD8LIP=['add8u_5R3','add8u_5SY','add8u_006','add8u_8ES']
ADD8LIP_area=[63.8,28.2,15,8]
MUL8LIP=['mul8u_Y48','mul8u_2P7','mul8u_KEM','mul8u_150Q']
MUL8LIP_area=[390,386,370,360]
ADD16LIP=['add16u_0RN','add16u_0EM','add16u_1JH','add16u_073']
ADD16LIP_area=[60,57,51,43]
# ADD16LIP=['add16u_0EM','add16u_1JH','add16u_073','add16u_0M0']
# ADD16LIP_area=[57,51,43,36]

ADD1 = 0
ADD1 = cdll.LoadLibrary("./approlib/add8u_5R3.so")
ADD2 = 0
ADD2 = cdll.LoadLibrary("./approlib/add8u_5SY.so")
ADD3 = 0
ADD3 = cdll.LoadLibrary("./approlib/add8u_006.so")
ADD4 = 0
ADD4 = cdll.LoadLibrary("./approlib/add8u_8ES.so")
MUL1 = 0
MUL1 = cdll.LoadLibrary("./approlib/mul8u_Y48.so")
MUL2 = 0
MUL2 = cdll.LoadLibrary("./approlib/mul8u_150Q.so")
MUL3 = 0
MUL3 = cdll.LoadLibrary("./approlib/mul8u_185Q.so")
MUL4 = 0
MUL4 = cdll.LoadLibrary("./approlib/mul8u_13QR.so")
MUL5 = 0
MUL5 = cdll.LoadLibrary("./approlib/mul8u_2HH.so")
MUL6 = 0
MUL6 = cdll.LoadLibrary("./approlib/mul8u_2P7.so")
MUL7 = 0
MUL7 = cdll.LoadLibrary("./approlib/mul8u_CK5.so")
MUL8 = 0
MUL8 = cdll.LoadLibrary("./approlib/mul8u_KEM.so")


ADD161 = 0
ADD161 = cdll.LoadLibrary("./approlib/add16u_0EM.so")
ADD162 = 0
ADD162 = cdll.LoadLibrary("./approlib/add16u_073.so")
ADD163 = 0
ADD163 = cdll.LoadLibrary("./approlib/add16u_00G.so")
ADD164 = 0
ADD164 = cdll.LoadLibrary("./approlib/add16u_02E.so")


ADD165 = 0
ADD165 = cdll.LoadLibrary("./approlib/add16u_0M0.so")
ADD166 = 0
ADD166 = cdll.LoadLibrary("./approlib/add16u_1E2.so")
ADD167 = 0
ADD167 = cdll.LoadLibrary("./approlib/add16u_1JH.so")
ADD168 = 0
ADD168 = cdll.LoadLibrary("./approlib/add16u_0RN.so")


ADD169 = 0
ADD169 = cdll.LoadLibrary("./approlib/add16se_1Y7.so")
ADD170 = 0
ADD170 = cdll.LoadLibrary("./approlib/add16se_2JY.so")
ADD171 = 0
ADD171 = cdll.LoadLibrary("./approlib/add16se_20J.so")
ADD172 = 0
ADD172 = cdll.LoadLibrary("./approlib/add16se_26Q.so")
ADD173 = 0
ADD173 = cdll.LoadLibrary("./approlib/add16se_2BY.so")

# def excel_one_line_to_list():
#     b = np.arange(0, 256)
#     df = pd.read_excel("222.xlsx", usecols=b,
#                        names=None)  # 读取项目名称和行业领域两列，并不要列名
#     df_li = df.values.tolist()
#     return df_li
def dcterrorcomputing(obj1):
    # q=excel_one_line_to_list()
    n1=0 #随机变量生成范围
    n2=255 #随机变量生成范围
    xunh=100000 #循环次数也就是随机变量的个数
    A1=6
    A2=25
    sum=[]
    # for i in range (0,len(q[0])-3):
    for j in range(0,xunh):
        a= random.randint(n1, n2)
        b=random.randint(n1, n2)
        d = random.randint(n1, n2)
        c=random.randint(n1, n2)
        a1= random.randint(n1, n2)
        b1=random.randint(n1, n2)
        d1 = random.randint(n1, n2)
        c1=random.randint(n1, n2)
        input1=a
        input2=0
        if obj1[0]['functions']['function'] == 'mul':
            obj1[0]['functions']['write_data'] = input1 * input2
        if obj1[0]['functions']['function'] == 'mul8u_Y48':
            obj1[0]['functions']['write_data'] = MUL1.mul8u_Y48(input1, input2)
        if obj1[0]['functions']['function'] == 'mul8u_150Q':
            obj1[0]['functions']['write_data'] = MUL2.mul8u_150Q(input1, input2)
        if obj1[0]['functions']['function'] == 'mul8u_2P7':
            obj1[0]['functions']['write_data'] = MUL6.mul8u_2P7(input1, input2)
        if obj1[0]['functions']['function'] == 'mul8u_KEM':
            obj1[0]['functions']['write_data'] = MUL8.mul8u_KEM(input1, input2)
        if obj1[0]['functions']['function'] == 'mul8u_CK5':
            obj1[0]['functions']['write_data'] = MUL7.mul8u_CK5(input1, input2)


        input1=obj1[0]['functions']['write_data']
        input2=0
        # print(input1, input2)
        if obj1[1]['functions']['function'] == 'add':
            obj1[1]['functions']['write_data'] = input1 + input2
        if obj1[1]['functions']['function'] == 'add16u_0RN':
            obj1[1]['functions']['write_data'] = ADD168.add16u_0RN(input1, input2)
        if obj1[1]['functions']['function'] == 'add16u_0EM':
            obj1[1]['functions']['write_data'] = ADD161.add16u_0EM(input1, input2)
        if obj1[1]['functions']['function'] == 'add16u_1JH':
            obj1[1]['functions']['write_data'] = ADD167.add16u_1JH(input1, input2)
        if obj1[1]['functions']['function'] == 'add16u_073':
            obj1[1]['functions']['write_data'] = ADD162.add16u_073(input1, input2)
        if obj1[1]['functions']['function'] == 'add16u_0M0':
            obj1[1]['functions']['write_data'] = ADD165.add16u_0M0(input1, input2)



        input1=a
        input2=50
        if obj1[2]['functions']['function'] == 'mul':
            obj1[2]['functions']['write_data'] = input1 * input2
        if obj1[2]['functions']['function'] == 'mul8u_Y48':
            obj1[2]['functions']['write_data'] = MUL1.mul8u_Y48(input1, input2)
        if obj1[2]['functions']['function'] == 'mul8u_150Q':
            obj1[2]['functions']['write_data'] = MUL2.mul8u_150Q(input1, input2)
        if obj1[2]['functions']['function'] == 'mul8u_2P7':
            obj1[2]['functions']['write_data'] = MUL6.mul8u_2P7(input1, input2)
        if obj1[2]['functions']['function'] == 'mul8u_KEM':
            obj1[2]['functions']['write_data'] = MUL8.mul8u_KEM(input1, input2)
        if obj1[2]['functions']['function'] == 'mul8u_CK5':
            obj1[2]['functions']['write_data'] = MUL7.mul8u_CK5(input1, input2)

        input1=obj1[1]['functions']['write_data']
        input2=obj1[2]['functions']['write_data']
        # print(input1, input2)
        if obj1[3]['functions']['function'] == 'add':
            obj1[3]['functions']['write_data'] = input1 + input2
        if obj1[3]['functions']['function'] == 'add16u_0RN':
            obj1[3]['functions']['write_data'] = ADD168.add16u_0RN(input1, input2)
        if obj1[3]['functions']['function'] == 'add16u_0EM':
            obj1[3]['functions']['write_data'] = ADD161.add16u_0EM(input1, input2)
        if obj1[3]['functions']['function'] == 'add16u_1JH':
            obj1[3]['functions']['write_data'] = ADD167.add16u_1JH(input1, input2)
        if obj1[3]['functions']['function'] == 'add16u_073':
            obj1[3]['functions']['write_data'] = ADD162.add16u_073(input1, input2)
        if obj1[3]['functions']['function'] == 'add16u_0M0':
            obj1[3]['functions']['write_data'] = ADD165.add16u_0M0(input1, input2)

        input1=a
        input2=10
        if obj1[4]['functions']['function'] == 'mul':
            obj1[4]['functions']['write_data'] = input1 * input2
        if obj1[4]['functions']['function'] == 'mul8u_Y48':
            obj1[4]['functions']['write_data'] = MUL1.mul8u_Y48(input1, input2)
        if obj1[4]['functions']['function'] == 'mul8u_150Q':
            obj1[4]['functions']['write_data'] = MUL2.mul8u_150Q(input1, input2)
        if obj1[4]['functions']['function'] == 'mul8u_2P7':
            obj1[4]['functions']['write_data'] = MUL6.mul8u_2P7(input1, input2)
        if obj1[4]['functions']['function'] == 'mul8u_KEM':
            obj1[4]['functions']['write_data'] = MUL8.mul8u_KEM(input1, input2)
        if obj1[4]['functions']['function'] == 'mul8u_CK5':
            obj1[4]['functions']['write_data'] = MUL7.mul8u_CK5(input1, input2)

        input1=obj1[4]['functions']['write_data']
        input2=obj1[3]['functions']['write_data']
        # print(input1, input2)
        if obj1[5]['functions']['function'] == 'add':
            obj1[5]['functions']['write_data'] = input1 + input2
        if obj1[5]['functions']['function'] == 'add16u_0RN':
            obj1[5]['functions']['write_data'] = ADD168.add16u_0RN(input1, input2)
        if obj1[5]['functions']['function'] == 'add16u_0EM':
            obj1[5]['functions']['write_data'] = ADD161.add16u_0EM(input1, input2)
        if obj1[5]['functions']['function'] == 'add16u_1JH':
            obj1[5]['functions']['write_data'] = ADD167.add16u_1JH(input1, input2)
        if obj1[5]['functions']['function'] == 'add16u_073':
            obj1[5]['functions']['write_data'] = ADD162.add16u_073(input1, input2)
        if obj1[5]['functions']['function'] == 'add16u_0M0':
            obj1[5]['functions']['write_data'] = ADD165.add16u_0M0(input1, input2)

        input1=a
        input2=15
        # print(input1, input2)
        if obj1[6]['functions']['function'] == 'mul':
            obj1[6]['functions']['write_data'] = input1 * input2
        if obj1[6]['functions']['function'] == 'mul8u_Y48':
            obj1[6]['functions']['write_data'] = MUL1.mul8u_Y48(input1, input2)
        if obj1[6]['functions']['function'] == 'mul8u_150Q':
            obj1[6]['functions']['write_data'] = MUL2.mul8u_150Q(input1, input2)
        if obj1[6]['functions']['function'] == 'mul8u_2P7':
            obj1[6]['functions']['write_data'] = MUL6.mul8u_2P7(input1, input2)
        if obj1[6]['functions']['function'] == 'mul8u_KEM':
            obj1[6]['functions']['write_data'] = MUL8.mul8u_KEM(input1, input2)
        if obj1[6]['functions']['function'] == 'mul8u_CK5':
            obj1[6]['functions']['write_data'] = MUL7.mul8u_CK5(input1, input2)

        input1=obj1[6]['functions']['write_data']
        input2=obj1[5]['functions']['write_data']
        # print(input1, input2)
        if obj1[7]['functions']['function'] == 'add':
            obj1[7]['functions']['write_data'] = input1 + input2
        if obj1[7]['functions']['function'] == 'add16u_0RN':
            obj1[7]['functions']['write_data'] = ADD168.add16u_0RN(input1, input2)
        if obj1[7]['functions']['function'] == 'add16u_0EM':
            obj1[7]['functions']['write_data'] = ADD161.add16u_0EM(input1, input2)
        if obj1[7]['functions']['function'] == 'add16u_1JH':
            obj1[7]['functions']['write_data'] = ADD167.add16u_1JH(input1, input2)
        if obj1[7]['functions']['function'] == 'add16u_073':
            obj1[7]['functions']['write_data'] = ADD162.add16u_073(input1, input2)
        if obj1[7]['functions']['function'] == 'add16u_0M0':
            obj1[7]['functions']['write_data'] = ADD165.add16u_0M0(input1, input2)




        input1=b
        input2=19
        # print(input1, input2)
        if obj1[8]['functions']['function'] == 'mul':
            obj1[8]['functions']['write_data'] = input1 * input2
        if obj1[8]['functions']['function'] == 'mul8u_Y48':
            obj1[8]['functions']['write_data'] = MUL1.mul8u_Y48(input1, input2)
        if obj1[8]['functions']['function'] == 'mul8u_150Q':
            obj1[8]['functions']['write_data'] = MUL2.mul8u_150Q(input1, input2)
        if obj1[8]['functions']['function'] == 'mul8u_2P7':
            obj1[8]['functions']['write_data'] = MUL6.mul8u_2P7(input1, input2)
        if obj1[8]['functions']['function'] == 'mul8u_KEM':
            obj1[8]['functions']['write_data'] = MUL8.mul8u_KEM(input1, input2)
        if obj1[8]['functions']['function'] == 'mul8u_CK5':
            obj1[8]['functions']['write_data'] = MUL7.mul8u_CK5(input1, input2)


        input1=obj1[8]['functions']['write_data']
        input2=0
        # print(input1, input2)
        if obj1[9]['functions']['function'] == 'add':
            obj1[9]['functions']['write_data'] = (input1)+(input2)
        if obj1[9]['functions']['function'] == 'add16u_0RN':
            obj1[9]['functions']['write_data'] = ADD168.add16u_0RN(input1, input2)
        if obj1[9]['functions']['function'] == 'add16u_0EM':
            obj1[9]['functions']['write_data'] = ADD161.add16u_0EM(input1, input2)
        if obj1[9]['functions']['function'] == 'add16u_1JH':
            obj1[9]['functions']['write_data'] = ADD167.add16u_1JH(input1, input2)
        if obj1[9]['functions']['function'] == 'add16u_073':
            obj1[9]['functions']['write_data'] = ADD162.add16u_073(input1, input2)
        if obj1[9]['functions']['function'] == 'add16u_0M0':
            obj1[9]['functions']['write_data'] = ADD165.add16u_0M0(input1, input2)


        input1=b
        input2=24
        # print(input1, input2)
        if obj1[10]['functions']['function'] == 'mul':
            obj1[10]['functions']['write_data'] = input1 * input2
        if obj1[10]['functions']['function'] == 'mul8u_Y48':
            obj1[10]['functions']['write_data'] = MUL1.mul8u_Y48(input1, input2)
        if obj1[10]['functions']['function'] == 'mul8u_150Q':
            obj1[10]['functions']['write_data'] = MUL2.mul8u_150Q(input1, input2)
        if obj1[10]['functions']['function'] == 'mul8u_2P7':
            obj1[10]['functions']['write_data'] = MUL6.mul8u_2P7(input1, input2)
        if obj1[10]['functions']['function'] == 'mul8u_KEM':
            obj1[10]['functions']['write_data'] = MUL8.mul8u_KEM(input1, input2)
        if obj1[10]['functions']['function'] == 'mul8u_CK5':
            obj1[10]['functions']['write_data'] = MUL7.mul8u_CK5(input1, input2)

        input1=obj1[10]['functions']['write_data']
        input2=obj1[9]['functions']['write_data']
        # print(input1, input2)
        if obj1[11]['functions']['function'] == 'add':
            obj1[11]['functions']['write_data'] = input1 + input2
        if obj1[11]['functions']['function'] == 'add16u_0RN':
            obj1[11]['functions']['write_data'] = ADD168.add16u_0RN(input1, input2)
        if obj1[11]['functions']['function'] == 'add16u_0EM':
            obj1[11]['functions']['write_data'] = ADD161.add16u_0EM(input1, input2)
        if obj1[11]['functions']['function'] == 'add16u_1JH':
            obj1[11]['functions']['write_data'] = ADD167.add16u_1JH(input1, input2)
        if obj1[11]['functions']['function'] == 'add16u_073':
            obj1[11]['functions']['write_data'] = ADD162.add16u_073(input1, input2)
        if obj1[11]['functions']['function'] == 'add16u_0M0':
            obj1[11]['functions']['write_data'] = ADD165.add16u_0M0(input1, input2)

        input1=b
        input2=28
        # print(input1, input2)
        if obj1[12]['functions']['function'] == 'mul':
            obj1[12]['functions']['write_data'] = input1 * input2
        if obj1[12]['functions']['function'] == 'mul8u_Y48':
            obj1[12]['functions']['write_data'] = MUL1.mul8u_Y48(input1, input2)
        if obj1[12]['functions']['function'] == 'mul8u_150Q':
            obj1[12]['functions']['write_data'] = MUL2.mul8u_150Q(input1, input2)
        if obj1[12]['functions']['function'] == 'mul8u_2P7':
            obj1[12]['functions']['write_data'] = MUL6.mul8u_2P7(input1, input2)
        if obj1[12]['functions']['function'] == 'mul8u_KEM':
            obj1[12]['functions']['write_data'] = MUL8.mul8u_KEM(input1, input2)
        if obj1[12]['functions']['function'] == 'mul8u_CK5':
            obj1[12]['functions']['write_data'] = MUL7.mul8u_CK5(input1, input2)

        input1=obj1[12]['functions']['write_data']
        input2=obj1[11]['functions']['write_data']
        # print(input1, input2)
        if obj1[13]['functions']['function'] == 'add':
            obj1[13]['functions']['write_data'] = input1 + input2
        if obj1[13]['functions']['function'] == 'add16u_0RN':
            obj1[13]['functions']['write_data'] = ADD168.add16u_0RN(input1, input2)
        if obj1[13]['functions']['function'] == 'add16u_0EM':
            obj1[13]['functions']['write_data'] = ADD161.add16u_0EM(input1, input2)
        if obj1[13]['functions']['function'] == 'add16u_1JH':
            obj1[13]['functions']['write_data'] = ADD167.add16u_1JH(input1, input2)
        if obj1[13]['functions']['function'] == 'add16u_073':
            obj1[13]['functions']['write_data'] = ADD162.add16u_073(input1, input2)
        if obj1[13]['functions']['function'] == 'add16u_0M0':
            obj1[13]['functions']['write_data'] = ADD165.add16u_0M0(input1, input2)

        input1=b
        input2=32
        # print(input1, input2)
        if obj1[14]['functions']['function'] == 'mul':
            obj1[14]['functions']['write_data'] = input1 * input2
        if obj1[14]['functions']['function'] == 'mul8u_Y48':
            obj1[14]['functions']['write_data'] = MUL1.mul8u_Y48(input1, input2)
        if obj1[14]['functions']['function'] == 'mul8u_150Q':
            obj1[14]['functions']['write_data'] = MUL2.mul8u_150Q(input1, input2)
        if obj1[14]['functions']['function'] == 'mul8u_2P7':
            obj1[14]['functions']['write_data'] = MUL6.mul8u_2P7(input1, input2)
        if obj1[14]['functions']['function'] == 'mul8u_KEM':
            obj1[14]['functions']['write_data'] = MUL8.mul8u_KEM(input1, input2)
        if obj1[14]['functions']['function'] == 'mul8u_CK5':
            obj1[14]['functions']['write_data'] = MUL7.mul8u_CK5(input1, input2)

        input1=obj1[14]['functions']['write_data']
        input2=obj1[13]['functions']['write_data']
        # print(input1,input2)
        if obj1[15]['functions']['function'] == 'add':
            obj1[15]['functions']['write_data'] = input1 + input2
        if obj1[15]['functions']['function'] == 'add16u_0RN':
            obj1[15]['functions']['write_data'] = ADD168.add16u_0RN(input1, input2)
        if obj1[15]['functions']['function'] == 'add16u_0EM':
            obj1[15]['functions']['write_data'] = ADD161.add16u_0EM(input1, input2)
        if obj1[15]['functions']['function'] == 'add16u_1JH':
            obj1[15]['functions']['write_data'] = ADD167.add16u_1JH(input1, input2)
        if obj1[15]['functions']['function'] == 'add16u_073':
            obj1[15]['functions']['write_data'] = ADD162.add16u_073(input1, input2)
        if obj1[15]['functions']['function'] == 'add16u_0M0':
            obj1[15]['functions']['write_data'] = ADD165.add16u_0M0(input1, input2)




        input1=c
        input2=36
        # print(input1, input2)
        if obj1[16]['functions']['function'] == 'mul':
            obj1[16]['functions']['write_data'] = input1 * input2
        if obj1[16]['functions']['function'] == 'mul8u_Y48':
            obj1[16]['functions']['write_data'] = MUL1.mul8u_Y48(input1, input2)
        if obj1[16]['functions']['function'] == 'mul8u_150Q':
            obj1[16]['functions']['write_data'] = MUL2.mul8u_150Q(input1, input2)
        if obj1[16]['functions']['function'] == 'mul8u_2P7':
            obj1[16]['functions']['write_data'] = MUL6.mul8u_2P7(input1, input2)
        if obj1[16]['functions']['function'] == 'mul8u_KEM':
            obj1[16]['functions']['write_data'] = MUL8.mul8u_KEM(input1, input2)
        if obj1[16]['functions']['function'] == 'mul8u_CK5':
            obj1[16]['functions']['write_data'] = MUL7.mul8u_CK5(input1, input2)


        input1=obj1[16]['functions']['write_data']
        input2=0
        # print(input1, input2)
        if obj1[17]['functions']['function'] == 'add':
            obj1[17]['functions']['write_data'] = input1 + input2
        if obj1[17]['functions']['function'] == 'add16u_0RN':
            obj1[17]['functions']['write_data'] = ADD168.add16u_0RN(input1, input2)
        if obj1[17]['functions']['function'] == 'add16u_0EM':
            obj1[17]['functions']['write_data'] = ADD161.add16u_0EM(input1, input2)
        if obj1[17]['functions']['function'] == 'add16u_1JH':
            obj1[17]['functions']['write_data'] = ADD167.add16u_1JH(input1, input2)
        if obj1[17]['functions']['function'] == 'add16u_073':
            obj1[17]['functions']['write_data'] = ADD162.add16u_073(input1, input2)
        if obj1[17]['functions']['function'] == 'add16u_0M0':
            obj1[17]['functions']['write_data'] = ADD165.add16u_0M0(input1, input2)


        input1=c
        input2=39
        if obj1[18]['functions']['function'] == 'mul':
            obj1[18]['functions']['write_data'] = input1 * input2
        if obj1[18]['functions']['function'] == 'mul8u_Y48':
            obj1[18]['functions']['write_data'] = MUL1.mul8u_Y48(input1, input2)
        if obj1[18]['functions']['function'] == 'mul8u_150Q':
            obj1[18]['functions']['write_data'] = MUL2.mul8u_150Q(input1, input2)
        if obj1[18]['functions']['function'] == 'mul8u_2P7':
            obj1[18]['functions']['write_data'] = MUL6.mul8u_2P7(input1, input2)
        if obj1[18]['functions']['function'] == 'mul8u_KEM':
            obj1[18]['functions']['write_data'] = MUL8.mul8u_KEM(input1, input2)
        if obj1[18]['functions']['function'] == 'mul8u_CK5':
            obj1[18]['functions']['write_data'] = MUL7.mul8u_CK5(input1, input2)

        input1=obj1[18]['functions']['write_data']
        input2=obj1[17]['functions']['write_data']
        # print(input1, input2)
        if obj1[19]['functions']['function'] == 'add':
            obj1[19]['functions']['write_data'] = input1 + input2
        if obj1[19]['functions']['function'] == 'add16u_0RN':
            obj1[19]['functions']['write_data'] = ADD168.add16u_0RN(input1, input2)
        if obj1[19]['functions']['function'] == 'add16u_0EM':
            obj1[19]['functions']['write_data'] = ADD161.add16u_0EM(input1, input2)
        if obj1[19]['functions']['function'] == 'add16u_1JH':
            obj1[19]['functions']['write_data'] = ADD167.add16u_1JH(input1, input2)
        if obj1[19]['functions']['function'] == 'add16u_073':
            obj1[19]['functions']['write_data'] = ADD162.add16u_073(input1, input2)
        if obj1[19]['functions']['function'] == 'add16u_0M0':
            obj1[19]['functions']['write_data'] = ADD165.add16u_0M0(input1, input2)

        input1=c
        input2=42
        if obj1[20]['functions']['function'] == 'mul':
            obj1[20]['functions']['write_data'] = input1 * input2
        if obj1[20]['functions']['function'] == 'mul8u_Y48':
            obj1[20]['functions']['write_data'] = MUL1.mul8u_Y48(input1, input2)
        if obj1[20]['functions']['function'] == 'mul8u_150Q':
            obj1[20]['functions']['write_data'] = MUL2.mul8u_150Q(input1, input2)
        if obj1[20]['functions']['function'] == 'mul8u_2P7':
            obj1[20]['functions']['write_data'] = MUL6.mul8u_2P7(input1, input2)
        if obj1[20]['functions']['function'] == 'mul8u_KEM':
            obj1[20]['functions']['write_data'] = MUL8.mul8u_KEM(input1, input2)
        if obj1[20]['functions']['function'] == 'mul8u_CK5':
            obj1[20]['functions']['write_data'] = MUL7.mul8u_CK5(input1, input2)

        input1=obj1[20]['functions']['write_data']
        input2=obj1[19]['functions']['write_data']
        # print(input1,input2)
        if obj1[21]['functions']['function'] == 'add':
            obj1[21]['functions']['write_data'] = input1 + input2
        if obj1[21]['functions']['function'] == 'add16u_0RN':
            obj1[21]['functions']['write_data'] = ADD168.add16u_0RN(input1, input2)
        if obj1[21]['functions']['function'] == 'add16u_0EM':
            obj1[21]['functions']['write_data'] = ADD161.add16u_0EM(input1, input2)
        if obj1[21]['functions']['function'] == 'add16u_1JH':
            obj1[21]['functions']['write_data'] = ADD167.add16u_1JH(input1, input2)
        if obj1[21]['functions']['function'] == 'add16u_073':
            obj1[21]['functions']['write_data'] = ADD162.add16u_073(input1, input2)
        if obj1[21]['functions']['function'] == 'add16u_0M0':
            obj1[21]['functions']['write_data'] = ADD165.add16u_0M0(input1, input2)

        input1=c
        input2=45
        if obj1[22]['functions']['function'] == 'mul':
            obj1[22]['functions']['write_data'] = input1 * input2
        if obj1[22]['functions']['function'] == 'mul8u_Y48':
            obj1[22]['functions']['write_data'] = MUL1.mul8u_Y48(input1, input2)
        if obj1[22]['functions']['function'] == 'mul8u_150Q':
            obj1[22]['functions']['write_data'] = MUL2.mul8u_150Q(input1, input2)
        if obj1[22]['functions']['function'] == 'mul8u_2P7':
            obj1[22]['functions']['write_data'] = MUL6.mul8u_2P7(input1, input2)
        if obj1[22]['functions']['function'] == 'mul8u_KEM':
            obj1[22]['functions']['write_data'] = MUL8.mul8u_KEM(input1, input2)
        if obj1[22]['functions']['function'] == 'mul8u_CK5':
            obj1[22]['functions']['write_data'] = MUL7.mul8u_CK5(input1, input2)

        input1=obj1[22]['functions']['write_data']
        input2=obj1[21]['functions']['write_data']
        # print(input1, input2)
        if obj1[23]['functions']['function'] == 'add':
            obj1[23]['functions']['write_data'] = input1 + input2
        if obj1[23]['functions']['function'] == 'add16u_0RN':
            obj1[23]['functions']['write_data'] = ADD168.add16u_0RN(input1, input2)
        if obj1[23]['functions']['function'] == 'add16u_0EM':
            obj1[23]['functions']['write_data'] = ADD161.add16u_0EM(input1, input2)
        if obj1[23]['functions']['function'] == 'add16u_1JH':
            obj1[23]['functions']['write_data'] = ADD167.add16u_1JH(input1, input2)
        if obj1[23]['functions']['function'] == 'add16u_073':
            obj1[23]['functions']['write_data'] = ADD162.add16u_073(input1, input2)
        if obj1[23]['functions']['function'] == 'add16u_0M0':
            obj1[23]['functions']['write_data'] = ADD165.add16u_0M0(input1, input2)




        input1=d
        input2=47
        if obj1[24]['functions']['function'] == 'mul':
            obj1[24]['functions']['write_data'] = input1 * input2
        if obj1[24]['functions']['function'] == 'mul8u_Y48':
            obj1[24]['functions']['write_data'] = MUL1.mul8u_Y48(input1, input2)
        if obj1[24]['functions']['function'] == 'mul8u_150Q':
            obj1[24]['functions']['write_data'] = MUL2.mul8u_150Q(input1, input2)
        if obj1[24]['functions']['function'] == 'mul8u_2P7':
            obj1[24]['functions']['write_data'] = MUL6.mul8u_2P7(input1, input2)
        if obj1[24]['functions']['function'] == 'mul8u_KEM':
            obj1[24]['functions']['write_data'] = MUL8.mul8u_KEM(input1, input2)
        if obj1[24]['functions']['function'] == 'mul8u_CK5':
            obj1[24]['functions']['write_data'] = MUL7.mul8u_CK5(input1, input2)


        input1=obj1[24]['functions']['write_data']
        input2=0
        if obj1[25]['functions']['function'] == 'add':
            obj1[25]['functions']['write_data'] = input1 + input2
        if obj1[25]['functions']['function'] == 'add16u_0RN':
            obj1[25]['functions']['write_data'] = ADD168.add16u_0RN(input1, input2)
        if obj1[25]['functions']['function'] == 'add16u_0EM':
            obj1[25]['functions']['write_data'] = ADD161.add16u_0EM(input1, input2)
        if obj1[25]['functions']['function'] == 'add16u_1JH':
            obj1[25]['functions']['write_data'] = ADD167.add16u_1JH(input1, input2)
        if obj1[25]['functions']['function'] == 'add16u_073':
            obj1[25]['functions']['write_data'] = ADD162.add16u_073(input1, input2)
        if obj1[25]['functions']['function'] == 'add16u_0M0':
            obj1[25]['functions']['write_data'] = ADD165.add16u_0M0(input1, input2)


        input1=d
        input2=49
        if obj1[26]['functions']['function'] == 'mul':
            obj1[26]['functions']['write_data'] = input1 * input2
        if obj1[26]['functions']['function'] == 'mul8u_Y48':
            obj1[26]['functions']['write_data'] = MUL1.mul8u_Y48(input1, input2)
        if obj1[26]['functions']['function'] == 'mul8u_150Q':
            obj1[26]['functions']['write_data'] = MUL2.mul8u_150Q(input1, input2)
        if obj1[26]['functions']['function'] == 'mul8u_2P7':
            obj1[26]['functions']['write_data'] = MUL6.mul8u_2P7(input1, input2)
        if obj1[26]['functions']['function'] == 'mul8u_KEM':
            obj1[26]['functions']['write_data'] = MUL8.mul8u_KEM(input1, input2)
        if obj1[26]['functions']['function'] == 'mul8u_CK5':
            obj1[26]['functions']['write_data'] = MUL7.mul8u_CK5(input1, input2)

        input1=obj1[26]['functions']['write_data']
        input2=obj1[25]['functions']['write_data']
        if obj1[27]['functions']['function'] == 'add':
            obj1[27]['functions']['write_data'] = input1 + input2
        if obj1[27]['functions']['function'] == 'add16u_0RN':
            obj1[27]['functions']['write_data'] = ADD168.add16u_0RN(input1, input2)
        if obj1[27]['functions']['function'] == 'add16u_0EM':
            obj1[27]['functions']['write_data'] = ADD161.add16u_0EM(input1, input2)
        if obj1[27]['functions']['function'] == 'add16u_1JH':
            obj1[27]['functions']['write_data'] = ADD167.add16u_1JH(input1, input2)
        if obj1[27]['functions']['function'] == 'add16u_073':
            obj1[27]['functions']['write_data'] = ADD162.add16u_073(input1, input2)
        if obj1[27]['functions']['function'] == 'add16u_0M0':
            obj1[27]['functions']['write_data'] = ADD165.add16u_0M0(input1, input2)


        input1=d
        input2=50
        if obj1[28]['functions']['function'] == 'mul':
            obj1[28]['functions']['write_data'] = input1 * input2
        if obj1[28]['functions']['function'] == 'mul8u_Y48':
            obj1[28]['functions']['write_data'] = MUL1.mul8u_Y48(input1, input2)
        if obj1[28]['functions']['function'] == 'mul8u_150Q':
            obj1[28]['functions']['write_data'] = MUL2.mul8u_150Q(input1, input2)
        if obj1[28]['functions']['function'] == 'mul8u_2P7':
            obj1[28]['functions']['write_data'] = MUL6.mul8u_2P7(input1, input2)
        if obj1[28]['functions']['function'] == 'mul8u_KEM':
            obj1[28]['functions']['write_data'] = MUL8.mul8u_KEM(input1, input2)
        if obj1[28]['functions']['function'] == 'mul8u_CK5':
            obj1[28]['functions']['write_data'] = MUL7.mul8u_CK5(input1, input2)

        input1=obj1[28]['functions']['write_data']
        input2=obj1[27]['functions']['write_data']
        if obj1[29]['functions']['function'] == 'add':
            obj1[29]['functions']['write_data'] = input1 + input2
        if obj1[29]['functions']['function'] == 'add16u_0RN':
            obj1[29]['functions']['write_data'] = ADD168.add16u_0RN(input1, input2)
        if obj1[29]['functions']['function'] == 'add16u_0EM':
            obj1[29]['functions']['write_data'] = ADD161.add16u_0EM(input1, input2)
        if obj1[29]['functions']['function'] == 'add16u_1JH':
            obj1[29]['functions']['write_data'] = ADD167.add16u_1JH(input1, input2)
        if obj1[29]['functions']['function'] == 'add16u_073':
            obj1[29]['functions']['write_data'] = ADD162.add16u_073(input1, input2)
        if obj1[29]['functions']['function'] == 'add16u_0M0':
            obj1[29]['functions']['write_data'] = ADD165.add16u_0M0(input1, input2)

        input1=d
        input2=51
        if obj1[30]['functions']['function'] == 'mul':
            obj1[30]['functions']['write_data'] = input1 * input2
        if obj1[30]['functions']['function'] == 'mul8u_Y48':
            obj1[30]['functions']['write_data'] = MUL1.mul8u_Y48(input1, input2)
        if obj1[30]['functions']['function'] == 'mul8u_150Q':
            obj1[30]['functions']['write_data'] = MUL2.mul8u_150Q(input1, input2)
        if obj1[30]['functions']['function'] == 'mul8u_2P7':
            obj1[30]['functions']['write_data'] = MUL6.mul8u_2P7(input1, input2)
        if obj1[30]['functions']['function'] == 'mul8u_KEM':
            obj1[30]['functions']['write_data'] = MUL8.mul8u_KEM(input1, input2)
        if obj1[30]['functions']['function'] == 'mul8u_CK5':
            obj1[30]['functions']['write_data'] = MUL7.mul8u_CK5(input1, input2)

        input1=obj1[30]['functions']['write_data']
        input2=obj1[29]['functions']['write_data']
        if obj1[31]['functions']['function'] == 'add':
            obj1[31]['functions']['write_data'] = input1 + input2
        if obj1[31]['functions']['function'] == 'add16u_0RN':
            obj1[31]['functions']['write_data'] = ADD168.add16u_0RN(input1, input2)
        if obj1[31]['functions']['function'] == 'add16u_0EM':
            obj1[31]['functions']['write_data'] = ADD161.add16u_0EM(input1, input2)
        if obj1[31]['functions']['function'] == 'add16u_1JH':
            obj1[31]['functions']['write_data'] = ADD167.add16u_1JH(input1, input2)
        if obj1[31]['functions']['function'] == 'add16u_073':
            obj1[31]['functions']['write_data'] = ADD162.add16u_073(input1, input2)
        if obj1[31]['functions']['function'] == 'add16u_0M0':
            obj1[31]['functions']['write_data'] = ADD165.add16u_0M0(input1, input2)

        input1 = a1
        input2 = 51
        if obj1[32]['functions']['function'] == 'mul':
            obj1[32]['functions']['write_data'] = input1 * input2
        if obj1[32]['functions']['function'] == 'mul8u_Y48':
            obj1[32]['functions']['write_data'] = MUL1.mul8u_Y48(input1, input2)
        if obj1[32]['functions']['function'] == 'mul8u_150Q':
            obj1[32]['functions']['write_data'] = MUL2.mul8u_150Q(input1, input2)
        if obj1[32]['functions']['function'] == 'mul8u_2P7':
            obj1[32]['functions']['write_data'] = MUL6.mul8u_2P7(input1, input2)
        if obj1[32]['functions']['function'] == 'mul8u_KEM':
            obj1[32]['functions']['write_data'] = MUL8.mul8u_KEM(input1, input2)
        if obj1[32]['functions']['function'] == 'mul8u_CK5':
            obj1[32]['functions']['write_data'] = MUL7.mul8u_CK5(input1, input2)

        input1 = obj1[32]['functions']['write_data']
        input2 = 0
        if obj1[33]['functions']['function'] == 'add':
            obj1[33]['functions']['write_data'] = input1 + input2
        if obj1[33]['functions']['function'] == 'add16u_0RN':
            obj1[33]['functions']['write_data'] = ADD168.add16u_0RN(input1, input2)
        if obj1[33]['functions']['function'] == 'add16u_0EM':
            obj1[33]['functions']['write_data'] = ADD161.add16u_0EM(input1, input2)
        if obj1[33]['functions']['function'] == 'add16u_1JH':
            obj1[33]['functions']['write_data'] = ADD167.add16u_1JH(input1, input2)
        if obj1[33]['functions']['function'] == 'add16u_073':
            obj1[33]['functions']['write_data'] = ADD162.add16u_073(input1, input2)
        if obj1[33]['functions']['function'] == 'add16u_0M0':
            obj1[33]['functions']['write_data'] = ADD165.add16u_0M0(input1, input2)

        input1 = a1
        input2 = 51
        if obj1[34]['functions']['function'] == 'mul':
            obj1[34]['functions']['write_data'] = input1 * input2
        if obj1[34]['functions']['function'] == 'mul8u_Y48':
            obj1[34]['functions']['write_data'] = MUL1.mul8u_Y48(input1, input2)
        if obj1[34]['functions']['function'] == 'mul8u_150Q':
            obj1[34]['functions']['write_data'] = MUL2.mul8u_150Q(input1, input2)
        if obj1[34]['functions']['function'] == 'mul8u_2P7':
            obj1[34]['functions']['write_data'] = MUL6.mul8u_2P7(input1, input2)
        if obj1[34]['functions']['function'] == 'mul8u_KEM':
            obj1[34]['functions']['write_data'] = MUL8.mul8u_KEM(input1, input2)
        if obj1[34]['functions']['function'] == 'mul8u_CK5':
            obj1[34]['functions']['write_data'] = MUL7.mul8u_CK5(input1, input2)

        input1 = obj1[34]['functions']['write_data']
        input2 = obj1[33]['functions']['write_data']
        if obj1[35]['functions']['function'] == 'add':
            obj1[35]['functions']['write_data'] = input1 + input2
        if obj1[35]['functions']['function'] == 'add16u_0RN':
            obj1[35]['functions']['write_data'] = ADD168.add16u_0RN(input1, input2)
        if obj1[35]['functions']['function'] == 'add16u_0EM':
            obj1[35]['functions']['write_data'] = ADD161.add16u_0EM(input1, input2)
        if obj1[35]['functions']['function'] == 'add16u_1JH':
            obj1[35]['functions']['write_data'] = ADD167.add16u_1JH(input1, input2)
        if obj1[35]['functions']['function'] == 'add16u_073':
            obj1[35]['functions']['write_data'] = ADD162.add16u_073(input1, input2)
        if obj1[35]['functions']['function'] == 'add16u_0M0':
            obj1[35]['functions']['write_data'] = ADD165.add16u_0M0(input1, input2)

        input1 = a1
        input2 = 51
        if obj1[36]['functions']['function'] == 'mul':
            obj1[36]['functions']['write_data'] = input1 * input2
        if obj1[36]['functions']['function'] == 'mul8u_Y48':
            obj1[36]['functions']['write_data'] = MUL1.mul8u_Y48(input1, input2)
        if obj1[36]['functions']['function'] == 'mul8u_150Q':
            obj1[36]['functions']['write_data'] = MUL2.mul8u_150Q(input1, input2)
        if obj1[36]['functions']['function'] == 'mul8u_2P7':
            obj1[36]['functions']['write_data'] = MUL6.mul8u_2P7(input1, input2)
        if obj1[36]['functions']['function'] == 'mul8u_KEM':
            obj1[36]['functions']['write_data'] = MUL8.mul8u_KEM(input1, input2)
        if obj1[36]['functions']['function'] == 'mul8u_CK5':
            obj1[36]['functions']['write_data'] = MUL7.mul8u_CK5(input1, input2)

        input1 = obj1[36]['functions']['write_data']
        input2 = obj1[35]['functions']['write_data']
        if obj1[37]['functions']['function'] == 'add':
            obj1[37]['functions']['write_data'] = input1 + input2
        if obj1[37]['functions']['function'] == 'add16u_0RN':
            obj1[37]['functions']['write_data'] = ADD168.add16u_0RN(input1, input2)
        if obj1[37]['functions']['function'] == 'add16u_0EM':
            obj1[37]['functions']['write_data'] = ADD161.add16u_0EM(input1, input2)
        if obj1[37]['functions']['function'] == 'add16u_1JH':
            obj1[37]['functions']['write_data'] = ADD167.add16u_1JH(input1, input2)
        if obj1[37]['functions']['function'] == 'add16u_073':
            obj1[37]['functions']['write_data'] = ADD162.add16u_073(input1, input2)
        if obj1[37]['functions']['function'] == 'add16u_0M0':
            obj1[37]['functions']['write_data'] = ADD165.add16u_0M0(input1, input2)

        input1 = a1
        input2 = 50
        if obj1[38]['functions']['function'] == 'mul':
            obj1[38]['functions']['write_data'] = input1 * input2
        if obj1[38]['functions']['function'] == 'mul8u_Y48':
            obj1[38]['functions']['write_data'] = MUL1.mul8u_Y48(input1, input2)
        if obj1[38]['functions']['function'] == 'mul8u_150Q':
            obj1[38]['functions']['write_data'] = MUL2.mul8u_150Q(input1, input2)
        if obj1[38]['functions']['function'] == 'mul8u_2P7':
            obj1[38]['functions']['write_data'] = MUL6.mul8u_2P7(input1, input2)
        if obj1[38]['functions']['function'] == 'mul8u_KEM':
            obj1[38]['functions']['write_data'] = MUL8.mul8u_KEM(input1, input2)
        if obj1[38]['functions']['function'] == 'mul8u_CK5':
            obj1[38]['functions']['write_data'] = MUL7.mul8u_CK5(input1, input2)

        input1 = obj1[38]['functions']['write_data']
        input2 = obj1[37]['functions']['write_data']
        # print()
        if obj1[39]['functions']['function'] == 'add':
            obj1[39]['functions']['write_data'] = input1 + input2
        if obj1[39]['functions']['function'] == 'add16u_0RN':
            obj1[39]['functions']['write_data'] = ADD168.add16u_0RN(input1, input2)
        if obj1[39]['functions']['function'] == 'add16u_0EM':
            obj1[39]['functions']['write_data'] = ADD161.add16u_0EM(input1, input2)
        if obj1[39]['functions']['function'] == 'add16u_1JH':
            obj1[39]['functions']['write_data'] = ADD167.add16u_1JH(input1, input2)
        if obj1[39]['functions']['function'] == 'add16u_073':
            obj1[39]['functions']['write_data'] = ADD162.add16u_073(input1, input2)
        if obj1[39]['functions']['function'] == 'add16u_0M0':
            obj1[39]['functions']['write_data'] = ADD165.add16u_0M0(input1, input2)



        input1 = b1
        input2 = 49
        if obj1[40]['functions']['function'] == 'mul':
            obj1[40]['functions']['write_data'] = input1 * input2
        if obj1[40]['functions']['function'] == 'mul8u_Y48':
            obj1[40]['functions']['write_data'] = MUL1.mul8u_Y48(input1, input2)
        if obj1[40]['functions']['function'] == 'mul8u_150Q':
            obj1[40]['functions']['write_data'] = MUL2.mul8u_150Q(input1, input2)
        if obj1[40]['functions']['function'] == 'mul8u_2P7':
            obj1[40]['functions']['write_data'] = MUL6.mul8u_2P7(input1, input2)
        if obj1[40]['functions']['function'] == 'mul8u_KEM':
            obj1[40]['functions']['write_data'] = MUL8.mul8u_KEM(input1, input2)
        if obj1[40]['functions']['function'] == 'mul8u_CK5':
            obj1[40]['functions']['write_data'] = MUL7.mul8u_CK5(input1, input2)

        input1 = obj1[40]['functions']['write_data']
        input2 = 0
        if obj1[41]['functions']['function'] == 'add':
            obj1[41]['functions']['write_data'] = input1 + input2
        if obj1[41]['functions']['function'] == 'add16u_0RN':
            obj1[41]['functions']['write_data'] = ADD168.add16u_0RN(input1, input2)
        if obj1[41]['functions']['function'] == 'add16u_0EM':
            obj1[41]['functions']['write_data'] = ADD161.add16u_0EM(input1, input2)
        if obj1[41]['functions']['function'] == 'add16u_1JH':
            obj1[41]['functions']['write_data'] = ADD167.add16u_1JH(input1, input2)
        if obj1[41]['functions']['function'] == 'add16u_073':
            obj1[41]['functions']['write_data'] = ADD162.add16u_073(input1, input2)
        if obj1[41]['functions']['function'] == 'add16u_0M0':
            obj1[41]['functions']['write_data'] = ADD165.add16u_0M0(input1, input2)

        input1 = b1
        input2 = 47
        if obj1[42]['functions']['function'] == 'mul':
            obj1[42]['functions']['write_data'] = input1 * input2
        if obj1[42]['functions']['function'] == 'mul8u_Y48':
            obj1[42]['functions']['write_data'] = MUL1.mul8u_Y48(input1, input2)
        if obj1[42]['functions']['function'] == 'mul8u_150Q':
            obj1[42]['functions']['write_data'] = MUL2.mul8u_150Q(input1, input2)
        if obj1[42]['functions']['function'] == 'mul8u_2P7':
            obj1[42]['functions']['write_data'] = MUL6.mul8u_2P7(input1, input2)
        if obj1[42]['functions']['function'] == 'mul8u_KEM':
            obj1[42]['functions']['write_data'] = MUL8.mul8u_KEM(input1, input2)
        if obj1[42]['functions']['function'] == 'mul8u_CK5':
            obj1[42]['functions']['write_data'] = MUL7.mul8u_CK5(input1, input2)

        input1 = obj1[42]['functions']['write_data']
        input2 = obj1[41]['functions']['write_data']
        if obj1[43]['functions']['function'] == 'add':
            obj1[43]['functions']['write_data'] = input1 + input2
        if obj1[43]['functions']['function'] == 'add16u_0RN':
            obj1[43]['functions']['write_data'] = ADD168.add16u_0RN(input1, input2)
        if obj1[43]['functions']['function'] == 'add16u_0EM':
            obj1[43]['functions']['write_data'] = ADD161.add16u_0EM(input1, input2)
        if obj1[43]['functions']['function'] == 'add16u_1JH':
            obj1[43]['functions']['write_data'] = ADD167.add16u_1JH(input1, input2)
        if obj1[43]['functions']['function'] == 'add16u_073':
            obj1[43]['functions']['write_data'] = ADD162.add16u_073(input1, input2)
        if obj1[43]['functions']['function'] == 'add16u_0M0':
            obj1[43]['functions']['write_data'] = ADD165.add16u_0M0(input1, input2)

        input1 = b1
        input2 = 45
        if obj1[44]['functions']['function'] == 'mul':
            obj1[44]['functions']['write_data'] = input1 * input2
        if obj1[44]['functions']['function'] == 'mul8u_Y48':
            obj1[44]['functions']['write_data'] = MUL1.mul8u_Y48(input1, input2)
        if obj1[44]['functions']['function'] == 'mul8u_150Q':
            obj1[44]['functions']['write_data'] = MUL2.mul8u_150Q(input1, input2)
        if obj1[44]['functions']['function'] == 'mul8u_2P7':
            obj1[44]['functions']['write_data'] = MUL6.mul8u_2P7(input1, input2)
        if obj1[44]['functions']['function'] == 'mul8u_KEM':
            obj1[44]['functions']['write_data'] = MUL8.mul8u_KEM(input1, input2)
        if obj1[44]['functions']['function'] == 'mul8u_CK5':
            obj1[44]['functions']['write_data'] = MUL7.mul8u_CK5(input1, input2)

        input1 = obj1[44]['functions']['write_data']
        input2 = obj1[43]['functions']['write_data']
        if obj1[45]['functions']['function'] == 'add':
            obj1[45]['functions']['write_data'] = input1 + input2
        if obj1[45]['functions']['function'] == 'add16u_0RN':
            obj1[45]['functions']['write_data'] = ADD168.add16u_0RN(input1, input2)
        if obj1[45]['functions']['function'] == 'add16u_0EM':
            obj1[45]['functions']['write_data'] = ADD161.add16u_0EM(input1, input2)
        if obj1[45]['functions']['function'] == 'add16u_1JH':
            obj1[45]['functions']['write_data'] = ADD167.add16u_1JH(input1, input2)
        if obj1[45]['functions']['function'] == 'add16u_073':
            obj1[45]['functions']['write_data'] = ADD162.add16u_073(input1, input2)
        if obj1[45]['functions']['function'] == 'add16u_0M0':
            obj1[45]['functions']['write_data'] = ADD165.add16u_0M0(input1, input2)

        input1 = b1
        input2 = 42
        if obj1[46]['functions']['function'] == 'mul':
            obj1[46]['functions']['write_data'] = input1 * input2
        if obj1[46]['functions']['function'] == 'mul8u_Y48':
            obj1[46]['functions']['write_data'] = MUL1.mul8u_Y48(input1, input2)
        if obj1[46]['functions']['function'] == 'mul8u_150Q':
            obj1[46]['functions']['write_data'] = MUL2.mul8u_150Q(input1, input2)
        if obj1[46]['functions']['function'] == 'mul8u_2P7':
            obj1[46]['functions']['write_data'] = MUL6.mul8u_2P7(input1, input2)
        if obj1[46]['functions']['function'] == 'mul8u_KEM':
            obj1[46]['functions']['write_data'] = MUL8.mul8u_KEM(input1, input2)
        if obj1[46]['functions']['function'] == 'mul8u_CK5':
            obj1[46]['functions']['write_data'] = MUL7.mul8u_CK5(input1, input2)

        input1 = obj1[46]['functions']['write_data']
        input2 = obj1[45]['functions']['write_data']
        if obj1[47]['functions']['function'] == 'add':
            obj1[47]['functions']['write_data'] = input1 + input2
        if obj1[47]['functions']['function'] == 'add16u_0RN':
            obj1[47]['functions']['write_data'] = ADD168.add16u_0RN(input1, input2)
        if obj1[47]['functions']['function'] == 'add16u_0EM':
            obj1[47]['functions']['write_data'] = ADD161.add16u_0EM(input1, input2)
        if obj1[47]['functions']['function'] == 'add16u_1JH':
            obj1[47]['functions']['write_data'] = ADD167.add16u_1JH(input1, input2)
        if obj1[47]['functions']['function'] == 'add16u_073':
            obj1[47]['functions']['write_data'] = ADD162.add16u_073(input1, input2)
        if obj1[47]['functions']['function'] == 'add16u_0M0':
            obj1[47]['functions']['write_data'] = ADD165.add16u_0M0(input1, input2)



        input1 = c1
        input2 = 39
        if obj1[48]['functions']['function'] == 'mul':
            obj1[48]['functions']['write_data'] = input1 * input2
        if obj1[48]['functions']['function'] == 'mul8u_Y48':
            obj1[48]['functions']['write_data'] = MUL1.mul8u_Y48(input1, input2)
        if obj1[48]['functions']['function'] == 'mul8u_150Q':
            obj1[48]['functions']['write_data'] = MUL2.mul8u_150Q(input1, input2)
        if obj1[48]['functions']['function'] == 'mul8u_2P7':
            obj1[48]['functions']['write_data'] = MUL6.mul8u_2P7(input1, input2)
        if obj1[48]['functions']['function'] == 'mul8u_KEM':
            obj1[48]['functions']['write_data'] = MUL8.mul8u_KEM(input1, input2)
        if obj1[48]['functions']['function'] == 'mul8u_CK5':
            obj1[48]['functions']['write_data'] = MUL7.mul8u_CK5(input1, input2)
        input1 = obj1[48]['functions']['write_data']
        input2 = 0
        if obj1[49]['functions']['function'] == 'add':
            obj1[49]['functions']['write_data'] = input1 + input2
        if obj1[49]['functions']['function'] == 'add16u_0RN':
            obj1[49]['functions']['write_data'] = ADD168.add16u_0RN(input1, input2)
        if obj1[49]['functions']['function'] == 'add16u_0EM':
            obj1[49]['functions']['write_data'] = ADD161.add16u_0EM(input1, input2)
        if obj1[49]['functions']['function'] == 'add16u_1JH':
            obj1[49]['functions']['write_data'] = ADD167.add16u_1JH(input1, input2)
        if obj1[49]['functions']['function'] == 'add16u_073':
            obj1[49]['functions']['write_data'] = ADD162.add16u_073(input1, input2)
        if obj1[49]['functions']['function'] == 'add16u_0M0':
            obj1[49]['functions']['write_data'] = ADD165.add16u_0M0(input1, input2)

        input1 = c1
        input2 = 36
        if obj1[50]['functions']['function'] == 'mul':
            obj1[50]['functions']['write_data'] = input1 * input2
        if obj1[50]['functions']['function'] == 'mul8u_Y48':
            obj1[50]['functions']['write_data'] = MUL1.mul8u_Y48(input1, input2)
        if obj1[50]['functions']['function'] == 'mul8u_150Q':
            obj1[50]['functions']['write_data'] = MUL2.mul8u_150Q(input1, input2)
        if obj1[50]['functions']['function'] == 'mul8u_2P7':
            obj1[50]['functions']['write_data'] = MUL6.mul8u_2P7(input1, input2)
        if obj1[50]['functions']['function'] == 'mul8u_KEM':
            obj1[50]['functions']['write_data'] = MUL8.mul8u_KEM(input1, input2)
        if obj1[50]['functions']['function'] == 'mul8u_CK5':
            obj1[50]['functions']['write_data'] = MUL7.mul8u_CK5(input1, input2)

        input1 = obj1[50]['functions']['write_data']
        input2 = obj1[49]['functions']['write_data']
        if obj1[51]['functions']['function'] == 'add':
            obj1[51]['functions']['write_data'] = input1 + input2
        if obj1[51]['functions']['function'] == 'add16u_0RN':
            obj1[51]['functions']['write_data'] = ADD168.add16u_0RN(input1, input2)
        if obj1[51]['functions']['function'] == 'add16u_0EM':
            obj1[51]['functions']['write_data'] = ADD161.add16u_0EM(input1, input2)
        if obj1[51]['functions']['function'] == 'add16u_1JH':
            obj1[51]['functions']['write_data'] = ADD167.add16u_1JH(input1, input2)
        if obj1[51]['functions']['function'] == 'add16u_073':
            obj1[51]['functions']['write_data'] = ADD162.add16u_073(input1, input2)
        if obj1[51]['functions']['function'] == 'add16u_0M0':
            obj1[51]['functions']['write_data'] = ADD165.add16u_0M0(input1, input2)

        input1 = c1
        input2 = 32
        if obj1[52]['functions']['function'] == 'mul':
            obj1[52]['functions']['write_data'] = input1 * input2
        if obj1[52]['functions']['function'] == 'mul8u_Y48':
            obj1[52]['functions']['write_data'] = MUL1.mul8u_Y48(input1, input2)
        if obj1[52]['functions']['function'] == 'mul8u_150Q':
            obj1[52]['functions']['write_data'] = MUL2.mul8u_150Q(input1, input2)
        if obj1[52]['functions']['function'] == 'mul8u_2P7':
            obj1[52]['functions']['write_data'] = MUL6.mul8u_2P7(input1, input2)
        if obj1[52]['functions']['function'] == 'mul8u_KEM':
            obj1[52]['functions']['write_data'] = MUL8.mul8u_KEM(input1, input2)
        if obj1[52]['functions']['function'] == 'mul8u_CK5':
            obj1[52]['functions']['write_data'] = MUL7.mul8u_CK5(input1, input2)

        input1 = obj1[52]['functions']['write_data']
        input2 = obj1[51]['functions']['write_data']
        if obj1[53]['functions']['function'] == 'add':
            obj1[53]['functions']['write_data'] = input1 + input2
        if obj1[53]['functions']['function'] == 'add16u_0RN':
            obj1[53]['functions']['write_data'] = ADD168.add16u_0RN(input1, input2)
        if obj1[53]['functions']['function'] == 'add16u_0EM':
            obj1[53]['functions']['write_data'] = ADD161.add16u_0EM(input1, input2)
        if obj1[53]['functions']['function'] == 'add16u_1JH':
            obj1[53]['functions']['write_data'] = ADD167.add16u_1JH(input1, input2)
        if obj1[53]['functions']['function'] == 'add16u_073':
            obj1[53]['functions']['write_data'] = ADD162.add16u_073(input1, input2)
        if obj1[53]['functions']['function'] == 'add16u_0M0':
            obj1[53]['functions']['write_data'] = ADD165.add16u_0M0(input1, input2)

        input1 = c1
        input2 = 28
        if obj1[54]['functions']['function'] == 'mul':
            obj1[54]['functions']['write_data'] = input1 * input2
        if obj1[54]['functions']['function'] == 'mul8u_Y48':
            obj1[54]['functions']['write_data'] = MUL1.mul8u_Y48(input1, input2)
        if obj1[54]['functions']['function'] == 'mul8u_150Q':
            obj1[54]['functions']['write_data'] = MUL2.mul8u_150Q(input1, input2)
        if obj1[54]['functions']['function'] == 'mul8u_2P7':
            obj1[54]['functions']['write_data'] = MUL6.mul8u_2P7(input1, input2)
        if obj1[54]['functions']['function'] == 'mul8u_KEM':
            obj1[54]['functions']['write_data'] = MUL8.mul8u_KEM(input1, input2)
        if obj1[54]['functions']['function'] == 'mul8u_CK5':
            obj1[54]['functions']['write_data'] = MUL7.mul8u_CK5(input1, input2)

        input1 = obj1[54]['functions']['write_data']
        input2 = obj1[53]['functions']['write_data']
        # print(input1,input2)
        if obj1[55]['functions']['function'] == 'add':
            obj1[55]['functions']['write_data'] = input1 + input2
        if obj1[55]['functions']['function'] == 'add16u_0RN':
            obj1[55]['functions']['write_data'] = ADD168.add16u_0RN(input1, input2)
        if obj1[55]['functions']['function'] == 'add16u_0EM':
            obj1[55]['functions']['write_data'] = ADD161.add16u_0EM(input1, input2)
        if obj1[55]['functions']['function'] == 'add16u_1JH':
            obj1[55]['functions']['write_data'] = ADD167.add16u_1JH(input1, input2)
        if obj1[55]['functions']['function'] == 'add16u_073':
            obj1[55]['functions']['write_data'] = ADD162.add16u_073(input1, input2)
        if obj1[55]['functions']['function'] == 'add16u_0M0':
            obj1[55]['functions']['write_data'] = ADD165.add16u_0M0(input1, input2)



        input1 = d1
        input2 = 24
        if obj1[56]['functions']['function'] == 'mul':
            obj1[56]['functions']['write_data'] = input1 * input2
        if obj1[56]['functions']['function'] == 'mul8u_Y48':
            obj1[56]['functions']['write_data'] = MUL1.mul8u_Y48(input1, input2)
        if obj1[56]['functions']['function'] == 'mul8u_150Q':
            obj1[56]['functions']['write_data'] = MUL2.mul8u_150Q(input1, input2)
        if obj1[56]['functions']['function'] == 'mul8u_2P7':
            obj1[56]['functions']['write_data'] = MUL6.mul8u_2P7(input1, input2)
        if obj1[56]['functions']['function'] == 'mul8u_KEM':
            obj1[56]['functions']['write_data'] = MUL8.mul8u_KEM(input1, input2)
        if obj1[56]['functions']['function'] == 'mul8u_CK5':
            obj1[56]['functions']['write_data'] = MUL7.mul8u_CK5(input1, input2)

        input1 = obj1[56]['functions']['write_data']
        input2 = 0
        if obj1[57]['functions']['function'] == 'add':
            obj1[57]['functions']['write_data'] = input1 + input2
        if obj1[57]['functions']['function'] == 'add16u_0RN':
            obj1[57]['functions']['write_data'] = ADD168.add16u_0RN(input1, input2)
        if obj1[57]['functions']['function'] == 'add16u_0EM':
            obj1[57]['functions']['write_data'] = ADD161.add16u_0EM(input1, input2)
        if obj1[57]['functions']['function'] == 'add16u_1JH':
            obj1[57]['functions']['write_data'] = ADD167.add16u_1JH(input1, input2)
        if obj1[57]['functions']['function'] == 'add16u_073':
            obj1[57]['functions']['write_data'] = ADD162.add16u_073(input1, input2)
        if obj1[57]['functions']['function'] == 'add16u_0M0':
            obj1[57]['functions']['write_data'] = ADD165.add16u_0M0(input1, input2)

        input1 = d1
        input2 = 19
        if obj1[58]['functions']['function'] == 'mul':
            obj1[58]['functions']['write_data'] = input1 * input2
        if obj1[58]['functions']['function'] == 'mul8u_Y48':
            obj1[58]['functions']['write_data'] = MUL1.mul8u_Y48(input1, input2)
        if obj1[58]['functions']['function'] == 'mul8u_150Q':
            obj1[58]['functions']['write_data'] = MUL2.mul8u_150Q(input1, input2)
        if obj1[58]['functions']['function'] == 'mul8u_2P7':
            obj1[58]['functions']['write_data'] = MUL6.mul8u_2P7(input1, input2)
        if obj1[58]['functions']['function'] == 'mul8u_KEM':
            obj1[58]['functions']['write_data'] = MUL8.mul8u_KEM(input1, input2)
        if obj1[58]['functions']['function'] == 'mul8u_CK5':
            obj1[58]['functions']['write_data'] = MUL7.mul8u_CK5(input1, input2)

        input1 = obj1[58]['functions']['write_data']
        input2 = obj1[57]['functions']['write_data']
        if obj1[59]['functions']['function'] == 'add':
            obj1[59]['functions']['write_data'] = input1 + input2
        if obj1[59]['functions']['function'] == 'add16u_0RN':
            obj1[59]['functions']['write_data'] = ADD168.add16u_0RN(input1, input2)
        if obj1[59]['functions']['function'] == 'add16u_0EM':
            obj1[59]['functions']['write_data'] = ADD161.add16u_0EM(input1, input2)
        if obj1[59]['functions']['function'] == 'add16u_1JH':
            obj1[59]['functions']['write_data'] = ADD167.add16u_1JH(input1, input2)
        if obj1[59]['functions']['function'] == 'add16u_073':
            obj1[59]['functions']['write_data'] = ADD162.add16u_073(input1, input2)
        if obj1[59]['functions']['function'] == 'add16u_0M0':
            obj1[59]['functions']['write_data'] = ADD165.add16u_0M0(input1, input2)

        input1 = d1
        input2 = 14
        if obj1[60]['functions']['function'] == 'mul':
            obj1[60]['functions']['write_data'] = input1 * input2
        if obj1[60]['functions']['function'] == 'mul8u_Y48':
            obj1[60]['functions']['write_data'] = MUL1.mul8u_Y48(input1, input2)
        if obj1[60]['functions']['function'] == 'mul8u_150Q':
            obj1[60]['functions']['write_data'] = MUL2.mul8u_150Q(input1, input2)
        if obj1[60]['functions']['function'] == 'mul8u_2P7':
            obj1[60]['functions']['write_data'] = MUL6.mul8u_2P7(input1, input2)
        if obj1[60]['functions']['function'] == 'mul8u_KEM':
            obj1[60]['functions']['write_data'] = MUL8.mul8u_KEM(input1, input2)
        if obj1[60]['functions']['function'] == 'mul8u_CK5':
            obj1[60]['functions']['write_data'] = MUL7.mul8u_CK5(input1, input2)

        input1 = obj1[60]['functions']['write_data']
        input2 = obj1[59]['functions']['write_data']
        if obj1[61]['functions']['function'] == 'add':
            obj1[61]['functions']['write_data'] = input1 + input2
        if obj1[61]['functions']['function'] == 'add16u_0RN':
            obj1[61]['functions']['write_data'] = ADD168.add16u_0RN(input1, input2)
        if obj1[61]['functions']['function'] == 'add16u_0EM':
            obj1[61]['functions']['write_data'] = ADD161.add16u_0EM(input1, input2)
        if obj1[61]['functions']['function'] == 'add16u_1JH':
            obj1[61]['functions']['write_data'] = ADD167.add16u_1JH(input1, input2)
        if obj1[61]['functions']['function'] == 'add16u_073':
            obj1[61]['functions']['write_data'] = ADD162.add16u_073(input1, input2)
        if obj1[61]['functions']['function'] == 'add16u_0M0':
            obj1[61]['functions']['write_data'] = ADD165.add16u_0M0(input1, input2)

        input1 = d1
        input2 = 10
        if obj1[62]['functions']['function'] == 'mul':
            obj1[62]['functions']['write_data'] = input1 * input2
        if obj1[62]['functions']['function'] == 'mul8u_Y48':
            obj1[62]['functions']['write_data'] = MUL1.mul8u_Y48(input1, input2)
        if obj1[62]['functions']['function'] == 'mul8u_150Q':
            obj1[62]['functions']['write_data'] = MUL2.mul8u_150Q(input1, input2)
        if obj1[62]['functions']['function'] == 'mul8u_2P7':
            obj1[62]['functions']['write_data'] = MUL6.mul8u_2P7(input1, input2)
        if obj1[62]['functions']['function'] == 'mul8u_KEM':
            obj1[62]['functions']['write_data'] = MUL8.mul8u_KEM(input1, input2)
        if obj1[62]['functions']['function'] == 'mul8u_CK5':
            obj1[62]['functions']['write_data'] = MUL7.mul8u_CK5(input1, input2)

        input1 = obj1[62]['functions']['write_data']
        input2 = obj1[61]['functions']['write_data']
        if obj1[63]['functions']['function'] == 'add':
            obj1[63]['functions']['write_data'] = input1 + input2
        if obj1[63]['functions']['function'] == 'add16u_0RN':
            obj1[63]['functions']['write_data'] = ADD168.add16u_0RN(input1, input2)
        if obj1[63]['functions']['function'] == 'add16u_0EM':
            obj1[63]['functions']['write_data'] = ADD161.add16u_0EM(input1, input2)
        if obj1[63]['functions']['function'] == 'add16u_1JH':
            obj1[63]['functions']['write_data'] = ADD167.add16u_1JH(input1, input2)
        if obj1[63]['functions']['function'] == 'add16u_073':
            obj1[63]['functions']['write_data'] = ADD162.add16u_073(input1, input2)
        if obj1[63]['functions']['function'] == 'add16u_0M0':
            obj1[63]['functions']['write_data'] = ADD165.add16u_0M0(input1, input2)






        x1 = a * 0 + a * 50 + a * 10 + a * 15
        x2 = b * 19 + b * 24 + b * 28 + b * 32
        x3 = c * 36 + c * 39 + c * 42 + c * 45
        x4 = d * 47 + d * 49 + d * 50 + d * 51
        x5 = a1 * 51 + a1 * 51 + a1 * 51 + a1 * 50
        x6 = b1 * 49 + b1 * 47 + b1 * 45 + b1 * 42
        x7 = c1 * 39 + c1 * 36 + c1 * 32 + c1 * 28
        x8 = d1 * 24 + d1 * 19 + d1 * 14 + d1 * 10
        ed1=obj1[63]['functions']['write_data']-x8
        ed2=obj1[55]['functions']['write_data']-x7
        ed3 = obj1[47]['functions']['write_data']-x6
        ed4=obj1[39]['functions']['write_data']-x5
        ed5=obj1[31]['functions']['write_data'] - x4
        ed6=obj1[23]['functions']['write_data'] - x3
        ed7=obj1[15]['functions']['write_data'] - x2
        ed8=obj1[7]['functions']['write_data'] - x1
        # MSE=(ed1-ed2-ed3-ed4-ed5-ed6-ed7-ed8)/8
        # psnr=10*math.log10((max1*max1)/MSE)
        sum.append(ed1)
        sum.append(ed2)
        sum.append(ed3)
        sum.append(ed4)
        sum.append(ed5)
        sum.append(ed6)
        sum.append(ed7)
        sum.append(ed8)
        # print(ed1,ed2,ed3,ed4,ed5,ed6,ed7,ed8)
    summ=0
    for o in range(0,len(sum)):
        summ=summ+abs(sum[o])
    MSE=summ/len(sum)
    if MSE==0:
        MSE=1
    # print(MSE)
    PSNR=10*math.log10((n2*n2)/MSE)
    # print(PSNR)
    return PSNR

if __name__ == '__main__':
    _list = DFGparsing.reg.search_order()
    obj1=_list
    psnr=dcterrorcomputing(obj1)
    print(psnr)

