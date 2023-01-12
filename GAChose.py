import copy

import GAmedcomputing

MUL8LIP=['mul8u_Y48','mul8u_2P7','mul8u_KEM','mul8u_150Q']
MUL8LIP_area=[390,386,370,360]
ADD16LIP=['add16u_0RN','add16u_0EM','add16u_1JH','add16u_073']
ADD16LIP_area=[60,57,51,43]
def chose1(randoms1a,randoms2a,_list2,N,ERROR):
    orderror1=[]
    orderror2=[]
    orderror=[]

    for i in range(0, len(randoms1a)):
        for j in range(0, len(randoms1a[i])):
            orderror1.append(randoms1a[i][j])
            orderror2.append(randoms2a[i][j])
            DAERROR = GAmedcomputing.GAerror(_list2, randoms1a[i][j], randoms2a[i][j],N)
            orderror.append(DAERROR)
    sumsave1=[]
    sumsave1error=[]
    errorsave=[]
    randoms1a=[]
    randoms2b=[]
    for u in range(0,len(orderror)):
        if orderror[u]<=ERROR:
            jisuanlist = copy.deepcopy(_list2)
            sumsave = 0
            for j in range(0,len(orderror1[u])):
                obj = jisuanlist[orderror1[u][j]]
                if (obj['functions']['function'] == 'add'):
                    sumsave=sumsave+(72-ADD16LIP_area[orderror2[u][j]])
                    obj['functions']['function'] = ADD16LIP[orderror2[u][j]]
                if (obj['functions']['function'] == 'mul'):
                    sumsave= sumsave + (391 - MUL8LIP_area[orderror2[u][j]])
                    obj['functions']['function'] = MUL8LIP[orderror2[u][j]]
            sumsave1.append(sumsave)
            sumsave1error.append(orderror[u])
            randoms1a.append(orderror1[u])
            randoms2b.append(orderror2[u])

            if len(sumsave1) >= 5 & (~(orderror[u] in sumsave1error)):
                for i in range(0, len(sumsave1)):
                    if sumsave > sumsave1[i]:
                        sumsave1[i] = sumsave
                        sumsave1error[i] = orderror[u]
                        randoms1a[i] = orderror1[u]
                        randoms2b[i] = orderror2[u]
                        break
                    if sumsave==sumsave1[i]:
                        if orderror[u] < sumsave1error[i]:
                            sumsave1[i] = sumsave
                            sumsave1error[i] = orderror[u]
                            randoms1a[i] = orderror1[u]
                            randoms2b[i] = orderror2[u]
                        break
            if (len(sumsave1) < 5) & (~(orderror[u] in sumsave1error)):
                sumsave1.append(sumsave)
                sumsave1error.append(orderror[u])
                randoms1a.append(orderror1[u])
                randoms2b.append(orderror2[u])

    if len(randoms1a) < 5:
        for u in range(0, len(orderror)):
            jisuanlist = copy.deepcopy(_list2)
            sumsave = 0
            for j in range(0, len(orderror1[u])):
                obj = jisuanlist[orderror1[u][j]]
                if (obj['functions']['function'] == 'add'):
                    sumsave = sumsave + (72 - ADD16LIP_area[orderror2[u][j]])
                    obj['functions']['function'] = ADD16LIP[orderror2[u][j]]
                if (obj['functions']['function'] == 'mul'):
                    sumsave = sumsave + (391 - MUL8LIP_area[orderror2[u][j]])
                    obj['functions']['function'] = MUL8LIP[orderror2[u][j]]
            if (len(sumsave1) < 5) & (~(orderror[u] in sumsave1error)):
                if (orderror[u] in sumsave1error):
                     print('true1')
                else:
                    sumsave1.append(sumsave)
                    sumsave1error.append(orderror[u])
                    randoms1a.append(orderror1[u])
                    randoms2b.append(orderror2[u])
            if len(sumsave1) >= 5 & ((orderror[u] in sumsave1error) < 0):
                if (orderror[u] in sumsave1error):
                     print('true2')
                else:
                    for i in range(0, len(sumsave1)): #保留错误较小的配置
                        if (sumsave > sumsave1[i])&(orderror[u]>sumsave1error[i]):
                            sumsave1[i] = sumsave
                            sumsave1error[i] = orderror[u]
                            randoms1a[i] = orderror1[u]
                            randoms2b[i] = orderror2[u]
                            break
                        if sumsave == sumsave1[i]:
                            if orderror[u] < sumsave1error[i]:
                                sumsave1[i] = sumsave
                                sumsave1error[i] = orderror[u]
                                randoms1a[i] = orderror1[u]
                                randoms2b[i] = orderror2[u]
                                break
    return randoms1a,randoms2b,sumsave1,sumsave1error



def chose2(randoms1a,randoms2a,_list2,N,ERROR):
    orderror1 = []
    orderror2 = []
    orderror = []
    for i in range(0, len(randoms1a)):
            orderror1.append(randoms1a[i])
            orderror2.append(randoms2a[i])
            DAERROR = GAmedcomputing.GAerror(_list2, randoms1a[i], randoms2a[i], N)
            orderror.append(DAERROR)
    sumsave1 = []
    sumsave1error = []
    errorsave = []
    randoms1a = []
    randoms2b = []
    for u in range(0, len(orderror)):
        if orderror[u] <= ERROR:
            jisuanlist = copy.deepcopy(_list2)
            sumsave = 0
            for j in range(0, len(orderror1[u])):
                obj = jisuanlist[orderror1[u][j]]
                if (obj['functions']['function'] == 'add'):
                    sumsave = sumsave + (72 - ADD16LIP_area[orderror2[u][j]])
                    obj['functions']['function'] = ADD16LIP[orderror2[u][j]]
                if (obj['functions']['function'] == 'mul'):
                    sumsave = sumsave + (391 - MUL8LIP_area[orderror2[u][j]])
                    obj['functions']['function'] = MUL8LIP[orderror2[u][j]]
            if (len(sumsave1) < 5) & (~(orderror[u] in sumsave1error)):
                sumsave1.append(sumsave)
                sumsave1error.append(orderror[u])
                randoms1a.append(orderror1[u])
                randoms2b.append(orderror2[u])
            if len(sumsave1) >= 5 & ((orderror[u] in sumsave1error)<0):
                if (orderror[u] in sumsave1error):
                   nn=0
                else:
                    for i in range(0, len(sumsave1)):
                        if sumsave > sumsave1[i]:
                            sumsave1[i] = sumsave
                            sumsave1error[i] = orderror[u]
                            randoms1a[i] = orderror1[u]
                            randoms2b[i] = orderror2[u]
                            break
                        if sumsave == sumsave1[i]:
                            if orderror[u] < sumsave1error[i]:
                                sumsave1[i] = sumsave
                                sumsave1error[i] = orderror[u]
                                randoms1a[i] = orderror1[u]
                                randoms2b[i] = orderror2[u]
                                break
    return randoms1a, randoms2b, sumsave1, sumsave1error
