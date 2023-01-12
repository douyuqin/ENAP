#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：demo_01
@File ：regular_matching.py
@Author ：sk
@Date ：2021/11/11 2:12 PM
'''
import DFGparsing
import GAChose
import Upperlimit
import Downlimit
import rank
import copy
import time
import random
import GAini
import GAcross
import GAmutation
from memory_profiler import profile


ii = 0
_list = DFGparsing.reg.search_order()
N=len(_list)
print('N',N)
MUL8LIP=['mul8u_Y48','mul8u_2P7','mul8u_KEM','mul8u_150Q','mul8u_CK5']
MUL8LIP_area=[390,386,370,360,345]
ADD16LIP=['add16u_0RN','add16u_0EM','add16u_1JH','add16u_073','add16u_0M0']
ADD16LIP_area=[60,57,51,43,36]
Area_ADD16JINQUE=72
Area_MUL8JINQUE=391
area=[0 for i in range(N)]
upresult=[0,0]
downresult=[0,0,0,0]

_list2=copy.deepcopy(_list)
_list4=copy.deepcopy(_list)
_list5=copy.deepcopy(_list)


for i in range(0,N):
    obj = _list[i]
    if obj['functions']['function'] == 'add':
       area[i]=Area_ADD16JINQUE
    if obj['functions']['function'] == 'mul':
       area[i]=Area_MUL8JINQUE

ERROR=5
area2=copy.deepcopy(area)
t1 = time.time()
# Upper bound estimation
(upresult,paixuMED)=Upperlimit.Upperlimit(_list,_list2,N,area,ERROR)
# Lower bound estimate
sadd=0
#Estimated power consumption for calculation
for i in range(0,N):
    sadd=sadd+(area2[i]-upresult[2][i])
downresult=Downlimit.Downlimit(sadd,_list5,N,_list2,_list4,upresult[0],ERROR)
print('Upperlimit',upresult[1])
print('Downlimit',downresult[0])


#
# upresult[1]=len(paixuMED[3])
# downresult[0]=4
# downresult[4]=4

# Produce O chromosomes
o=5
(randoms1,randoms2)=GAini.ini(_list,_list2,downresult,upresult,paixuMED,o)
# qq1=[[2],[2,5],[6],[1,3],[4,2,3]]
# qq2=[[1],[0,0],[1],[0,1],[0,0,0]]
# randoms1.append(qq1)
# randoms2.append(qq2)

z=3 # Number of crossover/mutation
(randoms1a,randoms2a)=GAcross.cross(_list,_list2,downresult,randoms1,randoms2,z,upresult)

(randoms1a,randoms2a)=GAmutation.mut(_list,_list2,downresult,randoms1a,randoms2a,z,upresult,paixuMED)

(randoms1a,randoms2b,sumsave1,sumsave1error)=GAChose.chose1(randoms1a,randoms2a,_list2,N,ERROR)

# Store the results in a file
file_handle = open('experiment/lapulasi5.txt', mode='w')
file_handle.write(str(randoms1a) + '\n')
file_handle.write(str(randoms2b) + '\n')
file_handle.write(str(sumsave1) + '\n')
file_handle.write(str(sumsave1error) + '\n')


for c in range(0,13):  # C refers to the number of iterations
    # The data change is used for the following calculation
    fuzhi1= copy.deepcopy(randoms1a)
    fuzhi2 = copy.deepcopy(randoms2b)
    randoms1=[]
    randoms2=[]
    for i in range(0,len(fuzhi1)):
        if (isinstance(fuzhi1[0][0], list)) == 1:
            if (isinstance(fuzhi1[0][0][0], list)) == 1:
                for a in range(0,len(isinstance(fuzhi1[i][j]))):
                    randoms1.append(fuzhi1[i][j][a])
                    randoms2.append(fuzhi2[i][j][a])
            else:
                for j in range(0,len(fuzhi1[i])):
                  if (isinstance(fuzhi1[i][j], list)) == 1:
                      randoms1.append(fuzhi1[i][j])
                      randoms2.append(fuzhi2[i][j])
        else:
              randoms1.append(fuzhi1[i])
              randoms2.append(fuzhi2[i])
    for i in range(0,len(randoms1)):
            if len(randoms1[i]) == 0:
                ss=[random.choice(paixuMED[3]),random.choice(paixuMED[3])]
                ss1 = [random.randint(0, 1), random.randint(0, 1)]
                randoms1[i].append(ss)
                randoms2[i].append(ss1)
    z = 10 # Number of crossover/mutation

    (randoms1a, randoms2a) = GAcross.cross(_list, _list2, downresult, randoms1, randoms2, z, upresult)

    (randoms1a, randoms2a) = GAmutation.mut1(_list, _list2, downresult, randoms1a, randoms2a, z, upresult, paixuMED)

    (randoms1a, randoms2b, sumsave1, sumsave1error) = GAChose.chose2(randoms1a, randoms2a, _list2, N, ERROR)
    print(randoms1a)
    print(randoms2b)
    print(sumsave1)
    print(sumsave1error)
    file_handle.write(str(randoms1a) + '\n')
    file_handle.write(str(randoms2b) + '\n')
    file_handle.write(str(sumsave1) + '\n')
    file_handle.write(str(sumsave1error) + '\n')

t1 = time.time()




