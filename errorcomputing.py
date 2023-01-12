
from ctypes import *
from numpy import *

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


def errorcomputing(_list,N,a,b):
        for i in range(0, N):
            # a = random.randint(1, 125)
            # b = random.randint(1, 125)
            obj = _list[i]
            if obj['depend_list'][0]== 2:
            # if obj['order'] == 2:
                if obj['functions']['function'] == 'add':
                    obj['functions']['write_data'] = a + b

                if obj['functions']['function'] == 'mul':
                    obj['functions']['write_data'] = a * b
                if obj['functions']['function'] == 'sub':
                    obj['functions']['write_data'] = a - b
                if obj['functions']['function'] == 'sll':
                    obj['functions']['write_data'] = a * obj['functions']['read'][1]
                    # print(obj['functions']['read'][1])

                # 近似单元计算部分
                if obj['functions']['function'] == 'add8u_5R3':
                    obj['functions']['write_data'] = ADD1.add8u_5R3(a, b)
                if obj['functions']['function'] == 'add8u_5SY':
                    obj['functions']['write_data'] = ADD2.add8u_5SY(a, b)
                if obj['functions']['function'] == 'add8u_006':
                    obj['functions']['write_data'] = ADD3.add8u_006(a, b)
                if obj['functions']['function'] == 'add8u_8ES':
                    obj['functions']['write_data'] = ADD4.add8u_8ES(a, b)
                if obj['functions']['function'] == 'add16u_0EM':
                    obj['functions']['write_data'] = ADD161.add16u_0EM(a, b)
                if obj['functions']['function'] == 'add16u_073':
                    obj['functions']['write_data'] = ADD162.add16u_073(a, b)
                if obj['functions']['function'] == 'add16u_00G':
                    obj['functions']['write_data'] = ADD163.add16u_00G(a, b)
                if obj['functions']['function'] == 'add16u_02E':
                    obj['functions']['write_data'] = ADD164.add16u_02E(a, b)
                if obj['functions']['function'] == 'add16u_0M0':
                    obj['functions']['write_data'] = ADD165.add16u_0M0(a, b)
                if obj['functions']['function'] == 'add16u_1E2':
                    obj['functions']['write_data'] = ADD166.add16u_1E2(a, b)
                if obj['functions']['function'] == 'add16u_1JH':
                    obj['functions']['write_data'] = ADD167.add16u_1JH(a, b)
                    # print(obj['functions']['write_data'])
                if obj['functions']['function'] == 'add16u_0RN':
                    obj['functions']['write_data'] = ADD168.add16u_0RN(a, b)

                if obj['functions']['function'] == 'add16se_1Y7':
                    obj['functions']['write_data'] = ADD169.add16se_1Y7(a, b)
                if obj['functions']['function'] == 'add16se_2JY':
                    obj['functions']['write_data'] = ADD170.add16se_2JY(a, b)
                if obj['functions']['function'] == 'add16se_20J':
                    obj['functions']['write_data'] = ADD171.add16se_20J(a, b)
                if obj['functions']['function'] == 'add16se_26Q':
                    obj['functions']['write_data'] = ADD172.add16se_26Q(a, b)
                if obj['functions']['function'] == 'add16se_2BY':
                    # print(55)
                    obj['functions']['write_data'] = ADD173.add16se_2BY(a, b)

                if obj['functions']['function'] == 'mul8u_Y48':
                    obj['functions']['write_data'] = MUL1.mul8u_Y48(a, b)
                if obj['functions']['function'] == 'mul8u_150Q':
                    obj['functions']['write_data'] = MUL2.mul8u_150Q(a, b)
                if obj['functions']['function'] == 'mul8u_185Q':
                    obj['functions']['write_data'] = MUL3.mul8u_185Q(a, b)
                if obj['functions']['function'] == 'mul8u_13QR':
                    obj['functions']['write_data'] = MUL4.mul8u_13QR(a, b)
                if obj['functions']['function'] == 'mul8u_2HH':
                    obj['functions']['write_data'] = MUL5.mul8u_2HH(a, b)
                if obj['functions']['function'] == 'mul8u_2P7':
                    obj['functions']['write_data'] = MUL6.mul8u_2P7(a, b)
                if obj['functions']['function'] == 'mul8u_CK5':
                    obj['functions']['write_data'] = MUL7.mul8u_CK5(a, b)
                if obj['functions']['function'] == 'mul8u_KEM':
                    obj['functions']['write_data'] = MUL8.mul8u_KEM(a, b)


            else:
                obj['functions']['write_data'] = 0

        for i in range(0, N):
            obj1 = _list[i]
            if (obj1['depend_list'][0]) > (2):
            # if (obj1['order']) > (2):
                for j in range(0, N):
                    obj2 = _list[j]
                    # 本段程序用于，第一个位置存储的不是有效变量，GAUT的一般情况是第二个位置放置非有效信息，即1
                    if obj1['depend_list'][0] == 3:
                      if obj1['functions']['read'][0] == obj2['functions']['write']:

                        for t in range(0, N):

                            obj3 = _list[t]
                            if obj1['functions']['read'][1] == obj3['functions']['write']:

                                if obj1['functions']['function'] == 'add':
                                    obj1['functions']['write_data'] = obj2['functions']['write_data'] + obj3['functions']['write_data']
                                    # print(obj1['functions']['write_data'])
                                    # print(obj2['functions']['write_data'])
                                if obj1['functions']['function'] == 'sra':

                                    obj1['functions']['write_data'] = obj2['functions']['write_data'] >> 4
                                    # print(obj1['functions']['write_data'])
                                if obj1['functions']['function'] == 'mul':
                                    obj1['functions']['write_data'] = obj2['functions']['write_data'] * obj3['functions'][
                                        'write_data']

                                if (obj1['functions']['function']) == 'sub':
                                    # print(obj2['functions']['write_data'])
                                    # print(obj3['functions']['write_data'])
                                    # print(obj1['functions']['function'])
                                    obj1['functions']['write_data'] = obj2['functions']['write_data'] - obj3['functions']['write_data']
                                    # print(obj1['functions']['write_data'])
                                if obj1['functions']['function'] == 'sll':
                                    obj1['functions']['write_data'] = obj2['functions']['write_data'] * obj['functions']['read'][1]
                                # 近似单元计算部分
                                if obj1['functions']['function'] == 'add8u_5R3':
                                    obj1['functions']['write_data'] = ADD1.add8u_5R3(obj2['functions']['write_data'],
                                                                                     obj3['functions']['write_data'])
                                if obj1['functions']['function'] == 'add8u_5SY':
                                    obj1['functions']['write_data'] = ADD2.add8u_5SY(obj2['functions']['write_data'],
                                                                                     obj3['functions']['write_data'])
                                if obj1['functions']['function'] == 'add8u_006':
                                    obj1['functions']['write_data'] = ADD3.add8u_006(obj2['functions']['write_data'],
                                                                                     obj3['functions']['write_data'])
                                if obj1['functions']['function'] == 'add8u_8ES':
                                    obj1['functions']['write_data'] = ADD4.add8u_8ES(obj2['functions']['write_data'],
                                                                                     obj3['functions']['write_data'])
                                if obj1['functions']['function'] == 'add16u_0EM':
                                    obj1['functions']['write_data'] = ADD161.add16u_0EM(obj2['functions']['write_data'],
                                                                                        obj3['functions']['write_data'])
                                if obj1['functions']['function'] == 'add16u_073':
                                    obj1['functions']['write_data'] = ADD162.add16u_073(obj2['functions']['write_data'],
                                                                                        obj3['functions']['write_data'])
                                if obj1['functions']['function'] == 'add16u_00G':
                                    obj1['functions']['write_data'] = ADD163.add16u_00G(obj2['functions']['write_data'],
                                                                                        obj3['functions']['write_data'])
                                if obj1['functions']['function'] == 'add16u_02E':
                                    obj1['functions']['write_data'] = ADD164.add16u_02E(obj2['functions']['write_data'],
                                                                                        obj3['functions']['write_data'])
                                if obj1['functions']['function'] == 'add16u_0M0':
                                    obj1['functions']['write_data'] = ADD165.add16u_0M0(obj2['functions']['write_data'],
                                                                                        obj3['functions']['write_data'])
                                if obj1['functions']['function'] == 'add16u_1E2':
                                    obj1['functions']['write_data'] = ADD166.add16u_1E2(obj2['functions']['write_data'],
                                                                                        obj3['functions']['write_data'])
                                if obj1['functions']['function'] == 'add16u_0RN':
                                    obj1['functions']['write_data'] = ADD168.add16u_0RN(obj2['functions']['write_data'],
                                                                                        obj3['functions']['write_data'])
                                if obj1['functions']['function'] == 'add16u_1JH':
                                    obj1['functions']['write_data'] = ADD167.add16u_1JH(obj2['functions']['write_data'],
                                                                                        obj3['functions']['write_data'])
                                if obj1['functions']['function'] == 'add16se_1Y7':
                                    obj1['functions']['write_data'] = ADD169.add16se_1Y7(obj2['functions']['write_data'],
                                                                                        obj3['functions']['write_data'])
                                if obj1['functions']['function'] == 'add16se_2JY':
                                    obj1['functions']['write_data'] = ADD170.add16se_2JY(obj2['functions']['write_data'],
                                                                                        obj3['functions']['write_data'])
                                if obj1['functions']['function'] == 'add16se_20J':
                                    obj1['functions']['write_data'] = ADD171.add16se_20J(obj2['functions']['write_data'],
                                                                                        obj3['functions']['write_data'])
                                if obj1['functions']['function'] == 'add16se_26Q':
                                    obj1['functions']['write_data'] = ADD172.add16se_26Q(obj2['functions']['write_data'],
                                                                                        obj3['functions']['write_data'])
                                if obj1['functions']['function'] == 'add16se_2BY':

                                    obj1['functions']['write_data'] = ADD173.add16se_2BY(obj2['functions']['write_data'],obj3['functions']['write_data'])
                                    # print(obj2['functions']['write_data'])
                                    # print(obj3['functions']['write_data'])
                                    # print(obj1['functions']['write_data'])

                                if obj1['functions']['function'] == 'mul8u_Y48':
                                    obj1['functions']['write_data'] = MUL1.mul8u_Y48(obj2['functions']['write_data'],


                                                                                     obj3['functions']['write_data'])
                                if obj1['functions']['function'] == 'mul8u_150Q':
                                    obj1['functions']['write_data'] = MUL2.mul8u_150Q(obj2['functions']['write_data'],
                                                                                      obj3['functions']['write_data'])
                                if obj1['functions']['function'] == 'mul8u_185Q':
                                    obj1['functions']['write_data'] = MUL3.mul8u_185Q(obj2['functions']['write_data'],
                                                                                      obj3['functions']['write_data'])
                                if obj1['functions']['function'] == 'mul8u_13QR':
                                    obj1['functions']['write_data'] = MUL4.mul8u_13QR(obj2['functions']['write_data'],
                                                                                      obj3['functions']['write_data'])
                                if obj1['functions']['function'] == 'mul8u_2HH':
                                    obj1['functions']['write_data'] = MUL5.mul8u_2HH(obj2['functions']['write_data'],
                                                                                      obj3['functions']['write_data'])
                                if obj1['functions']['function'] == 'mul8u_2P7':
                                    obj1['functions']['write_data'] = MUL6.mul8u_2P7(obj2['functions']['write_data'],
                                                                                      obj3['functions']['write_data'])
                                if obj1['functions']['function'] == 'mul8u_CK5':
                                    obj1['functions']['write_data'] = MUL7.mul8u_CK5(obj2['functions']['write_data'],
                                                                                      obj3['functions']['write_data'])
                                if obj1['functions']['function'] == 'mul8u_KEM':
                                    obj1['functions']['write_data'] = MUL8.mul8u_KEM(obj2['functions']['write_data'],
                                                                                      obj3['functions']['write_data'])



                                if obj1['functions']['write_data']>10000:
                                    obj1['functions']['write_data']=obj2['functions']['write_data']+obj3['functions']['write_data']





                            if obj1['depend_list'][1] == 1:
                                if obj1['functions']['function'] == 'add':
                                    obj1['functions']['write_data'] = int(obj2['functions']['write_data']) + a
                                if obj1['functions']['function'] == 'mul':
                                    obj1['functions']['write_data'] = obj2['functions']['write_data'] * a
                                if obj1['functions']['function'] == 'sub':
                                    obj1['functions']['write_data'] = obj2['functions']['write_data'] - a
                                if obj1['functions']['function'] == 'sll':
                                    obj1['functions']['write_data'] = obj2['functions']['write_data'] * obj['functions']['read'][1]
                                if obj1['functions']['function'] == 'sra':
                                   obj1['functions']['write_data'] = obj2['functions']['write_data'] >> obj['functions']['read'][1]
                                # 近似单元计算部分
                                if obj1['functions']['function'] == 'add8u_5R3':
                                    obj1['functions']['write_data'] = ADD1.add8u_5R3(obj2['functions']['write_data'], a)
                                if obj1['functions']['function'] == 'add8u_5SY':
                                    obj1['functions']['write_data'] = ADD2.add8u_5SY(obj2['functions']['write_data'], a)
                                if obj1['functions']['function'] == 'add8u_006':
                                    obj1['functions']['write_data'] = ADD3.add8u_006(obj2['functions']['write_data'], a)
                                if obj1['functions']['function'] == 'add8u_8ES':
                                    obj1['functions']['write_data'] = ADD4.add8u_8ES(obj2['functions']['write_data'], a)
                                if obj1['functions']['function'] == 'add16u_0EM':
                                    obj1['functions']['write_data'] = ADD161.add16u_0EM(obj2['functions']['write_data'],a)

                                if obj1['functions']['function'] == 'add16u_073':
                                    obj1['functions']['write_data'] = ADD162.add16u_073(obj2['functions']['write_data'], a)
                                if obj1['functions']['function'] == 'add16u_00G':
                                    obj1['functions']['write_data'] = ADD163.add16u_00G(obj2['functions']['write_data'], a)
                                if obj1['functions']['function'] == 'add16u_02E':
                                    obj1['functions']['write_data'] = ADD164.add16u_02E(obj2['functions']['write_data'], a)
                                if obj1['functions']['function'] == 'add16u_0M0':
                                    obj1['functions']['write_data'] = ADD165.add16u_0M0(obj2['functions']['write_data'], a)
                                if obj1['functions']['function'] == 'add16u_1E2':
                                    obj1['functions']['write_data'] = ADD166.add16u_1E2(obj2['functions']['write_data'], a)
                                if obj1['functions']['function'] == 'add16u_1JH':
                                    obj1['functions']['write_data'] = ADD167.add16u_1JH(obj2['functions']['write_data'], a)
                                if obj1['functions']['function'] == 'add16u_0RN':
                                    obj1['functions']['write_data'] = ADD168.add16u_0RN(obj2['functions']['write_data'], a)
                                if obj1['functions']['function'] == 'add16se_1Y7':
                                    obj1['functions']['write_data'] = ADD169.add16se_1Y7(obj2['functions']['write_data'],a)
                                if obj1['functions']['function'] == 'add16se_2JY':
                                    obj1['functions']['write_data'] = ADD170.add16se_2JY(obj2['functions']['write_data'],a)
                                if obj1['functions']['function'] == 'add16se_20J':
                                    obj1['functions']['write_data'] = ADD171.add16se_20J(obj2['functions']['write_data'],a)
                                if obj1['functions']['function'] == 'add16se_26Q':
                                    obj1['functions']['write_data'] = ADD172.add16se_26Q(obj2['functions']['write_data'],a)
                                if obj1['functions']['function'] == 'add16se_2BY':
                                    # print(77)
                                    obj1['functions']['write_data'] = ADD173.add16se_2BY(obj2['functions']['write_data'],a)

                                if obj1['functions']['function'] == 'mul8u_Y48':
                                    obj1['functions']['write_data'] = MUL1.mul8u_Y48(obj2['functions']['write_data'], a)
                                if obj1['functions']['function'] == 'mul8u_150Q':
                                    obj1['functions']['write_data'] = MUL2.mul8u_150Q(obj2['functions']['write_data'], a)
                                if obj1['functions']['function'] == 'mul8u_185Q':
                                    obj1['functions']['write_data'] = MUL3.mul8u_185Q(obj2['functions']['write_data'], a)
                                if obj1['functions']['function'] == 'mul8u_13QR':
                                    obj1['functions']['write_data'] = MUL4.mul8u_13QR(obj2['functions']['write_data'], a)
                                if obj1['functions']['function'] == 'mul8u_2HH':
                                    obj1['functions']['write_data'] = MUL5.mul8u_2HH(obj2['functions']['write_data'], a)
                                if obj1['functions']['function'] == 'mul8u_2P7':
                                    obj1['functions']['write_data'] = MUL6.mul8u_2P7(obj2['functions']['write_data'], a)
                                if obj1['functions']['function'] == 'mul8u_CK5':
                                    obj1['functions']['write_data'] = MUL7.mul8u_CK5(obj2['functions']['write_data'], a)
                                if obj1['functions']['function'] == 'mul8u_KEM':
                                    obj1['functions']['write_data'] = MUL8.mul8u_KEM(obj2['functions']['write_data'], a)

        e=obj['functions']['write_data']

        # print(e)
        return e
