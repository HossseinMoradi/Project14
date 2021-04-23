import math
import ast
from math import e
from decimal import *


getcontext().prec = 28

def flatten_list(_2d_list):
    flat_list = []
    # Iterate through the outer list
    for element in _2d_list:
        if type(element) is list:
            # If the element is of type list, iterate through the sublist
            for item in element:
                flat_list.append(item)
        else:
            flat_list.append(element)
    return flat_list

def permutation(lst):
    if len(lst) == 0:
        return []
    if len(lst) == 1:
        return [lst]

    l = []

    for i in range(len(lst)):
        m = lst[i]
        remLst = lst[:i] + lst[i + 1:]
        for p in permutation(remLst):
            l.append([m] + p)
    return l



def variance(data):
    n = len(data)
    if n!=0:
        mean = sum(data) / n
        deviations = [(x - mean) ** 2 for x in data]
        variance = sum(deviations) / n
    if n==0:
        variance=0
        
    return variance




def factorial(f):
    if f == 0:
        return 1
    else:
        return f * factorial(f - 1)


def toList(NestedTuple):
    return list(map(toList, NestedTuple)) if isinstance(NestedTuple, (list, tuple)) else NestedTuple


def Init():
    global vehTypesEquipped
    global vehTypesSpecial
    global vehsAttributes
    global vehsAttNames

    vehsAttributes = []
    vehsAttNames = []
    vehTypesAttributes = Vissim.Net.VehicleTypes.GetMultipleAttributes(['No', 'IsConnected', 'IsSpecial'])
    vehTypesEquipped = [x[0] for x in vehTypesAttributes if x[1] == True]
    vehTypesSpecial = [x[0] for x in vehTypesAttributes if x[2] == True]




def GetVissimDataVehicles():
    global vehsAttributes
    global vehsAttNames
    vehsAttributesNames = ['No', 'VehType\No', 'Pos', 'VehType\No', 'Lane\Link', 'Speed', 'DistanceToSigHead','InQueue']
    vehsAttributes = toList(Vissim.Net.Vehicles.GetMultipleAttributes(vehsAttributesNames))
    vehsAttNames = {}
    cnt = 0
    for att in vehsAttributesNames:
        vehsAttNames.update({att: cnt})
        cnt += 1
def GetSignalsData1():
    global SignalAttributes1
    global SigAttNames1
    SignalAttributes1 = []
    SigAttNames1 = []
    SignalAttributesNames1 = ['No','GreenStart', 'GreenEnd', 'IGT', 'SigState', 'GreenTimeDuration']
    SignalAttributes1 = toList(Vissim.Net.SignalControllers.ItemByKey(1).SGs.GetMultipleAttributes(SignalAttributesNames1))
    SigAttNames1 = {}
    ctt = 0
    for ftt in SignalAttributesNames1:
        SigAttNames1.update({ftt: ctt})
        ctt+=1

def GetSignalsData5():
    global SignalAttributes5
    global SigAttNames5
    SignalAttributes5 = []
    SigAttNames5 = []
    SignalAttributesNames5 = ['No','GreenStart', 'GreenEnd', 'IGT', 'SigState', 'GreenTimeDuration']
    SignalAttributes5 = toList(Vissim.Net.SignalControllers.ItemByKey(5).SGs.GetMultipleAttributes(SignalAttributesNames5))
    SigAttNames5 = {}
    ctt = 0
    for ftt in SignalAttributesNames5:
        SigAttNames5.update({ftt: ctt})
        ctt+=5


def GetSignalsData12():
    global SignalAttributes12
    global SigAttNames12
    SignalAttributes12 = []
    SigAttNames12 = []
    SignalAttributesNames12 = ['No','GreenStart', 'GreenEnd', 'IGT', 'SigState', 'GreenTimeDuration']
    SignalAttributes12 = toList(Vissim.Net.SignalControllers.ItemByKey(12).SGs.GetMultipleAttributes(SignalAttributesNames12))
    SigAttNames12 = {}
    ctt = 0
    for ftt in SignalAttributesNames12:
        SigAttNames12.update({ftt: ctt})
        ctt+=12

def GetSignalsData13():
    global SignalAttributes13
    global SigAttNames13
    SignalAttributes13 = []
    SigAttNames13 = []
    SignalAttributesNames13 = ['No','GreenStart', 'GreenEnd', 'IGT', 'SigState', 'GreenTimeDuration']
    SignalAttributes13 = toList(Vissim.Net.SignalControllers.ItemByKey(13).SGs.GetMultipleAttributes(SignalAttributesNames13))
    SigAttNames13 = {}
    ctt = 0
    for ftt in SignalAttributesNames13:
        SigAttNames13.update({ftt: ctt})
        ctt+=13




def GetSignalsData2():
    global SignalAttributes2
    global SigAttNames2
    SignalAttributes2 = []
    SigAttNames2 = []
    SignalAttributesNames2 = ['No','GreenStart', 'GreenEnd', 'IGT', 'SigState', 'GreenTimeDuration']
    SignalAttributes2 = toList(Vissim.Net.SignalControllers.ItemByKey(2).SGs.GetMultipleAttributes(SignalAttributesNames2))
    SigAttNames2 = {}
    ctt = 0
    for ftt in SignalAttributesNames2:
        SigAttNames2.update({ftt: ctt})
        ctt+=1


def GetSignalsData3():
    global SignalAttributes3
    global SigAttNames3
    SignalAttributes3 = []
    SigAttNames3 = []
    SignalAttributesNames3 = ['No','GreenStart', 'GreenEnd', 'IGT', 'SigState', 'GreenTimeDuration']
    SignalAttributes3 = toList(Vissim.Net.SignalControllers.ItemByKey(3).SGs.GetMultipleAttributes(SignalAttributesNames3))
    SigAttNames3 = {}
    ctt = 0
    for ftt in SignalAttributesNames3:
        SigAttNames3.update({ftt: ctt})
        ctt+=1



def GetSignalsData4():
    global SignalAttributes4
    global SigAttNames4
    SignalAttributes4 = []
    SigAttNames4 = []
    SignalAttributesNames4 = ['No','GreenStart', 'GreenEnd', 'IGT', 'SigState', 'GreenTimeDuration']
    SignalAttributes4 = toList(Vissim.Net.SignalControllers.ItemByKey(4).SGs.GetMultipleAttributes(SignalAttributesNames4))
    SigAttNames4 = {}
    ctt = 0
    for ftt in SignalAttributesNames4:
        SigAttNames4.update({ftt: ctt})
        ctt+=1


def GetSignalsData6():
    global SignalAttributes6
    global SigAttNames6
    SignalAttributes6 = []
    SigAttNames6 = []
    SignalAttributesNames6 = ['No','GreenStart', 'GreenEnd', 'IGT', 'SigState', 'GreenTimeDuration']
    SignalAttributes6 = toList(Vissim.Net.SignalControllers.ItemByKey(6).SGs.GetMultipleAttributes(SignalAttributesNames6))
    SigAttNames6 = {}
    ctt = 0
    for ftt in SignalAttributesNames6:
        SigAttNames6.update({ftt: ctt})
        ctt+=1


def GetSignalsData7():
    global SignalAttributes7
    global SigAttNames7
    SignalAttributes7 = []
    SigAttNames7 = []
    SignalAttributesNames7 = ['No','GreenStart', 'GreenEnd', 'IGT', 'SigState', 'GreenTimeDuration']
    SignalAttributes7 = toList(Vissim.Net.SignalControllers.ItemByKey(7).SGs.GetMultipleAttributes(SignalAttributesNames7))
    SigAttNames7 = {}
    ctt = 0
    for ftt in SignalAttributesNames7:
        SigAttNames7.update({ftt: ctt})
        ctt+=1


def GetSignalsData8():
    global SignalAttributes8
    global SigAttNames8
    SignalAttributes8 = []
    SigAttNames8 = []
    SignalAttributesNames8 = ['No','GreenStart', 'GreenEnd', 'IGT', 'SigState', 'GreenTimeDuration']
    SignalAttributes8 = toList(Vissim.Net.SignalControllers.ItemByKey(8).SGs.GetMultipleAttributes(SignalAttributesNames8))
    SigAttNames8 = {}
    ctt = 0
    for ftt in SignalAttributesNames8:
        SigAttNames8.update({ftt: ctt})
        ctt+=1

def GetSignalsData9():
    global SignalAttributes9
    global SigAttNames9
    SignalAttributes9 = []
    SigAttNames9 = []
    SignalAttributesNames9 = ['No','GreenStart', 'GreenEnd', 'IGT', 'SigState', 'GreenTimeDuration']
    SignalAttributes9 = toList(Vissim.Net.SignalControllers.ItemByKey(9).SGs.GetMultipleAttributes(SignalAttributesNames9))
    SigAttNames9 = {}
    ctt = 0
    for ftt in SignalAttributesNames9:
        SigAttNames9.update({ftt: ctt})
        ctt+=1

def GetSignalsData10():
    global SignalAttributes10
    global SigAttNames10
    SignalAttributes10 = []
    SigAttNames10 = []
    SignalAttributesNames10 = ['No','GreenStart', 'GreenEnd', 'IGT', 'SigState', 'GreenTimeDuration']
    SignalAttributes10 = toList(Vissim.Net.SignalControllers.ItemByKey(10).SGs.GetMultipleAttributes(SignalAttributesNames10))
    SigAttNames10 = {}
    ctt = 0
    for ftt in SignalAttributesNames10:
        SigAttNames10.update({ftt: ctt})
        ctt+=1

def GetSignalsData11():
    global SignalAttributes11
    global SigAttNames11
    SignalAttributes11 = []
    SigAttNames11 = []
    SignalAttributesNames11 = ['No','GreenStart', 'GreenEnd', 'IGT', 'SigState', 'GreenTimeDuration', 'ContrByCOM']
    SignalAttributes11 = toList(Vissim.Net.SignalControllers.ItemByKey(11).SGs.GetMultipleAttributes(SignalAttributesNames11))
    SigAttNames11 = {}
    ctt = 0
    for ftt in SignalAttributesNames11:
        SigAttNames11.update({ftt: ctt})
        ctt+=1


def GetLinksData():
    global LinkAttributes
    global LinAttNames
    LinkAttributes = []
    LinAttNames = []
    LinkAttributesNames = ['No','Count:Vehs']
    LinkAttributes = toList(Vissim.Net.Links.GetMultipleAttributes(LinkAttributesNames))
    LinAttNames = {}
    ppc = 0
    for ftt in LinkAttributesNames:
        LinAttNames.update({ftt: ppc})
        ppc+=1





def Density():
    GetLinksData()
    GetVissimDataVehicles()
    global density
    if Vissim.Net.SignalControllers.ItemByKey(1).AttValue ('CycSec')>3 and Vissim.Net.SignalControllers.ItemByKey(1).AttValue ('CycSec')<=4:
        kk=0
        for x in LinkAttributes:
            kk= kk + x[LinAttNames['Count:Vehs']]
        density = kk  - Vissim.Net.Links.ItemByKey(107).AttValue ('Count:Vehs') - Vissim.Net.Links.ItemByKey(108).AttValue ('Count:Vehs') - Vissim.Net.Links.ItemByKey(109).AttValue ('Count:Vehs')- Vissim.Net.Links.ItemByKey(110).AttValue ('Count:Vehs')- Vissim.Net.Links.ItemByKey(111).AttValue ('Count:Vehs')- Vissim.Net.Links.ItemByKey(112).AttValue ('Count:Vehs')- Vissim.Net.Links.ItemByKey(113).AttValue ('Count:Vehs')-- Vissim.Net.Links.ItemByKey(114).AttValue ('Count:Vehs')
        Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).SetAttValue ('Density', density)
        f= open("2.txt","a")
        f.write(","+str(density))
        f.write("\n")



def signals():
    CLength=80
    GetVissimDataVehicles()
    serivce=0.6

    proportion_of_CAVs=1

    Seconds = Vissim.Net.SignalControllers.ItemByKey(1).AttValue ('CycSec')

    ittearrival=10
    ittearrival2=80
    

    
    Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).SetAttValue('Seconds',Vissim.Net.Simulation.SimulationSecond)
    CySec = Vissim.Net.SignalControllers.ItemByKey(1).AttValue ('CycSec')
    SimSec = Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).AttValue('Seconds')




    if Seconds>6:

        f2 = open("Aseq.txt","r")  
        ggg = f2.readline()
        f2.close()
        Aseq= ast.literal_eval(ggg)






        if  Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(Aseq[0][0]).AttValue ('SigState') == 'GREEN':
            Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(Aseq[0][1]).SetAttValue ('SigState','RED')
            Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(Aseq[0][2]).SetAttValue ('SigState','RED')
            Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(Aseq[0][3]).SetAttValue ('SigState','RED')
            if Seconds >= Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(Aseq[0][0]).AttValue ('GreenEnd')-1:
                if Seconds <= Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(Aseq[0][0]).AttValue ('GreenEnd')+2:
                    Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(Aseq[0][0]).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(Aseq[0][1]).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(Aseq[0][2]).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(Aseq[0][3]).SetAttValue ('SigState','RED')


        if Seconds >= Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(Aseq[0][1]).AttValue ('GreenStart')-1:
            if Seconds <= Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(Aseq[0][1]).AttValue ('GreenEnd')-1:
                    Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(Aseq[0][0]).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(Aseq[0][1]).SetAttValue ('SigState','GREEN')
                    Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(Aseq[0][2]).SetAttValue ('SigState','GREEN')
                    Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(Aseq[0][3]).SetAttValue ('SigState','GREEN')



        if  Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(Aseq[0][1]).AttValue ('SigState') == 'GREEN':
            Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(Aseq[0][0]).SetAttValue ('SigState','RED')
            if Seconds >= Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(Aseq[0][1]).AttValue ('GreenEnd')-1:
                    Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(Aseq[0][0]).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(Aseq[0][1]).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(Aseq[0][2]).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(Aseq[0][3]).SetAttValue ('SigState','RED')





















        if  Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(Aseq[10][0]).AttValue ('SigState') == 'GREEN':
            Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(Aseq[10][1]).SetAttValue ('SigState','RED')
            Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(Aseq[10][2]).SetAttValue ('SigState','RED')
            Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(Aseq[10][3]).SetAttValue ('SigState','RED')
            if Seconds >= Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(Aseq[10][0]).AttValue ('GreenEnd')-1:
                if Seconds < Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(Aseq[10][0]).AttValue ('GreenEnd')+2:
                    Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(Aseq[10][1]).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(Aseq[10][0]).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(Aseq[10][2]).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(Aseq[10][3]).SetAttValue ('SigState','RED')





                    GI11=[[(CLength-12-Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(Aseq[10][0]).AttValue ('GreenTimeDuration'))/3,(CLength-12-Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(Aseq[10][0]).AttValue ('GreenTimeDuration'))/3,(CLength-12-Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(Aseq[10][0]).AttValue ('GreenTimeDuration'))/3], [(CLength-12-Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(Aseq[10][0]).AttValue ('GreenTimeDuration'))/4,(CLength-12-Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(Aseq[10][0]).AttValue ('GreenTimeDuration'))/4,(CLength-12-Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(Aseq[10][0]).AttValue ('GreenTimeDuration'))/2],[(CLength-12-Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(Aseq[10][0]).AttValue ('GreenTimeDuration'))/4,(CLength-12-Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(Aseq[10][0]).AttValue ('GreenTimeDuration'))/2,(CLength-12-Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(Aseq[10][0]).AttValue ('GreenTimeDuration'))/4],[(CLength-12-Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(Aseq[10][0]).AttValue ('GreenTimeDuration'))/5,3*(CLength-12-Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(Aseq[10][0]).AttValue ('GreenTimeDuration'))/5,(CLength-12-Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(Aseq[10][0]).AttValue ('GreenTimeDuration'))/5],[(CLength-12-Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(Aseq[10][0]).AttValue ('GreenTimeDuration'))/6,4*(CLength-12-Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(Aseq[10][0]).AttValue ('GreenTimeDuration'))/6,(CLength-12-Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(Aseq[10][0]).AttValue ('GreenTimeDuration'))/6],[(CLength-12-Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(Aseq[10][0]).AttValue ('GreenTimeDuration'))/7,5*(CLength-12-Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(Aseq[10][0]).AttValue ('GreenTimeDuration'))/7,(CLength-12-Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(Aseq[10][0]).AttValue ('GreenTimeDuration'))/7]]
                    indexI11=permutation([Aseq[10][1],Aseq[10][2],Aseq[10][3]])
                    grreenstrat11=[]
                    grreenenddd11=[]
                    for i in range(len(GI11)):
                        kokop=[]
                        kokop2=[]
                        for j in range(len(GI11[i])):
                            kokop.append([5+Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(Aseq[10][0]).AttValue ('GreenTimeDuration'), 8+Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(Aseq[10][0]).AttValue ('GreenTimeDuration')+GI11[i][j], 11+Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(Aseq[10][0]).AttValue ('GreenTimeDuration')+GI11[i][j ] +GI11[i][j-1]])
                            kokop2.append([5+Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(Aseq[10][0]).AttValue ('GreenTimeDuration')+GI11[i][j], 8+Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(Aseq[10][0]).AttValue ('GreenTimeDuration')+GI11[i][j-1] +GI11[i][j], 11+Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(Aseq[10][0]).AttValue ('GreenTimeDuration')+GI11[i][j ] +GI11[i][j-1]+GI11[i][j]])
                              
                        grreenstrat11.append(kokop)

                        grreenenddd11.append(kokop2)






                    ddst=[]
                    varices=[]
                    for i in grreenstrat11:
                        ddst1=[]
                        varices2=[]

                        for j in i:
                            ddst1.append(Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(Aseq[10][1]).AttValue ('distributionincapacity')+Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(Aseq[10][1]).AttValue ('ArrivalRate')*((j[0]-SimSec)/3600)-0.11*GI11[grreenstrat11.index(i)][0])
                            ddst1.append(Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(Aseq[10][2]).AttValue ('distributionincapacity')+Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(Aseq[10][2]).AttValue ('ArrivalRate')*((j[1]-SimSec)/3600)-0.11*GI11[grreenstrat11.index(i)][1])
                            ddst1.append(Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(Aseq[10][3]).AttValue ('distributionincapacity')+Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(Aseq[10][3]).AttValue ('ArrivalRate')*((j[2]-SimSec)/3600)-0.11*GI11[grreenstrat11.index(i)][2])
                            varices2.append(variance(ddst1))
                        ddst.append(ddst1)
                        varices.append(varices2)
                        



                    varices = flatten_list (varices)                    




                    ipip= int(math.floor(varices.index(min(varices))/3))
                    jpjp= int(varices.index(min(varices))- ipip*3)


                    Aseq[10][1]= indexI11[jpjp][0]
                    Aseq[10][2]= indexI11[jpjp][1]
                    Aseq[10][3]= indexI11[jpjp][2]

                    f2= open("Aseq.txt","w")
                    f2.write(str(Aseq))
                    f2.write("\n")
                    f2.close()






   
                    Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(Aseq[10][1]).SetAttValue('GreenTimeDuration',GI11[ipip][0])
                    Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(Aseq[10][2]).SetAttValue('GreenTimeDuration',GI11[ipip][1])
                    Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(Aseq[10][3]).SetAttValue('GreenTimeDuration',GI11[ipip][2])


     
                    Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(Aseq[10][1]).SetAttValue('GreenStart',grreenstrat11[ipip][jpjp][0])
                    Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(Aseq[10][2]).SetAttValue('GreenStart',grreenstrat11[ipip][jpjp][1])
                    Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(Aseq[10][3]).SetAttValue('GreenStart',grreenstrat11[ipip][jpjp][2])


    
                    Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(Aseq[10][1]).SetAttValue('GreenEnd',grreenenddd11[ipip][jpjp][0])
                    Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(Aseq[10][2]).SetAttValue('GreenEnd',grreenenddd11[ipip][jpjp][1])
                    Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(Aseq[10][3]).SetAttValue('GreenEnd',grreenenddd11[ipip][jpjp][2])



















        if Seconds >= Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(Aseq[10][1]).AttValue ('GreenStart')-1:
            if Seconds <= Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(Aseq[10][1]).AttValue ('GreenEnd')-1:
                    Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(Aseq[10][1]).SetAttValue ('SigState','GREEN')
                    Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(Aseq[10][0]).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(Aseq[10][2]).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(Aseq[10][3]).SetAttValue ('SigState','RED')


        if  Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(Aseq[10][1]).AttValue ('SigState') == 'GREEN':
            Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(Aseq[10][0]).SetAttValue ('SigState','RED')
            Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(Aseq[10][2]).SetAttValue ('SigState','RED')
            Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(Aseq[10][3]).SetAttValue ('SigState','RED')             
            if Seconds >= Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(Aseq[10][1]).AttValue ('GreenEnd')-1:
                if Seconds < Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(Aseq[10][1]).AttValue ('GreenEnd')+2:                 
                    Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(Aseq[10][2]).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(Aseq[10][0]).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(Aseq[10][1]).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(Aseq[10][3]).SetAttValue ('SigState','RED')




                    GI11=[[(CLength-12-Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(Aseq[10][0]).AttValue ('GreenTimeDuration')-Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(Aseq[10][1]).AttValue ('GreenTimeDuration'))/2,(CLength-12-Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(Aseq[10][0]).AttValue ('GreenTimeDuration')-Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(Aseq[10][1]).AttValue ('GreenTimeDuration'))/2],[2*(CLength-12-Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(Aseq[10][0]).AttValue ('GreenTimeDuration')-Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(Aseq[10][1]).AttValue ('GreenTimeDuration'))/3,(CLength-12-Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(Aseq[10][0]).AttValue ('GreenTimeDuration')-Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(Aseq[10][1]).AttValue ('GreenTimeDuration'))/3]]
                    indexI11=permutation([Aseq[10][2],Aseq[10][3]])
                    grreenstrat11=[]
                    grreenenddd11=[]
                    for i in range(len(GI11)):
                        kokop=[]
                        kokop2=[]
                        for j in range(len(GI11[i])):

                            kokop.append([8+Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(Aseq[10][0]).AttValue ('GreenTimeDuration') + Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(Aseq[10][0]).AttValue ('GreenTimeDuration'), 11+Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(Aseq[10][0]).AttValue ('GreenTimeDuration')+Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(Aseq[10][1]).AttValue ('GreenTimeDuration')+ GI11[i][j] ])
                            kokop2.append([8+Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(Aseq[10][0]).AttValue ('GreenTimeDuration') + Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(Aseq[10][0]).AttValue ('GreenTimeDuration') + GI11[i][j], 11+Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(Aseq[10][0]).AttValue ('GreenTimeDuration')+Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(Aseq[10][1]).AttValue ('GreenTimeDuration')+ GI11[i][j-1] + GI11[i][j]])

                              
                        grreenstrat11.append(kokop)

                        grreenenddd11.append(kokop2)





                    ddst=[]
                    varices=[]
                    for i in grreenstrat11:
                        ddst1=[]
                        varices2=[]

                        for j in i:
                            ddst1.append(Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(Aseq[10][2]).AttValue ('distributionincapacity')+Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(Aseq[10][2]).AttValue ('ArrivalRate')*((j[0]-SimSec)/3600)-0.11*GI11[grreenstrat11.index(i)][0])
                            ddst1.append(Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(Aseq[10][3]).AttValue ('distributionincapacity')+Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(Aseq[10][3]).AttValue ('ArrivalRate')*((j[1]-SimSec)/3600)-0.11*GI11[grreenstrat11.index(i)][1])
                            varices2.append(variance(ddst1))
                        ddst.append(ddst1)
                        varices.append(varices2)
                        

                    varices = flatten_list (varices)                    




                    ipip= int(math.floor(varices.index(min(varices))/2))
                    jpjp= int(varices.index(min(varices))- ipip*2)







                    Aseq[10][2]= indexI11[jpjp][0]
                    Aseq[10][3]= indexI11[jpjp][1]

                    f2= open("Aseq.txt","w")
                    f2.write(str(Aseq))
                    f2.write("\n")
                    f2.close()







   

                    Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(Aseq[10][2]).SetAttValue('GreenTimeDuration',GI11[ipip][0])
                    Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(Aseq[10][3]).SetAttValue('GreenTimeDuration',GI11[ipip][1])



                    Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(Aseq[10][2]).SetAttValue('GreenStart',grreenstrat11[ipip][jpjp][0])
                    Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(Aseq[10][3]).SetAttValue('GreenStart',grreenstrat11[ipip][jpjp][1])


    

                    Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(Aseq[10][2]).SetAttValue('GreenEnd',grreenenddd11[ipip][jpjp][0])
                    Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(Aseq[10][3]).SetAttValue('GreenEnd',grreenenddd11[ipip][jpjp][1])














        if Seconds >= Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(Aseq[10][2]).AttValue ('GreenStart')-1:
            if Seconds <= Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(Aseq[10][2]).AttValue ('GreenEnd')-1:
                    Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(Aseq[10][2]).SetAttValue ('SigState','GREEN')
                    Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(Aseq[10][0]).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(Aseq[10][1]).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(Aseq[10][3]).SetAttValue ('SigState','RED')


        if  Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(Aseq[10][2]).AttValue ('SigState') == 'GREEN':
            Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(Aseq[10][0]).SetAttValue ('SigState','RED')
            Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(Aseq[10][1]).SetAttValue ('SigState','RED')
            Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(Aseq[10][3]).SetAttValue ('SigState','RED') 
            if Seconds >= Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(Aseq[10][2]).AttValue ('GreenEnd')-1:
                if Seconds < Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(Aseq[10][2]).AttValue ('GreenEnd')+2:             
                    Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(Aseq[10][3]).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(Aseq[10][0]).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(Aseq[10][1]).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(Aseq[10][2]).SetAttValue ('SigState','RED')


        if Seconds >= Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(Aseq[10][3]).AttValue ('GreenStart')-1:
            if Seconds <= Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(Aseq[10][3]).AttValue ('GreenEnd')-1:
                    Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(Aseq[10][3]).SetAttValue ('SigState','GREEN')
                    Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(Aseq[10][0]).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(Aseq[10][1]).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(Aseq[10][2]).SetAttValue ('SigState','RED')


        if  Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(Aseq[10][3]).AttValue ('SigState') == 'GREEN':
            Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(Aseq[10][0]).SetAttValue ('SigState','RED')
            Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(Aseq[10][1]).SetAttValue ('SigState','RED')
            Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(Aseq[10][2]).SetAttValue ('SigState','RED')
            if Seconds >= Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(Aseq[10][3]).AttValue ('GreenEnd')-1:             
                    Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(Aseq[10][0]).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(Aseq[10][1]).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(Aseq[10][2]).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(Aseq[10][3]).SetAttValue ('SigState','RED')


                    GI11=[[(CLength-12)/4,(CLength-12)/4,(CLength-12)/4,(CLength-12)/4],[(CLength-12)/3,(CLength-12)/3,(CLength-12)/6,(CLength-12)/6],[(CLength-12)/3,(CLength-12)/3,(CLength-12)/6,(CLength-12)/6], [(CLength-12)/2,(CLength-12)/6,(CLength-12)/6,(CLength-12)/6],[(CLength-12)/4,(CLength-12)/4,(CLength-12)/4,(CLength-12)/4],[(CLength-12)/3,(CLength-12)/3,(CLength-12)/6,(CLength-12)/6],[(CLength-12)/3,(CLength-12)/3,(CLength-12)/6,(CLength-12)/6], [(CLength-12)/2,(CLength-12)/6,(CLength-12)/6,(CLength-12)/6],[(CLength-12)/4,(CLength-12)/4,(CLength-12)/4,(CLength-12)/4],[(CLength-12)/3,(CLength-12)/3,(CLength-12)/6,(CLength-12)/6],[(CLength-12)/3,(CLength-12)/3,(CLength-12)/6,(CLength-12)/6], [(CLength-12)/2,(CLength-12)/6,(CLength-12)/6,(CLength-12)/6],[(CLength-12)/4,(CLength-12)/4,(CLength-12)/4,(CLength-12)/4],[(CLength-12)/3,(CLength-12)/3,(CLength-12)/6,(CLength-12)/6],[(CLength-12)/3,(CLength-12)/3,(CLength-12)/6,(CLength-12)/6], [(CLength-12)/2,(CLength-12)/6,(CLength-12)/6,(CLength-12)/6],[(CLength-12)/4,(CLength-12)/4,(CLength-12)/4,(CLength-12)/4],[(CLength-12)/3,(CLength-12)/3,(CLength-12)/6,(CLength-12)/6],[(CLength-12)/3,(CLength-12)/3,(CLength-12)/6,(CLength-12)/6], [(CLength-12)/2,(CLength-12)/6,(CLength-12)/6,(CLength-12)/6],[(CLength-12)/4,(CLength-12)/4,(CLength-12)/4,(CLength-12)/4],[(CLength-12)/3,(CLength-12)/3,(CLength-12)/6,(CLength-12)/6],[(CLength-12)/3,(CLength-12)/3,(CLength-12)/6,(CLength-12)/6], [(CLength-12)/2,(CLength-12)/6,(CLength-12)/6,(CLength-12)/6]]
                    indexI11=permutation([Aseq[10][0],Aseq[10][1],Aseq[10][2],Aseq[10][3]])
                    grreenstrat11=[]
                    grreenenddd11=[]
                    for i in range(len(GI11)):
                        kokop=[]
                        kokop2=[]
                        for j in range(len(GI11[i])):
                            kokop.append([2, 5+GI11[i][j-3], 8+GI11[i][j-3]+GI11[i][j-2], 11+GI11[i][j-3]+GI11[i][j-2] +GI11[i][j-1]])
                            kokop2.append([2+GI11[i][j-3], 5+GI11[i][j-3]+GI11[i][j-2], 8+GI11[i][j-3]+GI11[i][j-2]+GI11[i][j-1], 11 +GI11[i][j-3]+GI11[i][j-2]+GI11[i][j-1] +GI11[i][j]])
 
                        grreenstrat11.append(kokop)
                        grreenenddd11.append(kokop2)




                    ddst=[]
                    varices=[]
                    for i in grreenstrat11:
                        ddst1=[]
                        varices2=[]

                        for j in i:
                            ddst1.append(Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(Aseq[10][0]).AttValue ('distributionincapacity')+Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(Aseq[10][0]).AttValue ('ArrivalRate')*((j[0]-SimSec)/3600)-0.11*GI11[grreenstrat11.index(i)][0])
                            ddst1.append(Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(Aseq[10][1]).AttValue ('distributionincapacity')+Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(Aseq[10][1]).AttValue ('ArrivalRate')*((j[1]-SimSec)/3600)-0.11*GI11[grreenstrat11.index(i)][1])
                            ddst1.append(Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(Aseq[10][2]).AttValue ('distributionincapacity')+Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(Aseq[10][2]).AttValue ('ArrivalRate')*((j[2]-SimSec)/3600)-0.11*GI11[grreenstrat11.index(i)][2])
                            ddst1.append(Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(Aseq[10][3]).AttValue ('distributionincapacity')+Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(Aseq[10][3]).AttValue ('ArrivalRate')*((j[3]-SimSec)/3600)-0.11*GI11[grreenstrat11.index(i)][3])
                            varices2.append(variance(ddst1))
                        ddst.append(ddst1)
                        varices.append(varices2)

                    varices = flatten_list (varices)                    




                    ipip= int(math.floor(varices.index(min(varices))/4))
                    jpjp= int(varices.index(min(varices))- ipip*4)






                    Aseq[10][0]= indexI11[jpjp][0]
                    Aseq[10][1]= indexI11[jpjp][1]
                    Aseq[10][2]= indexI11[jpjp][2]
                    Aseq[10][3]= indexI11[jpjp][3]

                    f2= open("Aseq.txt","w")
                    f2.write(str(Aseq))
                    f2.write("\n")
                    f2.close()



                    Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(Aseq[10][0]).SetAttValue('GreenTimeDuration',GI11[ipip][0])   
                    Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(Aseq[10][1]).SetAttValue('GreenTimeDuration',GI11[ipip][1])
                    Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(Aseq[10][2]).SetAttValue('GreenTimeDuration',GI11[ipip][2])
                    Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(Aseq[10][3]).SetAttValue('GreenTimeDuration',GI11[ipip][3])



                    Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(Aseq[10][0]).SetAttValue('GreenStart',grreenstrat11[ipip][jpjp][0])     
                    Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(Aseq[10][1]).SetAttValue('GreenStart',grreenstrat11[ipip][jpjp][1])
                    Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(Aseq[10][2]).SetAttValue('GreenStart',grreenstrat11[ipip][jpjp][2])
                    Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(Aseq[10][3]).SetAttValue('GreenStart',grreenstrat11[ipip][jpjp][3])


                    Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(Aseq[10][0]).SetAttValue('GreenEnd',grreenenddd11[ipip][jpjp][0])    
                    Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(Aseq[10][1]).SetAttValue('GreenEnd',grreenenddd11[ipip][jpjp][1])
                    Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(Aseq[10][2]).SetAttValue('GreenEnd',grreenenddd11[ipip][jpjp][2])
                    Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(Aseq[10][3]).SetAttValue('GreenEnd',grreenenddd11[ipip][jpjp][3])
















































        if  Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(Aseq[9][0]).AttValue ('SigState') == 'GREEN':
            Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(Aseq[9][1]).SetAttValue ('SigState','RED')
            Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(Aseq[9][2]).SetAttValue ('SigState','RED')
            Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(Aseq[9][3]).SetAttValue ('SigState','RED')
            if Seconds >= Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(Aseq[9][0]).AttValue ('GreenEnd')-1:
                if Seconds < Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(Aseq[9][0]).AttValue ('GreenEnd')+2:
                    Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(Aseq[9][1]).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(Aseq[9][0]).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(Aseq[9][2]).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(Aseq[9][3]).SetAttValue ('SigState','RED')


                    GI11=[[(CLength-12-Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(Aseq[9][0]).AttValue ('GreenTimeDuration'))/3,(CLength-12-Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(Aseq[9][0]).AttValue ('GreenTimeDuration'))/3,(CLength-12-Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(Aseq[9][0]).AttValue ('GreenTimeDuration'))/3], [(CLength-12-Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(Aseq[9][0]).AttValue ('GreenTimeDuration'))/4,(CLength-12-Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(Aseq[9][0]).AttValue ('GreenTimeDuration'))/4,(CLength-12-Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(Aseq[9][0]).AttValue ('GreenTimeDuration'))/2],[(CLength-12-Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(Aseq[9][0]).AttValue ('GreenTimeDuration'))/4,(CLength-12-Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(Aseq[9][0]).AttValue ('GreenTimeDuration'))/2,(CLength-12-Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(Aseq[9][0]).AttValue ('GreenTimeDuration'))/4],[(CLength-12-Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(Aseq[9][0]).AttValue ('GreenTimeDuration'))/5,3*(CLength-12-Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(Aseq[9][0]).AttValue ('GreenTimeDuration'))/5,(CLength-12-Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(Aseq[9][0]).AttValue ('GreenTimeDuration'))/5],[(CLength-12-Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(Aseq[9][0]).AttValue ('GreenTimeDuration'))/6,4*(CLength-12-Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(Aseq[9][0]).AttValue ('GreenTimeDuration'))/6,(CLength-12-Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(Aseq[9][0]).AttValue ('GreenTimeDuration'))/6],[(CLength-12-Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(Aseq[9][0]).AttValue ('GreenTimeDuration'))/7,5*(CLength-12-Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(Aseq[9][0]).AttValue ('GreenTimeDuration'))/7,(CLength-12-Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(Aseq[9][0]).AttValue ('GreenTimeDuration'))/7]]
                    indexI11=permutation([Aseq[9][1],Aseq[9][2],Aseq[9][3]])
                    grreenstrat11=[]
                    grreenenddd11=[]
                    for i in range(len(GI11)):
                        kokop=[]
                        kokop2=[]
                        for j in range(len(GI11[i])):
                            kokop.append([5+Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(Aseq[9][0]).AttValue ('GreenTimeDuration'), 8+Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(Aseq[9][0]).AttValue ('GreenTimeDuration')+GI11[i][j], 11+Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(Aseq[9][0]).AttValue ('GreenTimeDuration')+GI11[i][j ] +GI11[i][j-1]])
                            kokop2.append([5+Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(Aseq[9][0]).AttValue ('GreenTimeDuration')+GI11[i][j], 8+Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(Aseq[9][0]).AttValue ('GreenTimeDuration')+GI11[i][j-1] +GI11[i][j], 11+Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(Aseq[9][0]).AttValue ('GreenTimeDuration')+GI11[i][j ] +GI11[i][j-1]+GI11[i][j]])
                              
                        grreenstrat11.append(kokop)

                        grreenenddd11.append(kokop2)






                    ddst=[]
                    varices=[]
                    for i in grreenstrat11:
                        ddst1=[]
                        varices2=[]

                        for j in i:
                            ddst1.append(Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(Aseq[9][1]).AttValue ('distributionincapacity')+Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(Aseq[9][1]).AttValue ('ArrivalRate')*((j[0]-SimSec)/3600)-0.10*GI11[grreenstrat11.index(i)][0])
                            ddst1.append(Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(Aseq[9][2]).AttValue ('distributionincapacity')+Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(Aseq[9][2]).AttValue ('ArrivalRate')*((j[1]-SimSec)/3600)-0.10*GI11[grreenstrat11.index(i)][1])
                            ddst1.append(Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(Aseq[9][3]).AttValue ('distributionincapacity')+Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(Aseq[9][3]).AttValue ('ArrivalRate')*((j[2]-SimSec)/3600)-0.10*GI11[grreenstrat11.index(i)][2])
                            varices2.append(variance(ddst1))
                        ddst.append(ddst1)
                        varices.append(varices2)
                        



                    varices = flatten_list (varices)                    




                    ipip= int(math.floor(varices.index(min(varices))/3))
                    jpjp= int(varices.index(min(varices))- ipip*3)


                    Aseq[9][1]= indexI11[jpjp][0]
                    Aseq[9][2]= indexI11[jpjp][1]
                    Aseq[9][3]= indexI11[jpjp][2]

                    f2= open("Aseq.txt","w")
                    f2.write(str(Aseq))
                    f2.write("\n")
                    f2.close()






   
                    Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(Aseq[9][1]).SetAttValue('GreenTimeDuration',GI11[ipip][0])
                    Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(Aseq[9][2]).SetAttValue('GreenTimeDuration',GI11[ipip][1])
                    Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(Aseq[9][3]).SetAttValue('GreenTimeDuration',GI11[ipip][2])


     
                    Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(Aseq[9][1]).SetAttValue('GreenStart',grreenstrat11[ipip][jpjp][0])
                    Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(Aseq[9][2]).SetAttValue('GreenStart',grreenstrat11[ipip][jpjp][1])
                    Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(Aseq[9][3]).SetAttValue('GreenStart',grreenstrat11[ipip][jpjp][2])


    
                    Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(Aseq[9][1]).SetAttValue('GreenEnd',grreenenddd11[ipip][jpjp][0])
                    Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(Aseq[9][2]).SetAttValue('GreenEnd',grreenenddd11[ipip][jpjp][1])
                    Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(Aseq[9][3]).SetAttValue('GreenEnd',grreenenddd11[ipip][jpjp][2])












                        












        if Seconds >= Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(Aseq[9][1]).AttValue ('GreenStart')-1:
            if Seconds <= Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(Aseq[9][1]).AttValue ('GreenEnd')-1:
                    Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(Aseq[9][1]).SetAttValue ('SigState','GREEN')
                    Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(Aseq[9][0]).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(Aseq[9][2]).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(Aseq[9][3]).SetAttValue ('SigState','RED')


        if  Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(Aseq[9][1]).AttValue ('SigState') == 'GREEN':
            Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(Aseq[9][0]).SetAttValue ('SigState','RED')
            Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(Aseq[9][2]).SetAttValue ('SigState','RED')
            Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(Aseq[9][3]).SetAttValue ('SigState','RED')             
            if Seconds >= Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(Aseq[9][1]).AttValue ('GreenEnd')-1:
                if Seconds < Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(Aseq[9][1]).AttValue ('GreenEnd')+2:                 
                    Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(Aseq[9][2]).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(Aseq[9][0]).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(Aseq[9][1]).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(Aseq[9][3]).SetAttValue ('SigState','RED')






                    GI11=[[(CLength-12-Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(Aseq[9][0]).AttValue ('GreenTimeDuration')-Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(Aseq[9][1]).AttValue ('GreenTimeDuration'))/2,(CLength-12-Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(Aseq[9][0]).AttValue ('GreenTimeDuration')-Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(Aseq[9][1]).AttValue ('GreenTimeDuration'))/2],[2*(CLength-12-Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(Aseq[9][0]).AttValue ('GreenTimeDuration')-Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(Aseq[9][1]).AttValue ('GreenTimeDuration'))/3,(CLength-12-Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(Aseq[9][0]).AttValue ('GreenTimeDuration')-Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(Aseq[9][1]).AttValue ('GreenTimeDuration'))/3]]
                    indexI11=permutation([Aseq[9][2],Aseq[9][3]])
                    grreenstrat11=[]
                    grreenenddd11=[]
                    for i in range(len(GI11)):
                        kokop=[]
                        kokop2=[]
                        for j in range(len(GI11[i])):

                            kokop.append([8+Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(Aseq[9][0]).AttValue ('GreenTimeDuration') + Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(Aseq[9][0]).AttValue ('GreenTimeDuration'), 11+Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(Aseq[9][0]).AttValue ('GreenTimeDuration')+Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(Aseq[9][1]).AttValue ('GreenTimeDuration')+ GI11[i][j] ])
                            kokop2.append([8+Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(Aseq[9][0]).AttValue ('GreenTimeDuration') + Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(Aseq[9][0]).AttValue ('GreenTimeDuration') + GI11[i][j], 11+Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(Aseq[9][0]).AttValue ('GreenTimeDuration')+Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(Aseq[9][1]).AttValue ('GreenTimeDuration')+ GI11[i][j-1] + GI11[i][j]])

                              
                        grreenstrat11.append(kokop)

                        grreenenddd11.append(kokop2)





                    ddst=[]
                    varices=[]
                    for i in grreenstrat11:
                        ddst1=[]
                        varices2=[]

                        for j in i:
                            ddst1.append(Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(Aseq[9][2]).AttValue ('distributionincapacity')+Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(Aseq[9][2]).AttValue ('ArrivalRate')*((j[0]-SimSec)/3600)-0.10*GI11[grreenstrat11.index(i)][0])
                            ddst1.append(Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(Aseq[9][3]).AttValue ('distributionincapacity')+Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(Aseq[9][3]).AttValue ('ArrivalRate')*((j[1]-SimSec)/3600)-0.10*GI11[grreenstrat11.index(i)][1])
                            varices2.append(variance(ddst1))
                        ddst.append(ddst1)
                        varices.append(varices2)
                        

                    varices = flatten_list (varices)                    




                    ipip= int(math.floor(varices.index(min(varices))/2))
                    jpjp= int(varices.index(min(varices))- ipip*2)







                    Aseq[9][2]= indexI11[jpjp][0]
                    Aseq[9][3]= indexI11[jpjp][1]

                    f2= open("Aseq.txt","w")
                    f2.write(str(Aseq))
                    f2.write("\n")
                    f2.close()







   

                    Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(Aseq[9][2]).SetAttValue('GreenTimeDuration',GI11[ipip][0])
                    Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(Aseq[9][3]).SetAttValue('GreenTimeDuration',GI11[ipip][1])



                    Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(Aseq[9][2]).SetAttValue('GreenStart',grreenstrat11[ipip][jpjp][0])
                    Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(Aseq[9][3]).SetAttValue('GreenStart',grreenstrat11[ipip][jpjp][1])


    

                    Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(Aseq[9][2]).SetAttValue('GreenEnd',grreenenddd11[ipip][jpjp][0])
                    Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(Aseq[9][3]).SetAttValue('GreenEnd',grreenenddd11[ipip][jpjp][1])










     









        if Seconds >= Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(Aseq[9][2]).AttValue ('GreenStart')-1:
            if Seconds <= Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(Aseq[9][2]).AttValue ('GreenEnd')-1:
                    Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(Aseq[9][2]).SetAttValue ('SigState','GREEN')
                    Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(Aseq[9][0]).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(Aseq[9][1]).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(Aseq[9][3]).SetAttValue ('SigState','RED')


        if  Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(Aseq[9][2]).AttValue ('SigState') == 'GREEN':
            Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(Aseq[9][0]).SetAttValue ('SigState','RED')
            Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(Aseq[9][1]).SetAttValue ('SigState','RED')
            Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(Aseq[9][3]).SetAttValue ('SigState','RED') 
            if Seconds >= Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(Aseq[9][2]).AttValue ('GreenEnd')-1:
                if Seconds < Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(Aseq[9][2]).AttValue ('GreenEnd')+2:             
                    Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(Aseq[9][3]).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(Aseq[9][0]).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(Aseq[9][1]).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(Aseq[9][2]).SetAttValue ('SigState','RED')




        if Seconds >= Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(Aseq[9][3]).AttValue ('GreenStart')-1:
            if Seconds <= Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(Aseq[9][3]).AttValue ('GreenEnd')-1:
                    Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(Aseq[9][3]).SetAttValue ('SigState','GREEN')
                    Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(Aseq[9][0]).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(Aseq[9][1]).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(Aseq[9][2]).SetAttValue ('SigState','RED')


        if  Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(Aseq[9][3]).AttValue ('SigState') == 'GREEN':
            Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(Aseq[9][0]).SetAttValue ('SigState','RED')
            Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(Aseq[9][1]).SetAttValue ('SigState','RED')
            Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(Aseq[9][2]).SetAttValue ('SigState','RED')
            if Seconds >= Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(Aseq[9][3]).AttValue ('GreenEnd')-2:             
                    Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(Aseq[9][0]).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(Aseq[9][1]).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(Aseq[9][2]).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(Aseq[9][3]).SetAttValue ('SigState','RED')







                    GI11=[[(CLength-12)/4,(CLength-12)/4,(CLength-12)/4,(CLength-12)/4],[(CLength-12)/3,(CLength-12)/3,(CLength-12)/6,(CLength-12)/6],[(CLength-12)/3,(CLength-12)/3,(CLength-12)/6,(CLength-12)/6], [(CLength-12)/2,(CLength-12)/6,(CLength-12)/6,(CLength-12)/6],[(CLength-12)/4,(CLength-12)/4,(CLength-12)/4,(CLength-12)/4],[(CLength-12)/3,(CLength-12)/3,(CLength-12)/6,(CLength-12)/6],[(CLength-12)/3,(CLength-12)/3,(CLength-12)/6,(CLength-12)/6], [(CLength-12)/2,(CLength-12)/6,(CLength-12)/6,(CLength-12)/6],[(CLength-12)/4,(CLength-12)/4,(CLength-12)/4,(CLength-12)/4],[(CLength-12)/3,(CLength-12)/3,(CLength-12)/6,(CLength-12)/6],[(CLength-12)/3,(CLength-12)/3,(CLength-12)/6,(CLength-12)/6], [(CLength-12)/2,(CLength-12)/6,(CLength-12)/6,(CLength-12)/6],[(CLength-12)/4,(CLength-12)/4,(CLength-12)/4,(CLength-12)/4],[(CLength-12)/3,(CLength-12)/3,(CLength-12)/6,(CLength-12)/6],[(CLength-12)/3,(CLength-12)/3,(CLength-12)/6,(CLength-12)/6], [(CLength-12)/2,(CLength-12)/6,(CLength-12)/6,(CLength-12)/6],[(CLength-12)/4,(CLength-12)/4,(CLength-12)/4,(CLength-12)/4],[(CLength-12)/3,(CLength-12)/3,(CLength-12)/6,(CLength-12)/6],[(CLength-12)/3,(CLength-12)/3,(CLength-12)/6,(CLength-12)/6], [(CLength-12)/2,(CLength-12)/6,(CLength-12)/6,(CLength-12)/6],[(CLength-12)/4,(CLength-12)/4,(CLength-12)/4,(CLength-12)/4],[(CLength-12)/3,(CLength-12)/3,(CLength-12)/6,(CLength-12)/6],[(CLength-12)/3,(CLength-12)/3,(CLength-12)/6,(CLength-12)/6], [(CLength-12)/2,(CLength-12)/6,(CLength-12)/6,(CLength-12)/6]]
                    indexI11=permutation([Aseq[9][0],Aseq[9][1],Aseq[9][2],Aseq[9][3]])
                    grreenstrat11=[]
                    grreenenddd11=[]
                    for i in range(len(GI11)):
                        kokop=[]
                        kokop2=[]
                        for j in range(len(GI11[i])):
                            kokop.append([2, 5+GI11[i][j-3], 8+GI11[i][j-3]+GI11[i][j-2], 11+GI11[i][j-3]+GI11[i][j-2] +GI11[i][j-1]])
                            kokop2.append([2+GI11[i][j-3], 5+GI11[i][j-3]+GI11[i][j-2], 8+GI11[i][j-3]+GI11[i][j-2]+GI11[i][j-1], 11 +GI11[i][j-3]+GI11[i][j-2]+GI11[i][j-1] +GI11[i][j]])
 
                        grreenstrat11.append(kokop)
                        grreenenddd11.append(kokop2)




                    ddst=[]
                    varices=[]
                    for i in grreenstrat11:
                        ddst1=[]
                        varices2=[]

                        for j in i:
                            ddst1.append(Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(Aseq[9][0]).AttValue ('distributionincapacity')+Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(Aseq[9][0]).AttValue ('ArrivalRate')*((j[0]-SimSec)/3600)-0.10*GI11[grreenstrat11.index(i)][0])
                            ddst1.append(Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(Aseq[9][1]).AttValue ('distributionincapacity')+Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(Aseq[9][1]).AttValue ('ArrivalRate')*((j[1]-SimSec)/3600)-0.10*GI11[grreenstrat11.index(i)][1])
                            ddst1.append(Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(Aseq[9][2]).AttValue ('distributionincapacity')+Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(Aseq[9][2]).AttValue ('ArrivalRate')*((j[2]-SimSec)/3600)-0.10*GI11[grreenstrat11.index(i)][2])
                            ddst1.append(Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(Aseq[9][3]).AttValue ('distributionincapacity')+Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(Aseq[9][3]).AttValue ('ArrivalRate')*((j[3]-SimSec)/3600)-0.10*GI11[grreenstrat11.index(i)][3])
                            varices2.append(variance(ddst1))
                        ddst.append(ddst1)
                        varices.append(varices2)

                    varices = flatten_list (varices)                    




                    ipip= int(math.floor(varices.index(min(varices))/4))
                    jpjp= int(varices.index(min(varices))- ipip*4)






                    Aseq[9][0]= indexI11[jpjp][0]
                    Aseq[9][1]= indexI11[jpjp][1]
                    Aseq[9][2]= indexI11[jpjp][2]
                    Aseq[9][3]= indexI11[jpjp][3]

                    f2= open("Aseq.txt","w")
                    f2.write(str(Aseq))
                    f2.write("\n")
                    f2.close()



                    Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(Aseq[9][0]).SetAttValue('GreenTimeDuration',GI11[ipip][0])   
                    Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(Aseq[9][1]).SetAttValue('GreenTimeDuration',GI11[ipip][1])
                    Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(Aseq[9][2]).SetAttValue('GreenTimeDuration',GI11[ipip][2])
                    Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(Aseq[9][3]).SetAttValue('GreenTimeDuration',GI11[ipip][3])



                    Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(Aseq[9][0]).SetAttValue('GreenStart',grreenstrat11[ipip][jpjp][0])     
                    Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(Aseq[9][1]).SetAttValue('GreenStart',grreenstrat11[ipip][jpjp][1])
                    Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(Aseq[9][2]).SetAttValue('GreenStart',grreenstrat11[ipip][jpjp][2])
                    Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(Aseq[9][3]).SetAttValue('GreenStart',grreenstrat11[ipip][jpjp][3])


                    Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(Aseq[9][0]).SetAttValue('GreenEnd',grreenenddd11[ipip][jpjp][0])    
                    Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(Aseq[9][1]).SetAttValue('GreenEnd',grreenenddd11[ipip][jpjp][1])
                    Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(Aseq[9][2]).SetAttValue('GreenEnd',grreenenddd11[ipip][jpjp][2])
                    Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(Aseq[9][3]).SetAttValue('GreenEnd',grreenenddd11[ipip][jpjp][3])









                        






























































        if  Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(Aseq[8][0]).AttValue ('SigState') == 'GREEN':
            Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(Aseq[8][1]).SetAttValue ('SigState','RED')
            Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(Aseq[8][2]).SetAttValue ('SigState','RED')
            Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(Aseq[8][3]).SetAttValue ('SigState','RED')
            if Seconds >= Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(Aseq[8][0]).AttValue ('GreenEnd')-1:
                if Seconds < Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(Aseq[8][0]).AttValue ('GreenEnd')+2:
                    Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(Aseq[8][1]).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(Aseq[8][0]).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(Aseq[8][2]).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(Aseq[8][3]).SetAttValue ('SigState','RED')



                    GI11=[[(CLength-12-Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(Aseq[8][0]).AttValue ('GreenTimeDuration'))/3,(CLength-12-Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(Aseq[8][0]).AttValue ('GreenTimeDuration'))/3,(CLength-12-Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(Aseq[8][0]).AttValue ('GreenTimeDuration'))/3], [(CLength-12-Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(Aseq[8][0]).AttValue ('GreenTimeDuration'))/4,(CLength-12-Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(Aseq[8][0]).AttValue ('GreenTimeDuration'))/4,(CLength-12-Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(Aseq[8][0]).AttValue ('GreenTimeDuration'))/2],[(CLength-12-Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(Aseq[8][0]).AttValue ('GreenTimeDuration'))/4,(CLength-12-Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(Aseq[8][0]).AttValue ('GreenTimeDuration'))/2,(CLength-12-Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(Aseq[8][0]).AttValue ('GreenTimeDuration'))/4],[(CLength-12-Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(Aseq[8][0]).AttValue ('GreenTimeDuration'))/5,3*(CLength-12-Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(Aseq[8][0]).AttValue ('GreenTimeDuration'))/5,(CLength-12-Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(Aseq[8][0]).AttValue ('GreenTimeDuration'))/5],[(CLength-12-Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(Aseq[8][0]).AttValue ('GreenTimeDuration'))/6,4*(CLength-12-Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(Aseq[8][0]).AttValue ('GreenTimeDuration'))/6,(CLength-12-Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(Aseq[8][0]).AttValue ('GreenTimeDuration'))/6],[(CLength-12-Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(Aseq[8][0]).AttValue ('GreenTimeDuration'))/7,5*(CLength-12-Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(Aseq[8][0]).AttValue ('GreenTimeDuration'))/7,(CLength-12-Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(Aseq[8][0]).AttValue ('GreenTimeDuration'))/7]]
                    indexI11=permutation([Aseq[8][1],Aseq[8][2],Aseq[8][3]])
                    grreenstrat11=[]
                    grreenenddd11=[]
                    for i in range(len(GI11)):
                        kokop=[]
                        kokop2=[]
                        for j in range(len(GI11[i])):
                            kokop.append([5+Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(Aseq[8][0]).AttValue ('GreenTimeDuration'), 8+Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(Aseq[8][0]).AttValue ('GreenTimeDuration')+GI11[i][j], 11+Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(Aseq[8][0]).AttValue ('GreenTimeDuration')+GI11[i][j ] +GI11[i][j-1]])
                            kokop2.append([5+Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(Aseq[8][0]).AttValue ('GreenTimeDuration')+GI11[i][j], 8+Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(Aseq[8][0]).AttValue ('GreenTimeDuration')+GI11[i][j-1] +GI11[i][j], 11+Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(Aseq[8][0]).AttValue ('GreenTimeDuration')+GI11[i][j ] +GI11[i][j-1]+GI11[i][j]])
                              
                        grreenstrat11.append(kokop)

                        grreenenddd11.append(kokop2)






                    ddst=[]
                    varices=[]
                    for i in grreenstrat11:
                        ddst1=[]
                        varices2=[]

                        for j in i:
                            ddst1.append(Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(Aseq[8][1]).AttValue ('distributionincapacity')+Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(Aseq[8][1]).AttValue ('ArrivalRate')*((j[0]-SimSec)/3600)-0.9*GI11[grreenstrat11.index(i)][0])
                            ddst1.append(Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(Aseq[8][2]).AttValue ('distributionincapacity')+Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(Aseq[8][2]).AttValue ('ArrivalRate')*((j[1]-SimSec)/3600)-0.9*GI11[grreenstrat11.index(i)][1])
                            ddst1.append(Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(Aseq[8][3]).AttValue ('distributionincapacity')+Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(Aseq[8][3]).AttValue ('ArrivalRate')*((j[2]-SimSec)/3600)-0.9*GI11[grreenstrat11.index(i)][2])
                            varices2.append(variance(ddst1))
                        ddst.append(ddst1)
                        varices.append(varices2)
                        



                    varices = flatten_list (varices)                    




                    ipip= int(math.floor(varices.index(min(varices))/3))
                    jpjp= int(varices.index(min(varices))- ipip*3)


                    Aseq[8][1]= indexI11[jpjp][0]
                    Aseq[8][2]= indexI11[jpjp][1]
                    Aseq[8][3]= indexI11[jpjp][2]

                    f2= open("Aseq.txt","w")
                    f2.write(str(Aseq))
                    f2.write("\n")
                    f2.close()






   
                    Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(Aseq[8][1]).SetAttValue('GreenTimeDuration',GI11[ipip][0])
                    Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(Aseq[8][2]).SetAttValue('GreenTimeDuration',GI11[ipip][1])
                    Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(Aseq[8][3]).SetAttValue('GreenTimeDuration',GI11[ipip][2])


     
                    Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(Aseq[8][1]).SetAttValue('GreenStart',grreenstrat11[ipip][jpjp][0])
                    Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(Aseq[8][2]).SetAttValue('GreenStart',grreenstrat11[ipip][jpjp][1])
                    Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(Aseq[8][3]).SetAttValue('GreenStart',grreenstrat11[ipip][jpjp][2])


    
                    Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(Aseq[8][1]).SetAttValue('GreenEnd',grreenenddd11[ipip][jpjp][0])
                    Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(Aseq[8][2]).SetAttValue('GreenEnd',grreenenddd11[ipip][jpjp][1])
                    Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(Aseq[8][3]).SetAttValue('GreenEnd',grreenenddd11[ipip][jpjp][2])
























        if Seconds >= Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(Aseq[8][1]).AttValue ('GreenStart')-1:
            if Seconds <= Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(Aseq[8][1]).AttValue ('GreenEnd')-1:
                    Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(Aseq[8][1]).SetAttValue ('SigState','GREEN')
                    Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(Aseq[8][0]).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(Aseq[8][2]).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(Aseq[8][3]).SetAttValue ('SigState','RED')










        if  Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(Aseq[8][1]).AttValue ('SigState') == 'GREEN':
            Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(Aseq[8][0]).SetAttValue ('SigState','RED')
            Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(Aseq[8][2]).SetAttValue ('SigState','RED')
            Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(Aseq[8][3]).SetAttValue ('SigState','RED')             
            if Seconds >= Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(Aseq[8][1]).AttValue ('GreenEnd')-1:
                if Seconds < Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(Aseq[8][1]).AttValue ('GreenEnd')+2:                 
                    Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(Aseq[8][2]).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(Aseq[8][0]).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(Aseq[8][1]).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(Aseq[8][3]).SetAttValue ('SigState','RED')



                    GI11=[[(CLength-12-Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(Aseq[8][0]).AttValue ('GreenTimeDuration')-Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(Aseq[8][1]).AttValue ('GreenTimeDuration'))/2,(CLength-12-Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(Aseq[8][0]).AttValue ('GreenTimeDuration')-Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(Aseq[8][1]).AttValue ('GreenTimeDuration'))/2],[2*(CLength-12-Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(Aseq[8][0]).AttValue ('GreenTimeDuration')-Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(Aseq[8][1]).AttValue ('GreenTimeDuration'))/3,(CLength-12-Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(Aseq[8][0]).AttValue ('GreenTimeDuration')-Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(Aseq[8][1]).AttValue ('GreenTimeDuration'))/3]]
                    indexI11=permutation([Aseq[8][2],Aseq[8][3]])
                    grreenstrat11=[]
                    grreenenddd11=[]
                    for i in range(len(GI11)):
                        kokop=[]
                        kokop2=[]
                        for j in range(len(GI11[i])):

                            kokop.append([8+Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(Aseq[8][0]).AttValue ('GreenTimeDuration') + Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(Aseq[8][0]).AttValue ('GreenTimeDuration'), 11+Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(Aseq[8][0]).AttValue ('GreenTimeDuration')+Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(Aseq[8][1]).AttValue ('GreenTimeDuration')+ GI11[i][j] ])
                            kokop2.append([8+Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(Aseq[8][0]).AttValue ('GreenTimeDuration') + Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(Aseq[8][0]).AttValue ('GreenTimeDuration') + GI11[i][j], 11+Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(Aseq[8][0]).AttValue ('GreenTimeDuration')+Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(Aseq[8][1]).AttValue ('GreenTimeDuration')+ GI11[i][j-1] + GI11[i][j]])

                              
                        grreenstrat11.append(kokop)

                        grreenenddd11.append(kokop2)





                    ddst=[]
                    varices=[]
                    for i in grreenstrat11:
                        ddst1=[]
                        varices2=[]

                        for j in i:
                            ddst1.append(Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(Aseq[8][2]).AttValue ('distributionincapacity')+Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(Aseq[8][2]).AttValue ('ArrivalRate')*((j[0]-SimSec)/3600)-0.9*GI11[grreenstrat11.index(i)][0])
                            ddst1.append(Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(Aseq[8][3]).AttValue ('distributionincapacity')+Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(Aseq[8][3]).AttValue ('ArrivalRate')*((j[1]-SimSec)/3600)-0.9*GI11[grreenstrat11.index(i)][1])
                            varices2.append(variance(ddst1))
                        ddst.append(ddst1)
                        varices.append(varices2)
                        

                    varices = flatten_list (varices)                    




                    ipip= int(math.floor(varices.index(min(varices))/2))
                    jpjp= int(varices.index(min(varices))- ipip*2)







                    Aseq[8][2]= indexI11[jpjp][0]
                    Aseq[8][3]= indexI11[jpjp][1]

                    f2= open("Aseq.txt","w")
                    f2.write(str(Aseq))
                    f2.write("\n")
                    f2.close()







   

                    Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(Aseq[8][2]).SetAttValue('GreenTimeDuration',GI11[ipip][0])
                    Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(Aseq[8][3]).SetAttValue('GreenTimeDuration',GI11[ipip][1])



                    Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(Aseq[8][2]).SetAttValue('GreenStart',grreenstrat11[ipip][jpjp][0])
                    Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(Aseq[8][3]).SetAttValue('GreenStart',grreenstrat11[ipip][jpjp][1])


    

                    Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(Aseq[8][2]).SetAttValue('GreenEnd',grreenenddd11[ipip][jpjp][0])
                    Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(Aseq[8][3]).SetAttValue('GreenEnd',grreenenddd11[ipip][jpjp][1])







        if Seconds >= Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(Aseq[8][2]).AttValue ('GreenStart')-1:
            if Seconds <= Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(Aseq[8][2]).AttValue ('GreenEnd')-1:
                    Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(Aseq[8][2]).SetAttValue ('SigState','GREEN')
                    Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(Aseq[8][0]).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(Aseq[8][1]).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(Aseq[8][3]).SetAttValue ('SigState','RED')


        if  Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(Aseq[8][2]).AttValue ('SigState') == 'GREEN':
            Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(Aseq[8][0]).SetAttValue ('SigState','RED')
            Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(Aseq[8][1]).SetAttValue ('SigState','RED')
            Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(Aseq[8][3]).SetAttValue ('SigState','RED') 
            if Seconds >= Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(Aseq[8][2]).AttValue ('GreenEnd')-1:
                if Seconds < Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(Aseq[8][2]).AttValue ('GreenEnd')+2:             
                    Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(Aseq[8][3]).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(Aseq[8][0]).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(Aseq[8][1]).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(Aseq[8][2]).SetAttValue ('SigState','RED')


        if Seconds >= Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(Aseq[8][3]).AttValue ('GreenStart')-1:
            if Seconds <= Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(Aseq[8][3]).AttValue ('GreenEnd')-1:
                    Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(Aseq[8][3]).SetAttValue ('SigState','GREEN')
                    Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(Aseq[8][0]).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(Aseq[8][1]).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(Aseq[8][2]).SetAttValue ('SigState','RED')


        if  Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(Aseq[8][3]).AttValue ('SigState') == 'GREEN':
            Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(Aseq[8][0]).SetAttValue ('SigState','RED')
            Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(Aseq[8][1]).SetAttValue ('SigState','RED')
            Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(Aseq[8][2]).SetAttValue ('SigState','RED')
            if Seconds >= Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(Aseq[8][3]).AttValue ('GreenEnd')-1:             
                    Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(Aseq[8][0]).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(Aseq[8][1]).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(Aseq[8][2]).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(Aseq[8][3]).SetAttValue ('SigState','RED')



                    GI11=[[(CLength-12)/4,(CLength-12)/4,(CLength-12)/4,(CLength-12)/4],[(CLength-12)/3,(CLength-12)/3,(CLength-12)/6,(CLength-12)/6],[(CLength-12)/3,(CLength-12)/3,(CLength-12)/6,(CLength-12)/6], [(CLength-12)/2,(CLength-12)/6,(CLength-12)/6,(CLength-12)/6],[(CLength-12)/4,(CLength-12)/4,(CLength-12)/4,(CLength-12)/4],[(CLength-12)/3,(CLength-12)/3,(CLength-12)/6,(CLength-12)/6],[(CLength-12)/3,(CLength-12)/3,(CLength-12)/6,(CLength-12)/6], [(CLength-12)/2,(CLength-12)/6,(CLength-12)/6,(CLength-12)/6],[(CLength-12)/4,(CLength-12)/4,(CLength-12)/4,(CLength-12)/4],[(CLength-12)/3,(CLength-12)/3,(CLength-12)/6,(CLength-12)/6],[(CLength-12)/3,(CLength-12)/3,(CLength-12)/6,(CLength-12)/6], [(CLength-12)/2,(CLength-12)/6,(CLength-12)/6,(CLength-12)/6],[(CLength-12)/4,(CLength-12)/4,(CLength-12)/4,(CLength-12)/4],[(CLength-12)/3,(CLength-12)/3,(CLength-12)/6,(CLength-12)/6],[(CLength-12)/3,(CLength-12)/3,(CLength-12)/6,(CLength-12)/6], [(CLength-12)/2,(CLength-12)/6,(CLength-12)/6,(CLength-12)/6],[(CLength-12)/4,(CLength-12)/4,(CLength-12)/4,(CLength-12)/4],[(CLength-12)/3,(CLength-12)/3,(CLength-12)/6,(CLength-12)/6],[(CLength-12)/3,(CLength-12)/3,(CLength-12)/6,(CLength-12)/6], [(CLength-12)/2,(CLength-12)/6,(CLength-12)/6,(CLength-12)/6],[(CLength-12)/4,(CLength-12)/4,(CLength-12)/4,(CLength-12)/4],[(CLength-12)/3,(CLength-12)/3,(CLength-12)/6,(CLength-12)/6],[(CLength-12)/3,(CLength-12)/3,(CLength-12)/6,(CLength-12)/6], [(CLength-12)/2,(CLength-12)/6,(CLength-12)/6,(CLength-12)/6]]
                    indexI11=permutation([Aseq[8][0],Aseq[8][1],Aseq[8][2],Aseq[8][3]])
                    grreenstrat11=[]
                    grreenenddd11=[]
                    for i in range(len(GI11)):
                        kokop=[]
                        kokop2=[]
                        for j in range(len(GI11[i])):
                            kokop.append([2, 5+GI11[i][j-3], 8+GI11[i][j-3]+GI11[i][j-2], 11+GI11[i][j-3]+GI11[i][j-2] +GI11[i][j-1]])
                            kokop2.append([2+GI11[i][j-3], 5+GI11[i][j-3]+GI11[i][j-2], 8+GI11[i][j-3]+GI11[i][j-2]+GI11[i][j-1], 11 +GI11[i][j-3]+GI11[i][j-2]+GI11[i][j-1] +GI11[i][j]])
 
                        grreenstrat11.append(kokop)
                        grreenenddd11.append(kokop2)




                    ddst=[]
                    varices=[]
                    for i in grreenstrat11:
                        ddst1=[]
                        varices2=[]

                        for j in i:
                            ddst1.append(Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(Aseq[8][0]).AttValue ('distributionincapacity')+Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(Aseq[8][0]).AttValue ('ArrivalRate')*((j[0]-SimSec)/3600)-0.9*GI11[grreenstrat11.index(i)][0])
                            ddst1.append(Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(Aseq[8][1]).AttValue ('distributionincapacity')+Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(Aseq[8][1]).AttValue ('ArrivalRate')*((j[1]-SimSec)/3600)-0.9*GI11[grreenstrat11.index(i)][1])
                            ddst1.append(Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(Aseq[8][2]).AttValue ('distributionincapacity')+Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(Aseq[8][2]).AttValue ('ArrivalRate')*((j[2]-SimSec)/3600)-0.9*GI11[grreenstrat11.index(i)][2])
                            ddst1.append(Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(Aseq[8][3]).AttValue ('distributionincapacity')+Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(Aseq[8][3]).AttValue ('ArrivalRate')*((j[3]-SimSec)/3600)-0.9*GI11[grreenstrat11.index(i)][3])
                            varices2.append(variance(ddst1))
                        ddst.append(ddst1)
                        varices.append(varices2)

                    varices = flatten_list (varices)                    




                    ipip= int(math.floor(varices.index(min(varices))/4))
                    jpjp= int(varices.index(min(varices))- ipip*4)






                    Aseq[8][0]= indexI11[jpjp][0]
                    Aseq[8][1]= indexI11[jpjp][1]
                    Aseq[8][2]= indexI11[jpjp][2]
                    Aseq[8][3]= indexI11[jpjp][3]

                    f2= open("Aseq.txt","w")
                    f2.write(str(Aseq))
                    f2.write("\n")
                    f2.close()



                    Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(Aseq[8][0]).SetAttValue('GreenTimeDuration',GI11[ipip][0])   
                    Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(Aseq[8][1]).SetAttValue('GreenTimeDuration',GI11[ipip][1])
                    Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(Aseq[8][2]).SetAttValue('GreenTimeDuration',GI11[ipip][2])
                    Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(Aseq[8][3]).SetAttValue('GreenTimeDuration',GI11[ipip][3])



                    Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(Aseq[8][0]).SetAttValue('GreenStart',grreenstrat11[ipip][jpjp][0])     
                    Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(Aseq[8][1]).SetAttValue('GreenStart',grreenstrat11[ipip][jpjp][1])
                    Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(Aseq[8][2]).SetAttValue('GreenStart',grreenstrat11[ipip][jpjp][2])
                    Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(Aseq[8][3]).SetAttValue('GreenStart',grreenstrat11[ipip][jpjp][3])


                    Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(Aseq[8][0]).SetAttValue('GreenEnd',grreenenddd11[ipip][jpjp][0])    
                    Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(Aseq[8][1]).SetAttValue('GreenEnd',grreenenddd11[ipip][jpjp][1])
                    Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(Aseq[8][2]).SetAttValue('GreenEnd',grreenenddd11[ipip][jpjp][2])
                    Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(Aseq[8][3]).SetAttValue('GreenEnd',grreenenddd11[ipip][jpjp][3])





























































        if  Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(Aseq[7][0]).AttValue ('SigState') == 'GREEN':
            Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(Aseq[7][1]).SetAttValue ('SigState','RED')
            Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(Aseq[7][2]).SetAttValue ('SigState','RED')
            Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(Aseq[7][3]).SetAttValue ('SigState','RED')
            if Seconds >= Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(Aseq[7][0]).AttValue ('GreenEnd')-1:
                if Seconds < Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(Aseq[7][0]).AttValue ('GreenEnd')+2:
                    Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(Aseq[7][1]).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(Aseq[7][0]).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(Aseq[7][2]).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(Aseq[7][3]).SetAttValue ('SigState','RED')


                    GI11=[[(CLength-12-Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(Aseq[7][0]).AttValue ('GreenTimeDuration'))/3,(CLength-12-Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(Aseq[7][0]).AttValue ('GreenTimeDuration'))/3,(CLength-12-Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(Aseq[7][0]).AttValue ('GreenTimeDuration'))/3], [(CLength-12-Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(Aseq[7][0]).AttValue ('GreenTimeDuration'))/4,(CLength-12-Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(Aseq[7][0]).AttValue ('GreenTimeDuration'))/4,(CLength-12-Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(Aseq[7][0]).AttValue ('GreenTimeDuration'))/2],[(CLength-12-Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(Aseq[7][0]).AttValue ('GreenTimeDuration'))/4,(CLength-12-Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(Aseq[7][0]).AttValue ('GreenTimeDuration'))/2,(CLength-12-Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(Aseq[7][0]).AttValue ('GreenTimeDuration'))/4],[(CLength-12-Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(Aseq[7][0]).AttValue ('GreenTimeDuration'))/5,3*(CLength-12-Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(Aseq[7][0]).AttValue ('GreenTimeDuration'))/5,(CLength-12-Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(Aseq[7][0]).AttValue ('GreenTimeDuration'))/5],[(CLength-12-Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(Aseq[7][0]).AttValue ('GreenTimeDuration'))/6,4*(CLength-12-Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(Aseq[7][0]).AttValue ('GreenTimeDuration'))/6,(CLength-12-Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(Aseq[7][0]).AttValue ('GreenTimeDuration'))/6],[(CLength-12-Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(Aseq[7][0]).AttValue ('GreenTimeDuration'))/7,5*(CLength-12-Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(Aseq[7][0]).AttValue ('GreenTimeDuration'))/7,(CLength-12-Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(Aseq[7][0]).AttValue ('GreenTimeDuration'))/7]]
                    indexI11=permutation([Aseq[7][1],Aseq[7][2],Aseq[7][3]])
                    grreenstrat11=[]
                    grreenenddd11=[]
                    for i in range(len(GI11)):
                        kokop=[]
                        kokop2=[]
                        for j in range(len(GI11[i])):
                            kokop.append([5+Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(Aseq[7][0]).AttValue ('GreenTimeDuration'), 8+Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(Aseq[7][0]).AttValue ('GreenTimeDuration')+GI11[i][j], 11+Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(Aseq[7][0]).AttValue ('GreenTimeDuration')+GI11[i][j ] +GI11[i][j-1]])
                            kokop2.append([5+Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(Aseq[7][0]).AttValue ('GreenTimeDuration')+GI11[i][j], 8+Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(Aseq[7][0]).AttValue ('GreenTimeDuration')+GI11[i][j-1] +GI11[i][j], 11+Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(Aseq[7][0]).AttValue ('GreenTimeDuration')+GI11[i][j ] +GI11[i][j-1]+GI11[i][j]])
                              
                        grreenstrat11.append(kokop)

                        grreenenddd11.append(kokop2)






                    ddst=[]
                    varices=[]
                    for i in grreenstrat11:
                        ddst1=[]
                        varices2=[]

                        for j in i:
                            ddst1.append(Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(Aseq[7][1]).AttValue ('distributionincapacity')+Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(Aseq[7][1]).AttValue ('ArrivalRate')*((j[0]-SimSec)/3600)-0.8*GI11[grreenstrat11.index(i)][0])
                            ddst1.append(Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(Aseq[7][2]).AttValue ('distributionincapacity')+Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(Aseq[7][2]).AttValue ('ArrivalRate')*((j[1]-SimSec)/3600)-0.8*GI11[grreenstrat11.index(i)][1])
                            ddst1.append(Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(Aseq[7][3]).AttValue ('distributionincapacity')+Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(Aseq[7][3]).AttValue ('ArrivalRate')*((j[2]-SimSec)/3600)-0.8*GI11[grreenstrat11.index(i)][2])
                            varices2.append(variance(ddst1))
                        ddst.append(ddst1)
                        varices.append(varices2)
                        



                    varices = flatten_list (varices)                    




                    ipip= int(math.floor(varices.index(min(varices))/3))
                    jpjp= int(varices.index(min(varices))- ipip*3)


                    Aseq[7][1]= indexI11[jpjp][0]
                    Aseq[7][2]= indexI11[jpjp][1]
                    Aseq[7][3]= indexI11[jpjp][2]

                    f2= open("Aseq.txt","w")
                    f2.write(str(Aseq))
                    f2.write("\n")
                    f2.close()






   
                    Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(Aseq[7][1]).SetAttValue('GreenTimeDuration',GI11[ipip][0])
                    Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(Aseq[7][2]).SetAttValue('GreenTimeDuration',GI11[ipip][1])
                    Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(Aseq[7][3]).SetAttValue('GreenTimeDuration',GI11[ipip][2])


     
                    Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(Aseq[7][1]).SetAttValue('GreenStart',grreenstrat11[ipip][jpjp][0])
                    Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(Aseq[7][2]).SetAttValue('GreenStart',grreenstrat11[ipip][jpjp][1])
                    Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(Aseq[7][3]).SetAttValue('GreenStart',grreenstrat11[ipip][jpjp][2])


    
                    Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(Aseq[7][1]).SetAttValue('GreenEnd',grreenenddd11[ipip][jpjp][0])
                    Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(Aseq[7][2]).SetAttValue('GreenEnd',grreenenddd11[ipip][jpjp][1])
                    Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(Aseq[7][3]).SetAttValue('GreenEnd',grreenenddd11[ipip][jpjp][2])








        if Seconds >= Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(Aseq[7][1]).AttValue ('GreenStart')-1:
            if Seconds <= Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(Aseq[7][1]).AttValue ('GreenEnd')-1:
                    Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(Aseq[7][1]).SetAttValue ('SigState','GREEN')
                    Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(Aseq[7][0]).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(Aseq[7][2]).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(Aseq[7][3]).SetAttValue ('SigState','RED')


        if  Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(Aseq[7][1]).AttValue ('SigState') == 'GREEN':
            Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(Aseq[7][0]).SetAttValue ('SigState','RED')
            Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(Aseq[7][2]).SetAttValue ('SigState','RED')
            Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(Aseq[7][3]).SetAttValue ('SigState','RED')             
            if Seconds >= Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(Aseq[7][1]).AttValue ('GreenEnd')-1:
                if Seconds < Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(Aseq[7][1]).AttValue ('GreenEnd')+2:                 
                    Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(Aseq[7][2]).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(Aseq[7][0]).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(Aseq[7][1]).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(Aseq[7][3]).SetAttValue ('SigState','RED')



                    GI11=[[(CLength-12-Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(Aseq[7][0]).AttValue ('GreenTimeDuration')-Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(Aseq[7][1]).AttValue ('GreenTimeDuration'))/2,(CLength-12-Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(Aseq[7][0]).AttValue ('GreenTimeDuration')-Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(Aseq[7][1]).AttValue ('GreenTimeDuration'))/2],[2*(CLength-12-Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(Aseq[7][0]).AttValue ('GreenTimeDuration')-Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(Aseq[7][1]).AttValue ('GreenTimeDuration'))/3,(CLength-12-Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(Aseq[7][0]).AttValue ('GreenTimeDuration')-Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(Aseq[7][1]).AttValue ('GreenTimeDuration'))/3]]
                    indexI11=permutation([Aseq[7][2],Aseq[7][3]])
                    grreenstrat11=[]
                    grreenenddd11=[]
                    for i in range(len(GI11)):
                        kokop=[]
                        kokop2=[]
                        for j in range(len(GI11[i])):

                            kokop.append([8+Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(Aseq[7][0]).AttValue ('GreenTimeDuration') + Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(Aseq[7][0]).AttValue ('GreenTimeDuration'), 11+Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(Aseq[7][0]).AttValue ('GreenTimeDuration')+Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(Aseq[7][1]).AttValue ('GreenTimeDuration')+ GI11[i][j] ])
                            kokop2.append([8+Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(Aseq[7][0]).AttValue ('GreenTimeDuration') + Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(Aseq[7][0]).AttValue ('GreenTimeDuration') + GI11[i][j], 11+Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(Aseq[7][0]).AttValue ('GreenTimeDuration')+Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(Aseq[7][1]).AttValue ('GreenTimeDuration')+ GI11[i][j-1] + GI11[i][j]])

                              
                        grreenstrat11.append(kokop)

                        grreenenddd11.append(kokop2)





                    ddst=[]
                    varices=[]
                    for i in grreenstrat11:
                        ddst1=[]
                        varices2=[]

                        for j in i:
                            ddst1.append(Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(Aseq[7][2]).AttValue ('distributionincapacity')+Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(Aseq[7][2]).AttValue ('ArrivalRate')*((j[0]-SimSec)/3600)-0.8*GI11[grreenstrat11.index(i)][0])
                            ddst1.append(Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(Aseq[7][3]).AttValue ('distributionincapacity')+Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(Aseq[7][3]).AttValue ('ArrivalRate')*((j[1]-SimSec)/3600)-0.8*GI11[grreenstrat11.index(i)][1])
                            varices2.append(variance(ddst1))
                        ddst.append(ddst1)
                        varices.append(varices2)
                        

                    varices = flatten_list (varices)                    




                    ipip= int(math.floor(varices.index(min(varices))/2))
                    jpjp= int(varices.index(min(varices))- ipip*2)







                    Aseq[7][2]= indexI11[jpjp][0]
                    Aseq[7][3]= indexI11[jpjp][1]

                    f2= open("Aseq.txt","w")
                    f2.write(str(Aseq))
                    f2.write("\n")
                    f2.close()







   

                    Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(Aseq[7][2]).SetAttValue('GreenTimeDuration',GI11[ipip][0])
                    Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(Aseq[7][3]).SetAttValue('GreenTimeDuration',GI11[ipip][1])



                    Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(Aseq[7][2]).SetAttValue('GreenStart',grreenstrat11[ipip][jpjp][0])
                    Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(Aseq[7][3]).SetAttValue('GreenStart',grreenstrat11[ipip][jpjp][1])


    

                    Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(Aseq[7][2]).SetAttValue('GreenEnd',grreenenddd11[ipip][jpjp][0])
                    Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(Aseq[7][3]).SetAttValue('GreenEnd',grreenenddd11[ipip][jpjp][1])






        if Seconds >= Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(Aseq[7][2]).AttValue ('GreenStart')-1:
            if Seconds <= Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(Aseq[7][2]).AttValue ('GreenEnd')-1:
                    Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(Aseq[7][2]).SetAttValue ('SigState','GREEN')
                    Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(Aseq[7][0]).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(Aseq[7][1]).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(Aseq[7][3]).SetAttValue ('SigState','RED')


        if  Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(Aseq[7][2]).AttValue ('SigState') == 'GREEN':
            Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(Aseq[7][0]).SetAttValue ('SigState','RED')
            Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(Aseq[7][1]).SetAttValue ('SigState','RED')
            Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(Aseq[7][3]).SetAttValue ('SigState','RED') 
            if Seconds >= Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(Aseq[7][2]).AttValue ('GreenEnd')-1:
                if Seconds < Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(Aseq[7][2]).AttValue ('GreenEnd')+2:             
                    Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(Aseq[7][3]).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(Aseq[7][0]).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(Aseq[7][1]).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(Aseq[7][2]).SetAttValue ('SigState','RED')


        if Seconds >= Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(Aseq[7][3]).AttValue ('GreenStart')-1:
            if Seconds <= Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(Aseq[7][3]).AttValue ('GreenEnd')-1:
                    Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(Aseq[7][3]).SetAttValue ('SigState','GREEN')
                    Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(Aseq[7][0]).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(Aseq[7][1]).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(Aseq[7][2]).SetAttValue ('SigState','RED')


        if  Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(Aseq[7][3]).AttValue ('SigState') == 'GREEN':
            Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(Aseq[7][0]).SetAttValue ('SigState','RED')
            Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(Aseq[7][1]).SetAttValue ('SigState','RED')
            Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(Aseq[7][2]).SetAttValue ('SigState','RED')
            if Seconds >= Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(Aseq[7][3]).AttValue ('GreenEnd')-1:             
                    Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(Aseq[7][0]).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(Aseq[7][1]).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(Aseq[7][2]).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(Aseq[7][3]).SetAttValue ('SigState','RED')






                    GI11=[[(CLength-12)/4,(CLength-12)/4,(CLength-12)/4,(CLength-12)/4],[(CLength-12)/3,(CLength-12)/3,(CLength-12)/6,(CLength-12)/6],[(CLength-12)/3,(CLength-12)/3,(CLength-12)/6,(CLength-12)/6], [(CLength-12)/2,(CLength-12)/6,(CLength-12)/6,(CLength-12)/6],[(CLength-12)/4,(CLength-12)/4,(CLength-12)/4,(CLength-12)/4],[(CLength-12)/3,(CLength-12)/3,(CLength-12)/6,(CLength-12)/6],[(CLength-12)/3,(CLength-12)/3,(CLength-12)/6,(CLength-12)/6], [(CLength-12)/2,(CLength-12)/6,(CLength-12)/6,(CLength-12)/6],[(CLength-12)/4,(CLength-12)/4,(CLength-12)/4,(CLength-12)/4],[(CLength-12)/3,(CLength-12)/3,(CLength-12)/6,(CLength-12)/6],[(CLength-12)/3,(CLength-12)/3,(CLength-12)/6,(CLength-12)/6], [(CLength-12)/2,(CLength-12)/6,(CLength-12)/6,(CLength-12)/6],[(CLength-12)/4,(CLength-12)/4,(CLength-12)/4,(CLength-12)/4],[(CLength-12)/3,(CLength-12)/3,(CLength-12)/6,(CLength-12)/6],[(CLength-12)/3,(CLength-12)/3,(CLength-12)/6,(CLength-12)/6], [(CLength-12)/2,(CLength-12)/6,(CLength-12)/6,(CLength-12)/6],[(CLength-12)/4,(CLength-12)/4,(CLength-12)/4,(CLength-12)/4],[(CLength-12)/3,(CLength-12)/3,(CLength-12)/6,(CLength-12)/6],[(CLength-12)/3,(CLength-12)/3,(CLength-12)/6,(CLength-12)/6], [(CLength-12)/2,(CLength-12)/6,(CLength-12)/6,(CLength-12)/6],[(CLength-12)/4,(CLength-12)/4,(CLength-12)/4,(CLength-12)/4],[(CLength-12)/3,(CLength-12)/3,(CLength-12)/6,(CLength-12)/6],[(CLength-12)/3,(CLength-12)/3,(CLength-12)/6,(CLength-12)/6], [(CLength-12)/2,(CLength-12)/6,(CLength-12)/6,(CLength-12)/6]]
                    indexI11=permutation([Aseq[7][0],Aseq[7][1],Aseq[7][2],Aseq[7][3]])
                    grreenstrat11=[]
                    grreenenddd11=[]
                    for i in range(len(GI11)):
                        kokop=[]
                        kokop2=[]
                        for j in range(len(GI11[i])):
                            kokop.append([2, 5+GI11[i][j-3], 8+GI11[i][j-3]+GI11[i][j-2], 11+GI11[i][j-3]+GI11[i][j-2] +GI11[i][j-1]])
                            kokop2.append([2+GI11[i][j-3], 5+GI11[i][j-3]+GI11[i][j-2], 8+GI11[i][j-3]+GI11[i][j-2]+GI11[i][j-1], 11 +GI11[i][j-3]+GI11[i][j-2]+GI11[i][j-1] +GI11[i][j]])
 
                        grreenstrat11.append(kokop)
                        grreenenddd11.append(kokop2)




                    ddst=[]
                    varices=[]
                    for i in grreenstrat11:
                        ddst1=[]
                        varices2=[]

                        for j in i:
                            ddst1.append(Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(Aseq[7][0]).AttValue ('distributionincapacity')+Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(Aseq[7][0]).AttValue ('ArrivalRate')*((j[0]-SimSec)/3600)-0.8*GI11[grreenstrat11.index(i)][0])
                            ddst1.append(Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(Aseq[7][1]).AttValue ('distributionincapacity')+Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(Aseq[7][1]).AttValue ('ArrivalRate')*((j[1]-SimSec)/3600)-0.8*GI11[grreenstrat11.index(i)][1])
                            ddst1.append(Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(Aseq[7][2]).AttValue ('distributionincapacity')+Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(Aseq[7][2]).AttValue ('ArrivalRate')*((j[2]-SimSec)/3600)-0.8*GI11[grreenstrat11.index(i)][2])
                            ddst1.append(Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(Aseq[7][3]).AttValue ('distributionincapacity')+Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(Aseq[7][3]).AttValue ('ArrivalRate')*((j[3]-SimSec)/3600)-0.8*GI11[grreenstrat11.index(i)][3])
                            varices2.append(variance(ddst1))
                        ddst.append(ddst1)
                        varices.append(varices2)

                    varices = flatten_list (varices)                    




                    ipip= int(math.floor(varices.index(min(varices))/4))
                    jpjp= int(varices.index(min(varices))- ipip*4)






                    Aseq[7][0]= indexI11[jpjp][0]
                    Aseq[7][1]= indexI11[jpjp][1]
                    Aseq[7][2]= indexI11[jpjp][2]
                    Aseq[7][3]= indexI11[jpjp][3]

                    f2= open("Aseq.txt","w")
                    f2.write(str(Aseq))
                    f2.write("\n")
                    f2.close()



                    Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(Aseq[7][0]).SetAttValue('GreenTimeDuration',GI11[ipip][0])   
                    Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(Aseq[7][1]).SetAttValue('GreenTimeDuration',GI11[ipip][1])
                    Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(Aseq[7][2]).SetAttValue('GreenTimeDuration',GI11[ipip][2])
                    Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(Aseq[7][3]).SetAttValue('GreenTimeDuration',GI11[ipip][3])



                    Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(Aseq[7][0]).SetAttValue('GreenStart',grreenstrat11[ipip][jpjp][0])     
                    Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(Aseq[7][1]).SetAttValue('GreenStart',grreenstrat11[ipip][jpjp][1])
                    Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(Aseq[7][2]).SetAttValue('GreenStart',grreenstrat11[ipip][jpjp][2])
                    Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(Aseq[7][3]).SetAttValue('GreenStart',grreenstrat11[ipip][jpjp][3])


                    Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(Aseq[7][0]).SetAttValue('GreenEnd',grreenenddd11[ipip][jpjp][0])    
                    Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(Aseq[7][1]).SetAttValue('GreenEnd',grreenenddd11[ipip][jpjp][1])
                    Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(Aseq[7][2]).SetAttValue('GreenEnd',grreenenddd11[ipip][jpjp][2])
                    Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(Aseq[7][3]).SetAttValue('GreenEnd',grreenenddd11[ipip][jpjp][3])









                        




























        if  Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(Aseq[6][0]).AttValue ('SigState') == 'GREEN':
            Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(Aseq[6][1]).SetAttValue ('SigState','RED')
            Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(Aseq[6][2]).SetAttValue ('SigState','RED')
            Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(Aseq[6][3]).SetAttValue ('SigState','RED')
            if Seconds >= Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(Aseq[6][0]).AttValue ('GreenEnd')-1:
                if Seconds < Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(Aseq[6][0]).AttValue ('GreenEnd')+2:
                    Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(Aseq[6][1]).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(Aseq[6][0]).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(Aseq[6][2]).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(Aseq[6][3]).SetAttValue ('SigState','RED')


                    GI11=[[(CLength-12-Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(Aseq[6][0]).AttValue ('GreenTimeDuration'))/3,(CLength-12-Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(Aseq[6][0]).AttValue ('GreenTimeDuration'))/3,(CLength-12-Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(Aseq[6][0]).AttValue ('GreenTimeDuration'))/3], [(CLength-12-Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(Aseq[6][0]).AttValue ('GreenTimeDuration'))/4,(CLength-12-Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(Aseq[6][0]).AttValue ('GreenTimeDuration'))/4,(CLength-12-Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(Aseq[6][0]).AttValue ('GreenTimeDuration'))/2],[(CLength-12-Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(Aseq[6][0]).AttValue ('GreenTimeDuration'))/4,(CLength-12-Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(Aseq[6][0]).AttValue ('GreenTimeDuration'))/2,(CLength-12-Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(Aseq[6][0]).AttValue ('GreenTimeDuration'))/4],[(CLength-12-Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(Aseq[6][0]).AttValue ('GreenTimeDuration'))/5,3*(CLength-12-Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(Aseq[6][0]).AttValue ('GreenTimeDuration'))/5,(CLength-12-Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(Aseq[6][0]).AttValue ('GreenTimeDuration'))/5],[(CLength-12-Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(Aseq[6][0]).AttValue ('GreenTimeDuration'))/6,4*(CLength-12-Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(Aseq[6][0]).AttValue ('GreenTimeDuration'))/6,(CLength-12-Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(Aseq[6][0]).AttValue ('GreenTimeDuration'))/6],[(CLength-12-Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(Aseq[6][0]).AttValue ('GreenTimeDuration'))/7,5*(CLength-12-Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(Aseq[6][0]).AttValue ('GreenTimeDuration'))/7,(CLength-12-Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(Aseq[6][0]).AttValue ('GreenTimeDuration'))/7]]
                    indexI11=permutation([Aseq[6][1],Aseq[6][2],Aseq[6][3]])
                    grreenstrat11=[]
                    grreenenddd11=[]
                    for i in range(len(GI11)):
                        kokop=[]
                        kokop2=[]
                        for j in range(len(GI11[i])):
                            kokop.append([5+Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(Aseq[6][0]).AttValue ('GreenTimeDuration'), 8+Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(Aseq[6][0]).AttValue ('GreenTimeDuration')+GI11[i][j], 11+Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(Aseq[6][0]).AttValue ('GreenTimeDuration')+GI11[i][j ] +GI11[i][j-1]])
                            kokop2.append([5+Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(Aseq[6][0]).AttValue ('GreenTimeDuration')+GI11[i][j], 8+Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(Aseq[6][0]).AttValue ('GreenTimeDuration')+GI11[i][j-1] +GI11[i][j], 11+Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(Aseq[6][0]).AttValue ('GreenTimeDuration')+GI11[i][j ] +GI11[i][j-1]+GI11[i][j]])
                              
                        grreenstrat11.append(kokop)

                        grreenenddd11.append(kokop2)






                    ddst=[]
                    varices=[]
                    for i in grreenstrat11:
                        ddst1=[]
                        varices2=[]

                        for j in i:
                            ddst1.append(Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(Aseq[6][1]).AttValue ('distributionincapacity')+Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(Aseq[6][1]).AttValue ('ArrivalRate')*((j[0]-SimSec)/3600)-0.7*GI11[grreenstrat11.index(i)][0])
                            ddst1.append(Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(Aseq[6][2]).AttValue ('distributionincapacity')+Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(Aseq[6][2]).AttValue ('ArrivalRate')*((j[1]-SimSec)/3600)-0.7*GI11[grreenstrat11.index(i)][1])
                            ddst1.append(Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(Aseq[6][3]).AttValue ('distributionincapacity')+Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(Aseq[6][3]).AttValue ('ArrivalRate')*((j[2]-SimSec)/3600)-0.7*GI11[grreenstrat11.index(i)][2])
                            varices2.append(variance(ddst1))
                        ddst.append(ddst1)
                        varices.append(varices2)
                        



                    varices = flatten_list (varices)                    




                    ipip= int(math.floor(varices.index(min(varices))/3))
                    jpjp= int(varices.index(min(varices))- ipip*3)


                    Aseq[6][1]= indexI11[jpjp][0]
                    Aseq[6][2]= indexI11[jpjp][1]
                    Aseq[6][3]= indexI11[jpjp][2]

                    f2= open("Aseq.txt","w")
                    f2.write(str(Aseq))
                    f2.write("\n")
                    f2.close()






   
                    Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(Aseq[6][1]).SetAttValue('GreenTimeDuration',GI11[ipip][0])
                    Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(Aseq[6][2]).SetAttValue('GreenTimeDuration',GI11[ipip][1])
                    Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(Aseq[6][3]).SetAttValue('GreenTimeDuration',GI11[ipip][2])


     
                    Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(Aseq[6][1]).SetAttValue('GreenStart',grreenstrat11[ipip][jpjp][0])
                    Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(Aseq[6][2]).SetAttValue('GreenStart',grreenstrat11[ipip][jpjp][1])
                    Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(Aseq[6][3]).SetAttValue('GreenStart',grreenstrat11[ipip][jpjp][2])


    
                    Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(Aseq[6][1]).SetAttValue('GreenEnd',grreenenddd11[ipip][jpjp][0])
                    Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(Aseq[6][2]).SetAttValue('GreenEnd',grreenenddd11[ipip][jpjp][1])
                    Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(Aseq[6][3]).SetAttValue('GreenEnd',grreenenddd11[ipip][jpjp][2])








        if Seconds >= Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(Aseq[6][1]).AttValue ('GreenStart')-1:
            if Seconds <= Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(Aseq[6][1]).AttValue ('GreenEnd')-1:
                    Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(Aseq[6][1]).SetAttValue ('SigState','GREEN')
                    Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(Aseq[6][0]).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(Aseq[6][2]).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(Aseq[6][3]).SetAttValue ('SigState','RED')


        if  Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(Aseq[6][1]).AttValue ('SigState') == 'GREEN':
            Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(Aseq[6][0]).SetAttValue ('SigState','RED')
            Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(Aseq[6][2]).SetAttValue ('SigState','RED')
            Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(Aseq[6][3]).SetAttValue ('SigState','RED')             
            if Seconds >= Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(Aseq[6][1]).AttValue ('GreenEnd')-1:
                if Seconds < Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(Aseq[6][1]).AttValue ('GreenEnd')+2:                 
                    Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(Aseq[6][2]).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(Aseq[6][0]).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(Aseq[6][1]).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(Aseq[6][3]).SetAttValue ('SigState','RED')



                    GI11=[[(CLength-12-Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(Aseq[6][0]).AttValue ('GreenTimeDuration')-Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(Aseq[6][1]).AttValue ('GreenTimeDuration'))/2,(CLength-12-Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(Aseq[6][0]).AttValue ('GreenTimeDuration')-Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(Aseq[6][1]).AttValue ('GreenTimeDuration'))/2],[2*(CLength-12-Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(Aseq[6][0]).AttValue ('GreenTimeDuration')-Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(Aseq[6][1]).AttValue ('GreenTimeDuration'))/3,(CLength-12-Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(Aseq[6][0]).AttValue ('GreenTimeDuration')-Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(Aseq[6][1]).AttValue ('GreenTimeDuration'))/3]]
                    indexI11=permutation([Aseq[6][2],Aseq[6][3]])
                    grreenstrat11=[]
                    grreenenddd11=[]
                    for i in range(len(GI11)):
                        kokop=[]
                        kokop2=[]
                        for j in range(len(GI11[i])):

                            kokop.append([8+Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(Aseq[6][0]).AttValue ('GreenTimeDuration') + Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(Aseq[6][0]).AttValue ('GreenTimeDuration'), 11+Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(Aseq[6][0]).AttValue ('GreenTimeDuration')+Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(Aseq[6][1]).AttValue ('GreenTimeDuration')+ GI11[i][j] ])
                            kokop2.append([8+Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(Aseq[6][0]).AttValue ('GreenTimeDuration') + Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(Aseq[6][0]).AttValue ('GreenTimeDuration') + GI11[i][j], 11+Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(Aseq[6][0]).AttValue ('GreenTimeDuration')+Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(Aseq[6][1]).AttValue ('GreenTimeDuration')+ GI11[i][j-1] + GI11[i][j]])

                              
                        grreenstrat11.append(kokop)

                        grreenenddd11.append(kokop2)





                    ddst=[]
                    varices=[]
                    for i in grreenstrat11:
                        ddst1=[]
                        varices2=[]

                        for j in i:
                            ddst1.append(Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(Aseq[6][2]).AttValue ('distributionincapacity')+Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(Aseq[6][2]).AttValue ('ArrivalRate')*((j[0]-SimSec)/3600)-0.7*GI11[grreenstrat11.index(i)][0])
                            ddst1.append(Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(Aseq[6][3]).AttValue ('distributionincapacity')+Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(Aseq[6][3]).AttValue ('ArrivalRate')*((j[1]-SimSec)/3600)-0.7*GI11[grreenstrat11.index(i)][1])
                            varices2.append(variance(ddst1))
                        ddst.append(ddst1)
                        varices.append(varices2)
                        

                    varices = flatten_list (varices)                    




                    ipip= int(math.floor(varices.index(min(varices))/2))
                    jpjp= int(varices.index(min(varices))- ipip*2)







                    Aseq[6][2]= indexI11[jpjp][0]
                    Aseq[6][3]= indexI11[jpjp][1]

                    f2= open("Aseq.txt","w")
                    f2.write(str(Aseq))
                    f2.write("\n")
                    f2.close()







   

                    Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(Aseq[6][2]).SetAttValue('GreenTimeDuration',GI11[ipip][0])
                    Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(Aseq[6][3]).SetAttValue('GreenTimeDuration',GI11[ipip][1])



                    Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(Aseq[6][2]).SetAttValue('GreenStart',grreenstrat11[ipip][jpjp][0])
                    Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(Aseq[6][3]).SetAttValue('GreenStart',grreenstrat11[ipip][jpjp][1])


    

                    Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(Aseq[6][2]).SetAttValue('GreenEnd',grreenenddd11[ipip][jpjp][0])
                    Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(Aseq[6][3]).SetAttValue('GreenEnd',grreenenddd11[ipip][jpjp][1])







        if Seconds >= Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(Aseq[6][2]).AttValue ('GreenStart')-1:
            if Seconds <= Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(Aseq[6][2]).AttValue ('GreenEnd')-1:
                    Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(Aseq[6][2]).SetAttValue ('SigState','GREEN')
                    Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(Aseq[6][0]).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(Aseq[6][1]).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(Aseq[6][3]).SetAttValue ('SigState','RED')


        if  Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(Aseq[6][2]).AttValue ('SigState') == 'GREEN':
            Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(Aseq[6][0]).SetAttValue ('SigState','RED')
            Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(Aseq[6][1]).SetAttValue ('SigState','RED')
            Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(Aseq[6][3]).SetAttValue ('SigState','RED') 
            if Seconds >= Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(Aseq[6][2]).AttValue ('GreenEnd')-1:
                if Seconds < Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(Aseq[6][2]).AttValue ('GreenEnd')+2:             
                    Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(Aseq[6][3]).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(Aseq[6][0]).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(Aseq[6][1]).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(Aseq[6][2]).SetAttValue ('SigState','RED')


        if Seconds >= Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(Aseq[6][3]).AttValue ('GreenStart')-1:
            if Seconds <= Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(Aseq[6][3]).AttValue ('GreenEnd')-1:
                    Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(Aseq[6][3]).SetAttValue ('SigState','GREEN')
                    Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(Aseq[6][0]).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(Aseq[6][1]).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(Aseq[6][2]).SetAttValue ('SigState','RED')


        if  Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(Aseq[6][3]).AttValue ('SigState') == 'GREEN':
            Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(Aseq[6][0]).SetAttValue ('SigState','RED')
            Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(Aseq[6][1]).SetAttValue ('SigState','RED')
            Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(Aseq[6][2]).SetAttValue ('SigState','RED')
            if Seconds >= Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(Aseq[6][3]).AttValue ('GreenEnd')-1:             
                    Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(Aseq[6][0]).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(Aseq[6][1]).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(Aseq[6][2]).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(Aseq[6][3]).SetAttValue ('SigState','RED')






                    GI11=[[(CLength-12)/4,(CLength-12)/4,(CLength-12)/4,(CLength-12)/4],[(CLength-12)/3,(CLength-12)/3,(CLength-12)/6,(CLength-12)/6],[(CLength-12)/3,(CLength-12)/3,(CLength-12)/6,(CLength-12)/6], [(CLength-12)/2,(CLength-12)/6,(CLength-12)/6,(CLength-12)/6],[(CLength-12)/4,(CLength-12)/4,(CLength-12)/4,(CLength-12)/4],[(CLength-12)/3,(CLength-12)/3,(CLength-12)/6,(CLength-12)/6],[(CLength-12)/3,(CLength-12)/3,(CLength-12)/6,(CLength-12)/6], [(CLength-12)/2,(CLength-12)/6,(CLength-12)/6,(CLength-12)/6],[(CLength-12)/4,(CLength-12)/4,(CLength-12)/4,(CLength-12)/4],[(CLength-12)/3,(CLength-12)/3,(CLength-12)/6,(CLength-12)/6],[(CLength-12)/3,(CLength-12)/3,(CLength-12)/6,(CLength-12)/6], [(CLength-12)/2,(CLength-12)/6,(CLength-12)/6,(CLength-12)/6],[(CLength-12)/4,(CLength-12)/4,(CLength-12)/4,(CLength-12)/4],[(CLength-12)/3,(CLength-12)/3,(CLength-12)/6,(CLength-12)/6],[(CLength-12)/3,(CLength-12)/3,(CLength-12)/6,(CLength-12)/6], [(CLength-12)/2,(CLength-12)/6,(CLength-12)/6,(CLength-12)/6],[(CLength-12)/4,(CLength-12)/4,(CLength-12)/4,(CLength-12)/4],[(CLength-12)/3,(CLength-12)/3,(CLength-12)/6,(CLength-12)/6],[(CLength-12)/3,(CLength-12)/3,(CLength-12)/6,(CLength-12)/6], [(CLength-12)/2,(CLength-12)/6,(CLength-12)/6,(CLength-12)/6],[(CLength-12)/4,(CLength-12)/4,(CLength-12)/4,(CLength-12)/4],[(CLength-12)/3,(CLength-12)/3,(CLength-12)/6,(CLength-12)/6],[(CLength-12)/3,(CLength-12)/3,(CLength-12)/6,(CLength-12)/6], [(CLength-12)/2,(CLength-12)/6,(CLength-12)/6,(CLength-12)/6]]
                    indexI11=permutation([Aseq[6][0],Aseq[6][1],Aseq[6][2],Aseq[6][3]])
                    grreenstrat11=[]
                    grreenenddd11=[]
                    for i in range(len(GI11)):
                        kokop=[]
                        kokop2=[]
                        for j in range(len(GI11[i])):
                            kokop.append([2, 5+GI11[i][j-3], 8+GI11[i][j-3]+GI11[i][j-2], 11+GI11[i][j-3]+GI11[i][j-2] +GI11[i][j-1]])
                            kokop2.append([2+GI11[i][j-3], 5+GI11[i][j-3]+GI11[i][j-2], 8+GI11[i][j-3]+GI11[i][j-2]+GI11[i][j-1], 11 +GI11[i][j-3]+GI11[i][j-2]+GI11[i][j-1] +GI11[i][j]])
 
                        grreenstrat11.append(kokop)
                        grreenenddd11.append(kokop2)




                    ddst=[]
                    varices=[]
                    for i in grreenstrat11:
                        ddst1=[]
                        varices2=[]

                        for j in i:
                            ddst1.append(Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(Aseq[6][0]).AttValue ('distributionincapacity')+Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(Aseq[6][0]).AttValue ('ArrivalRate')*((j[0]-SimSec)/3600)-0.7*GI11[grreenstrat11.index(i)][0])
                            ddst1.append(Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(Aseq[6][1]).AttValue ('distributionincapacity')+Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(Aseq[6][1]).AttValue ('ArrivalRate')*((j[1]-SimSec)/3600)-0.7*GI11[grreenstrat11.index(i)][1])
                            ddst1.append(Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(Aseq[6][2]).AttValue ('distributionincapacity')+Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(Aseq[6][2]).AttValue ('ArrivalRate')*((j[2]-SimSec)/3600)-0.7*GI11[grreenstrat11.index(i)][2])
                            ddst1.append(Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(Aseq[6][3]).AttValue ('distributionincapacity')+Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(Aseq[6][3]).AttValue ('ArrivalRate')*((j[3]-SimSec)/3600)-0.7*GI11[grreenstrat11.index(i)][3])
                            varices2.append(variance(ddst1))
                        ddst.append(ddst1)
                        varices.append(varices2)

                    varices = flatten_list (varices)                    




                    ipip= int(math.floor(varices.index(min(varices))/4))
                    jpjp= int(varices.index(min(varices))- ipip*4)






                    Aseq[6][0]= indexI11[jpjp][0]
                    Aseq[6][1]= indexI11[jpjp][1]
                    Aseq[6][2]= indexI11[jpjp][2]
                    Aseq[6][3]= indexI11[jpjp][3]

                    f2= open("Aseq.txt","w")
                    f2.write(str(Aseq))
                    f2.write("\n")
                    f2.close()



                    Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(Aseq[6][0]).SetAttValue('GreenTimeDuration',GI11[ipip][0])   
                    Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(Aseq[6][1]).SetAttValue('GreenTimeDuration',GI11[ipip][1])
                    Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(Aseq[6][2]).SetAttValue('GreenTimeDuration',GI11[ipip][2])
                    Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(Aseq[6][3]).SetAttValue('GreenTimeDuration',GI11[ipip][3])



                    Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(Aseq[6][0]).SetAttValue('GreenStart',grreenstrat11[ipip][jpjp][0])     
                    Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(Aseq[6][1]).SetAttValue('GreenStart',grreenstrat11[ipip][jpjp][1])
                    Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(Aseq[6][2]).SetAttValue('GreenStart',grreenstrat11[ipip][jpjp][2])
                    Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(Aseq[6][3]).SetAttValue('GreenStart',grreenstrat11[ipip][jpjp][3])


                    Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(Aseq[6][0]).SetAttValue('GreenEnd',grreenenddd11[ipip][jpjp][0])    
                    Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(Aseq[6][1]).SetAttValue('GreenEnd',grreenenddd11[ipip][jpjp][1])
                    Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(Aseq[6][2]).SetAttValue('GreenEnd',grreenenddd11[ipip][jpjp][2])
                    Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(Aseq[6][3]).SetAttValue('GreenEnd',grreenenddd11[ipip][jpjp][3])









                        











































        if  Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(Aseq[5][0]).AttValue ('SigState') == 'GREEN':
            Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(Aseq[5][1]).SetAttValue ('SigState','RED')
            Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(Aseq[5][2]).SetAttValue ('SigState','RED')
            Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(Aseq[5][3]).SetAttValue ('SigState','RED')
            if Seconds >= Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(Aseq[5][0]).AttValue ('GreenEnd')-1:
                if Seconds < Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(Aseq[5][0]).AttValue ('GreenEnd')+2:
                    Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(Aseq[5][1]).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(Aseq[5][0]).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(Aseq[5][2]).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(Aseq[5][3]).SetAttValue ('SigState','RED')

                    GI11=[[(CLength-12-Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(Aseq[5][0]).AttValue ('GreenTimeDuration'))/3,(CLength-12-Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(Aseq[5][0]).AttValue ('GreenTimeDuration'))/3,(CLength-12-Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(Aseq[5][0]).AttValue ('GreenTimeDuration'))/3], [(CLength-12-Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(Aseq[5][0]).AttValue ('GreenTimeDuration'))/4,(CLength-12-Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(Aseq[5][0]).AttValue ('GreenTimeDuration'))/4,(CLength-12-Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(Aseq[5][0]).AttValue ('GreenTimeDuration'))/2],[(CLength-12-Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(Aseq[5][0]).AttValue ('GreenTimeDuration'))/4,(CLength-12-Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(Aseq[5][0]).AttValue ('GreenTimeDuration'))/2,(CLength-12-Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(Aseq[5][0]).AttValue ('GreenTimeDuration'))/4],[(CLength-12-Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(Aseq[5][0]).AttValue ('GreenTimeDuration'))/5,3*(CLength-12-Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(Aseq[5][0]).AttValue ('GreenTimeDuration'))/5,(CLength-12-Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(Aseq[5][0]).AttValue ('GreenTimeDuration'))/5],[(CLength-12-Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(Aseq[5][0]).AttValue ('GreenTimeDuration'))/6,4*(CLength-12-Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(Aseq[5][0]).AttValue ('GreenTimeDuration'))/6,(CLength-12-Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(Aseq[5][0]).AttValue ('GreenTimeDuration'))/6],[(CLength-12-Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(Aseq[5][0]).AttValue ('GreenTimeDuration'))/7,5*(CLength-12-Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(Aseq[5][0]).AttValue ('GreenTimeDuration'))/7,(CLength-12-Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(Aseq[5][0]).AttValue ('GreenTimeDuration'))/7]]
                    indexI11=permutation([Aseq[5][1],Aseq[5][2],Aseq[5][3]])
                    grreenstrat11=[]
                    grreenenddd11=[]
                    for i in range(len(GI11)):
                        kokop=[]
                        kokop2=[]
                        for j in range(len(GI11[i])):
                            kokop.append([5+Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(Aseq[5][0]).AttValue ('GreenTimeDuration'), 8+Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(Aseq[5][0]).AttValue ('GreenTimeDuration')+GI11[i][j], 11+Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(Aseq[5][0]).AttValue ('GreenTimeDuration')+GI11[i][j ] +GI11[i][j-1]])
                            kokop2.append([5+Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(Aseq[5][0]).AttValue ('GreenTimeDuration')+GI11[i][j], 8+Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(Aseq[5][0]).AttValue ('GreenTimeDuration')+GI11[i][j-1] +GI11[i][j], 11+Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(Aseq[5][0]).AttValue ('GreenTimeDuration')+GI11[i][j ] +GI11[i][j-1]+GI11[i][j]])
                              
                        grreenstrat11.append(kokop)

                        grreenenddd11.append(kokop2)






                    ddst=[]
                    varices=[]
                    for i in grreenstrat11:
                        ddst1=[]
                        varices2=[]

                        for j in i:
                            ddst1.append(Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(Aseq[5][1]).AttValue ('distributionincapacity')+Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(Aseq[5][1]).AttValue ('ArrivalRate')*((j[0]-SimSec)/3600)-0.6*GI11[grreenstrat11.index(i)][0])
                            ddst1.append(Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(Aseq[5][2]).AttValue ('distributionincapacity')+Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(Aseq[5][2]).AttValue ('ArrivalRate')*((j[1]-SimSec)/3600)-0.6*GI11[grreenstrat11.index(i)][1])
                            ddst1.append(Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(Aseq[5][3]).AttValue ('distributionincapacity')+Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(Aseq[5][3]).AttValue ('ArrivalRate')*((j[2]-SimSec)/3600)-0.6*GI11[grreenstrat11.index(i)][2])
                            varices2.append(variance(ddst1))
                        ddst.append(ddst1)
                        varices.append(varices2)
                        



                    varices = flatten_list (varices)                    




                    ipip= int(math.floor(varices.index(min(varices))/3))
                    jpjp= int(varices.index(min(varices))- ipip*3)


                    Aseq[5][1]= indexI11[jpjp][0]
                    Aseq[5][2]= indexI11[jpjp][1]
                    Aseq[5][3]= indexI11[jpjp][2]

                    f2= open("Aseq.txt","w")
                    f2.write(str(Aseq))
                    f2.write("\n")
                    f2.close()






   
                    Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(Aseq[5][1]).SetAttValue('GreenTimeDuration',GI11[ipip][0])
                    Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(Aseq[5][2]).SetAttValue('GreenTimeDuration',GI11[ipip][1])
                    Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(Aseq[5][3]).SetAttValue('GreenTimeDuration',GI11[ipip][2])


     
                    Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(Aseq[5][1]).SetAttValue('GreenStart',grreenstrat11[ipip][jpjp][0])
                    Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(Aseq[5][2]).SetAttValue('GreenStart',grreenstrat11[ipip][jpjp][1])
                    Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(Aseq[5][3]).SetAttValue('GreenStart',grreenstrat11[ipip][jpjp][2])


    
                    Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(Aseq[5][1]).SetAttValue('GreenEnd',grreenenddd11[ipip][jpjp][0])
                    Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(Aseq[5][2]).SetAttValue('GreenEnd',grreenenddd11[ipip][jpjp][1])
                    Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(Aseq[5][3]).SetAttValue('GreenEnd',grreenenddd11[ipip][jpjp][2])




        if Seconds >= Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(Aseq[5][1]).AttValue ('GreenStart')-1:
            if Seconds <= Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(Aseq[5][1]).AttValue ('GreenEnd')-1:
                    Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(Aseq[5][1]).SetAttValue ('SigState','GREEN')
                    Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(Aseq[5][0]).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(Aseq[5][2]).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(Aseq[5][3]).SetAttValue ('SigState','RED')


        if  Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(Aseq[5][1]).AttValue ('SigState') == 'GREEN':
            Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(Aseq[5][0]).SetAttValue ('SigState','RED')
            Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(Aseq[5][2]).SetAttValue ('SigState','RED')
            Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(Aseq[5][3]).SetAttValue ('SigState','RED')             
            if Seconds >= Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(Aseq[5][1]).AttValue ('GreenEnd')-1:
                if Seconds < Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(Aseq[5][1]).AttValue ('GreenEnd')+2:                 
                    Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(Aseq[5][2]).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(Aseq[5][0]).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(Aseq[5][1]).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(Aseq[5][3]).SetAttValue ('SigState','RED')


                    GI11=[[(CLength-12-Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(Aseq[5][0]).AttValue ('GreenTimeDuration')-Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(Aseq[5][1]).AttValue ('GreenTimeDuration'))/2,(CLength-12-Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(Aseq[5][0]).AttValue ('GreenTimeDuration')-Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(Aseq[5][1]).AttValue ('GreenTimeDuration'))/2],[2*(CLength-12-Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(Aseq[5][0]).AttValue ('GreenTimeDuration')-Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(Aseq[5][1]).AttValue ('GreenTimeDuration'))/3,(CLength-12-Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(Aseq[5][0]).AttValue ('GreenTimeDuration')-Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(Aseq[5][1]).AttValue ('GreenTimeDuration'))/3]]
                    indexI11=permutation([Aseq[5][2],Aseq[5][3]])
                    grreenstrat11=[]
                    grreenenddd11=[]
                    for i in range(len(GI11)):
                        kokop=[]
                        kokop2=[]
                        for j in range(len(GI11[i])):

                            kokop.append([8+Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(Aseq[5][0]).AttValue ('GreenTimeDuration') + Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(Aseq[5][0]).AttValue ('GreenTimeDuration'), 11+Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(Aseq[5][0]).AttValue ('GreenTimeDuration')+Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(Aseq[5][1]).AttValue ('GreenTimeDuration')+ GI11[i][j] ])
                            kokop2.append([8+Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(Aseq[5][0]).AttValue ('GreenTimeDuration') + Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(Aseq[5][0]).AttValue ('GreenTimeDuration') + GI11[i][j], 11+Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(Aseq[5][0]).AttValue ('GreenTimeDuration')+Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(Aseq[5][1]).AttValue ('GreenTimeDuration')+ GI11[i][j-1] + GI11[i][j]])

                              
                        grreenstrat11.append(kokop)

                        grreenenddd11.append(kokop2)





                    ddst=[]
                    varices=[]
                    for i in grreenstrat11:
                        ddst1=[]
                        varices2=[]

                        for j in i:
                            ddst1.append(Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(Aseq[5][2]).AttValue ('distributionincapacity')+Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(Aseq[5][2]).AttValue ('ArrivalRate')*((j[0]-SimSec)/3600)-0.6*GI11[grreenstrat11.index(i)][0])
                            ddst1.append(Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(Aseq[5][3]).AttValue ('distributionincapacity')+Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(Aseq[5][3]).AttValue ('ArrivalRate')*((j[1]-SimSec)/3600)-0.6*GI11[grreenstrat11.index(i)][1])
                            varices2.append(variance(ddst1))
                        ddst.append(ddst1)
                        varices.append(varices2)
                        

                    varices = flatten_list (varices)                    




                    ipip= int(math.floor(varices.index(min(varices))/2))
                    jpjp= int(varices.index(min(varices))- ipip*2)







                    Aseq[5][2]= indexI11[jpjp][0]
                    Aseq[5][3]= indexI11[jpjp][1]

                    f2= open("Aseq.txt","w")
                    f2.write(str(Aseq))
                    f2.write("\n")
                    f2.close()







   

                    Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(Aseq[5][2]).SetAttValue('GreenTimeDuration',GI11[ipip][0])
                    Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(Aseq[5][3]).SetAttValue('GreenTimeDuration',GI11[ipip][1])



                    Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(Aseq[5][2]).SetAttValue('GreenStart',grreenstrat11[ipip][jpjp][0])
                    Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(Aseq[5][3]).SetAttValue('GreenStart',grreenstrat11[ipip][jpjp][1])


    

                    Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(Aseq[5][2]).SetAttValue('GreenEnd',grreenenddd11[ipip][jpjp][0])
                    Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(Aseq[5][3]).SetAttValue('GreenEnd',grreenenddd11[ipip][jpjp][1])






        if Seconds >= Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(Aseq[5][2]).AttValue ('GreenStart')-1:
            if Seconds <= Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(Aseq[5][2]).AttValue ('GreenEnd')-1:
                    Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(Aseq[5][2]).SetAttValue ('SigState','GREEN')
                    Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(Aseq[5][0]).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(Aseq[5][1]).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(Aseq[5][3]).SetAttValue ('SigState','RED')


        if  Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(Aseq[5][2]).AttValue ('SigState') == 'GREEN':
            Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(Aseq[5][0]).SetAttValue ('SigState','RED')
            Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(Aseq[5][1]).SetAttValue ('SigState','RED')
            Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(Aseq[5][3]).SetAttValue ('SigState','RED') 
            if Seconds >= Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(Aseq[5][2]).AttValue ('GreenEnd')-1:
                if Seconds < Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(Aseq[5][2]).AttValue ('GreenEnd')+2:             
                    Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(Aseq[5][3]).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(Aseq[5][0]).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(Aseq[5][1]).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(Aseq[5][2]).SetAttValue ('SigState','RED')


        if Seconds >= Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(Aseq[5][3]).AttValue ('GreenStart')-1:
            if Seconds <= Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(Aseq[5][3]).AttValue ('GreenEnd')-1:
                    Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(Aseq[5][3]).SetAttValue ('SigState','GREEN')
                    Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(Aseq[5][0]).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(Aseq[5][1]).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(Aseq[5][2]).SetAttValue ('SigState','RED')


        if  Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(Aseq[5][3]).AttValue ('SigState') == 'GREEN':
            Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(Aseq[5][0]).SetAttValue ('SigState','RED')
            Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(Aseq[5][1]).SetAttValue ('SigState','RED')
            Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(Aseq[5][2]).SetAttValue ('SigState','RED')
            if Seconds >= Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(Aseq[5][3]).AttValue ('GreenEnd')-1:             
                    Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(Aseq[5][0]).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(Aseq[5][1]).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(Aseq[5][2]).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(Aseq[5][3]).SetAttValue ('SigState','RED')







                    GI11=[[(CLength-12)/4,(CLength-12)/4,(CLength-12)/4,(CLength-12)/4],[(CLength-12)/3,(CLength-12)/3,(CLength-12)/6,(CLength-12)/6],[(CLength-12)/3,(CLength-12)/3,(CLength-12)/6,(CLength-12)/6], [(CLength-12)/2,(CLength-12)/6,(CLength-12)/6,(CLength-12)/6],[(CLength-12)/4,(CLength-12)/4,(CLength-12)/4,(CLength-12)/4],[(CLength-12)/3,(CLength-12)/3,(CLength-12)/6,(CLength-12)/6],[(CLength-12)/3,(CLength-12)/3,(CLength-12)/6,(CLength-12)/6], [(CLength-12)/2,(CLength-12)/6,(CLength-12)/6,(CLength-12)/6],[(CLength-12)/4,(CLength-12)/4,(CLength-12)/4,(CLength-12)/4],[(CLength-12)/3,(CLength-12)/3,(CLength-12)/6,(CLength-12)/6],[(CLength-12)/3,(CLength-12)/3,(CLength-12)/6,(CLength-12)/6], [(CLength-12)/2,(CLength-12)/6,(CLength-12)/6,(CLength-12)/6],[(CLength-12)/4,(CLength-12)/4,(CLength-12)/4,(CLength-12)/4],[(CLength-12)/3,(CLength-12)/3,(CLength-12)/6,(CLength-12)/6],[(CLength-12)/3,(CLength-12)/3,(CLength-12)/6,(CLength-12)/6], [(CLength-12)/2,(CLength-12)/6,(CLength-12)/6,(CLength-12)/6],[(CLength-12)/4,(CLength-12)/4,(CLength-12)/4,(CLength-12)/4],[(CLength-12)/3,(CLength-12)/3,(CLength-12)/6,(CLength-12)/6],[(CLength-12)/3,(CLength-12)/3,(CLength-12)/6,(CLength-12)/6], [(CLength-12)/2,(CLength-12)/6,(CLength-12)/6,(CLength-12)/6],[(CLength-12)/4,(CLength-12)/4,(CLength-12)/4,(CLength-12)/4],[(CLength-12)/3,(CLength-12)/3,(CLength-12)/6,(CLength-12)/6],[(CLength-12)/3,(CLength-12)/3,(CLength-12)/6,(CLength-12)/6], [(CLength-12)/2,(CLength-12)/6,(CLength-12)/6,(CLength-12)/6]]
                    indexI11=permutation([Aseq[5][0],Aseq[5][1],Aseq[5][2],Aseq[5][3]])
                    grreenstrat11=[]
                    grreenenddd11=[]
                    for i in range(len(GI11)):
                        kokop=[]
                        kokop2=[]
                        for j in range(len(GI11[i])):
                            kokop.append([2, 5+GI11[i][j-3], 8+GI11[i][j-3]+GI11[i][j-2], 11+GI11[i][j-3]+GI11[i][j-2] +GI11[i][j-1]])
                            kokop2.append([2+GI11[i][j-3], 5+GI11[i][j-3]+GI11[i][j-2], 8+GI11[i][j-3]+GI11[i][j-2]+GI11[i][j-1], 11 +GI11[i][j-3]+GI11[i][j-2]+GI11[i][j-1] +GI11[i][j]])
 
                        grreenstrat11.append(kokop)
                        grreenenddd11.append(kokop2)




                    ddst=[]
                    varices=[]
                    for i in grreenstrat11:
                        ddst1=[]
                        varices2=[]

                        for j in i:
                            ddst1.append(Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(Aseq[5][0]).AttValue ('distributionincapacity')+Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(Aseq[5][0]).AttValue ('ArrivalRate')*((j[0]-SimSec)/3600)-0.6*GI11[grreenstrat11.index(i)][0])
                            ddst1.append(Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(Aseq[5][1]).AttValue ('distributionincapacity')+Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(Aseq[5][1]).AttValue ('ArrivalRate')*((j[1]-SimSec)/3600)-0.6*GI11[grreenstrat11.index(i)][1])
                            ddst1.append(Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(Aseq[5][2]).AttValue ('distributionincapacity')+Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(Aseq[5][2]).AttValue ('ArrivalRate')*((j[2]-SimSec)/3600)-0.6*GI11[grreenstrat11.index(i)][2])
                            ddst1.append(Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(Aseq[5][3]).AttValue ('distributionincapacity')+Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(Aseq[5][3]).AttValue ('ArrivalRate')*((j[3]-SimSec)/3600)-0.6*GI11[grreenstrat11.index(i)][3])
                            varices2.append(variance(ddst1))
                        ddst.append(ddst1)
                        varices.append(varices2)

                    varices = flatten_list (varices)                    




                    ipip= int(math.floor(varices.index(min(varices))/4))
                    jpjp= int(varices.index(min(varices))- ipip*4)






                    Aseq[5][0]= indexI11[jpjp][0]
                    Aseq[5][1]= indexI11[jpjp][1]
                    Aseq[5][2]= indexI11[jpjp][2]
                    Aseq[5][3]= indexI11[jpjp][3]

                    f2= open("Aseq.txt","w")
                    f2.write(str(Aseq))
                    f2.write("\n")
                    f2.close()



                    Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(Aseq[5][0]).SetAttValue('GreenTimeDuration',GI11[ipip][0])   
                    Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(Aseq[5][1]).SetAttValue('GreenTimeDuration',GI11[ipip][1])
                    Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(Aseq[5][2]).SetAttValue('GreenTimeDuration',GI11[ipip][2])
                    Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(Aseq[5][3]).SetAttValue('GreenTimeDuration',GI11[ipip][3])



                    Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(Aseq[5][0]).SetAttValue('GreenStart',grreenstrat11[ipip][jpjp][0])     
                    Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(Aseq[5][1]).SetAttValue('GreenStart',grreenstrat11[ipip][jpjp][1])
                    Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(Aseq[5][2]).SetAttValue('GreenStart',grreenstrat11[ipip][jpjp][2])
                    Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(Aseq[5][3]).SetAttValue('GreenStart',grreenstrat11[ipip][jpjp][3])


                    Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(Aseq[5][0]).SetAttValue('GreenEnd',grreenenddd11[ipip][jpjp][0])    
                    Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(Aseq[5][1]).SetAttValue('GreenEnd',grreenenddd11[ipip][jpjp][1])
                    Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(Aseq[5][2]).SetAttValue('GreenEnd',grreenenddd11[ipip][jpjp][2])
                    Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(Aseq[5][3]).SetAttValue('GreenEnd',grreenenddd11[ipip][jpjp][3])









                        































        if  Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(Aseq[3][0]).AttValue ('SigState') == 'GREEN':
            Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(Aseq[3][1]).SetAttValue ('SigState','RED')
            Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(Aseq[3][2]).SetAttValue ('SigState','RED')
            Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(Aseq[3][3]).SetAttValue ('SigState','RED')
            if Seconds >= Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(Aseq[3][0]).AttValue ('GreenEnd')-1:
                if Seconds < Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(Aseq[3][0]).AttValue ('GreenEnd')+2:
                    Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(Aseq[3][1]).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(Aseq[3][0]).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(Aseq[3][2]).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(Aseq[3][3]).SetAttValue ('SigState','RED')

                    GI11=[[(CLength-12-Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(Aseq[3][0]).AttValue ('GreenTimeDuration'))/3,(CLength-12-Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(Aseq[3][0]).AttValue ('GreenTimeDuration'))/3,(CLength-12-Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(Aseq[3][0]).AttValue ('GreenTimeDuration'))/3], [(CLength-12-Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(Aseq[3][0]).AttValue ('GreenTimeDuration'))/4,(CLength-12-Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(Aseq[3][0]).AttValue ('GreenTimeDuration'))/4,(CLength-12-Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(Aseq[3][0]).AttValue ('GreenTimeDuration'))/2],[(CLength-12-Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(Aseq[3][0]).AttValue ('GreenTimeDuration'))/4,(CLength-12-Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(Aseq[3][0]).AttValue ('GreenTimeDuration'))/2,(CLength-12-Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(Aseq[3][0]).AttValue ('GreenTimeDuration'))/4],[(CLength-12-Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(Aseq[3][0]).AttValue ('GreenTimeDuration'))/5,3*(CLength-12-Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(Aseq[3][0]).AttValue ('GreenTimeDuration'))/5,(CLength-12-Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(Aseq[3][0]).AttValue ('GreenTimeDuration'))/5],[(CLength-12-Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(Aseq[3][0]).AttValue ('GreenTimeDuration'))/6,4*(CLength-12-Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(Aseq[3][0]).AttValue ('GreenTimeDuration'))/6,(CLength-12-Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(Aseq[3][0]).AttValue ('GreenTimeDuration'))/6],[(CLength-12-Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(Aseq[3][0]).AttValue ('GreenTimeDuration'))/7,5*(CLength-12-Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(Aseq[3][0]).AttValue ('GreenTimeDuration'))/7,(CLength-12-Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(Aseq[3][0]).AttValue ('GreenTimeDuration'))/7]]
                    indexI11=permutation([Aseq[3][1],Aseq[3][2],Aseq[3][3]])
                    grreenstrat11=[]
                    grreenenddd11=[]
                    for i in range(len(GI11)):
                        kokop=[]
                        kokop2=[]
                        for j in range(len(GI11[i])):
                            kokop.append([5+Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(Aseq[3][0]).AttValue ('GreenTimeDuration'), 8+Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(Aseq[3][0]).AttValue ('GreenTimeDuration')+GI11[i][j], 11+Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(Aseq[3][0]).AttValue ('GreenTimeDuration')+GI11[i][j ] +GI11[i][j-1]])
                            kokop2.append([5+Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(Aseq[3][0]).AttValue ('GreenTimeDuration')+GI11[i][j], 8+Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(Aseq[3][0]).AttValue ('GreenTimeDuration')+GI11[i][j-1] +GI11[i][j], 11+Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(Aseq[3][0]).AttValue ('GreenTimeDuration')+GI11[i][j ] +GI11[i][j-1]+GI11[i][j]])
                              
                        grreenstrat11.append(kokop)

                        grreenenddd11.append(kokop2)






                    ddst=[]
                    varices=[]
                    for i in grreenstrat11:
                        ddst1=[]
                        varices2=[]

                        for j in i:
                            ddst1.append(Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(Aseq[3][1]).AttValue ('distributionincapacity')+Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(Aseq[3][1]).AttValue ('ArrivalRate')*((j[0]-SimSec)/3600)-0.4*GI11[grreenstrat11.index(i)][0])
                            ddst1.append(Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(Aseq[3][2]).AttValue ('distributionincapacity')+Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(Aseq[3][2]).AttValue ('ArrivalRate')*((j[1]-SimSec)/3600)-0.4*GI11[grreenstrat11.index(i)][1])
                            ddst1.append(Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(Aseq[3][3]).AttValue ('distributionincapacity')+Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(Aseq[3][3]).AttValue ('ArrivalRate')*((j[2]-SimSec)/3600)-0.4*GI11[grreenstrat11.index(i)][2])
                            varices2.append(variance(ddst1))
                        ddst.append(ddst1)
                        varices.append(varices2)
                        



                    varices = flatten_list (varices)                    




                    ipip= int(math.floor(varices.index(min(varices))/3))
                    jpjp= int(varices.index(min(varices))- ipip*3)


                    Aseq[3][1]= indexI11[jpjp][0]
                    Aseq[3][2]= indexI11[jpjp][1]
                    Aseq[3][3]= indexI11[jpjp][2]

                    f2= open("Aseq.txt","w")
                    f2.write(str(Aseq))
                    f2.write("\n")
                    f2.close()






   
                    Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(Aseq[3][1]).SetAttValue('GreenTimeDuration',GI11[ipip][0])
                    Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(Aseq[3][2]).SetAttValue('GreenTimeDuration',GI11[ipip][1])
                    Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(Aseq[3][3]).SetAttValue('GreenTimeDuration',GI11[ipip][2])


     
                    Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(Aseq[3][1]).SetAttValue('GreenStart',grreenstrat11[ipip][jpjp][0])
                    Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(Aseq[3][2]).SetAttValue('GreenStart',grreenstrat11[ipip][jpjp][1])
                    Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(Aseq[3][3]).SetAttValue('GreenStart',grreenstrat11[ipip][jpjp][2])


    
                    Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(Aseq[3][1]).SetAttValue('GreenEnd',grreenenddd11[ipip][jpjp][0])
                    Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(Aseq[3][2]).SetAttValue('GreenEnd',grreenenddd11[ipip][jpjp][1])
                    Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(Aseq[3][3]).SetAttValue('GreenEnd',grreenenddd11[ipip][jpjp][2])




        if Seconds >= Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(Aseq[3][1]).AttValue ('GreenStart')-1:
            if Seconds <= Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(Aseq[3][1]).AttValue ('GreenEnd')-1:
                    Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(Aseq[3][1]).SetAttValue ('SigState','GREEN')
                    Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(Aseq[3][0]).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(Aseq[3][2]).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(Aseq[3][3]).SetAttValue ('SigState','RED')


        if  Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(Aseq[3][1]).AttValue ('SigState') == 'GREEN':
            Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(Aseq[3][0]).SetAttValue ('SigState','RED')
            Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(Aseq[3][2]).SetAttValue ('SigState','RED')
            Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(Aseq[3][3]).SetAttValue ('SigState','RED')             
            if Seconds >= Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(Aseq[3][1]).AttValue ('GreenEnd')-1:
                if Seconds < Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(Aseq[3][1]).AttValue ('GreenEnd')+2:                 
                    Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(Aseq[3][2]).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(Aseq[3][0]).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(Aseq[3][1]).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(Aseq[3][3]).SetAttValue ('SigState','RED')


                    GI11=[[(CLength-12-Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(Aseq[3][0]).AttValue ('GreenTimeDuration')-Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(Aseq[3][1]).AttValue ('GreenTimeDuration'))/2,(CLength-12-Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(Aseq[3][0]).AttValue ('GreenTimeDuration')-Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(Aseq[3][1]).AttValue ('GreenTimeDuration'))/2],[2*(CLength-12-Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(Aseq[3][0]).AttValue ('GreenTimeDuration')-Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(Aseq[3][1]).AttValue ('GreenTimeDuration'))/3,(CLength-12-Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(Aseq[3][0]).AttValue ('GreenTimeDuration')-Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(Aseq[3][1]).AttValue ('GreenTimeDuration'))/3]]
                    indexI11=permutation([Aseq[3][2],Aseq[3][3]])
                    grreenstrat11=[]
                    grreenenddd11=[]
                    for i in range(len(GI11)):
                        kokop=[]
                        kokop2=[]
                        for j in range(len(GI11[i])):

                            kokop.append([8+Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(Aseq[3][0]).AttValue ('GreenTimeDuration') + Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(Aseq[3][0]).AttValue ('GreenTimeDuration'), 11+Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(Aseq[3][0]).AttValue ('GreenTimeDuration')+Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(Aseq[3][1]).AttValue ('GreenTimeDuration')+ GI11[i][j] ])
                            kokop2.append([8+Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(Aseq[3][0]).AttValue ('GreenTimeDuration') + Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(Aseq[3][0]).AttValue ('GreenTimeDuration') + GI11[i][j], 11+Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(Aseq[3][0]).AttValue ('GreenTimeDuration')+Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(Aseq[3][1]).AttValue ('GreenTimeDuration')+ GI11[i][j-1] + GI11[i][j]])

                              
                        grreenstrat11.append(kokop)

                        grreenenddd11.append(kokop2)





                    ddst=[]
                    varices=[]
                    for i in grreenstrat11:
                        ddst1=[]
                        varices2=[]

                        for j in i:
                            ddst1.append(Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(Aseq[3][2]).AttValue ('distributionincapacity')+Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(Aseq[3][2]).AttValue ('ArrivalRate')*((j[0]-SimSec)/3600)-0.4*GI11[grreenstrat11.index(i)][0])
                            ddst1.append(Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(Aseq[3][3]).AttValue ('distributionincapacity')+Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(Aseq[3][3]).AttValue ('ArrivalRate')*((j[1]-SimSec)/3600)-0.4*GI11[grreenstrat11.index(i)][1])
                            varices2.append(variance(ddst1))
                        ddst.append(ddst1)
                        varices.append(varices2)
                        

                    varices = flatten_list (varices)                    




                    ipip= int(math.floor(varices.index(min(varices))/2))
                    jpjp= int(varices.index(min(varices))- ipip*2)







                    Aseq[3][2]= indexI11[jpjp][0]
                    Aseq[3][3]= indexI11[jpjp][1]

                    f2= open("Aseq.txt","w")
                    f2.write(str(Aseq))
                    f2.write("\n")
                    f2.close()







   

                    Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(Aseq[3][2]).SetAttValue('GreenTimeDuration',GI11[ipip][0])
                    Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(Aseq[3][3]).SetAttValue('GreenTimeDuration',GI11[ipip][1])



                    Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(Aseq[3][2]).SetAttValue('GreenStart',grreenstrat11[ipip][jpjp][0])
                    Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(Aseq[3][3]).SetAttValue('GreenStart',grreenstrat11[ipip][jpjp][1])


    

                    Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(Aseq[3][2]).SetAttValue('GreenEnd',grreenenddd11[ipip][jpjp][0])
                    Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(Aseq[3][3]).SetAttValue('GreenEnd',grreenenddd11[ipip][jpjp][1])






        if Seconds >= Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(Aseq[3][2]).AttValue ('GreenStart')-1:
            if Seconds <= Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(Aseq[3][2]).AttValue ('GreenEnd')-1:
                    Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(Aseq[3][2]).SetAttValue ('SigState','GREEN')
                    Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(Aseq[3][0]).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(Aseq[3][1]).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(Aseq[3][3]).SetAttValue ('SigState','RED')


        if  Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(Aseq[3][2]).AttValue ('SigState') == 'GREEN':
            Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(Aseq[3][0]).SetAttValue ('SigState','RED')
            Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(Aseq[3][1]).SetAttValue ('SigState','RED')
            Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(Aseq[3][3]).SetAttValue ('SigState','RED') 
            if Seconds >= Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(Aseq[3][2]).AttValue ('GreenEnd')-1:
                if Seconds < Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(Aseq[3][2]).AttValue ('GreenEnd')+2:             
                    Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(Aseq[3][3]).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(Aseq[3][0]).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(Aseq[3][1]).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(Aseq[3][2]).SetAttValue ('SigState','RED')


        if Seconds >= Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(Aseq[3][3]).AttValue ('GreenStart')-1:
            if Seconds <= Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(Aseq[3][3]).AttValue ('GreenEnd')-1:
                    Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(Aseq[3][3]).SetAttValue ('SigState','GREEN')
                    Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(Aseq[3][0]).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(Aseq[3][1]).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(Aseq[3][2]).SetAttValue ('SigState','RED')


        if  Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(Aseq[3][3]).AttValue ('SigState') == 'GREEN':
            Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(Aseq[3][0]).SetAttValue ('SigState','RED')
            Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(Aseq[3][1]).SetAttValue ('SigState','RED')
            Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(Aseq[3][2]).SetAttValue ('SigState','RED')
            if Seconds >= Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(Aseq[3][3]).AttValue ('GreenEnd')-1:             
                    Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(Aseq[3][0]).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(Aseq[3][1]).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(Aseq[3][2]).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(Aseq[3][3]).SetAttValue ('SigState','RED')






                    GI11=[[(CLength-12)/4,(CLength-12)/4,(CLength-12)/4,(CLength-12)/4],[(CLength-12)/3,(CLength-12)/3,(CLength-12)/6,(CLength-12)/6],[(CLength-12)/3,(CLength-12)/3,(CLength-12)/6,(CLength-12)/6], [(CLength-12)/2,(CLength-12)/6,(CLength-12)/6,(CLength-12)/6],[(CLength-12)/4,(CLength-12)/4,(CLength-12)/4,(CLength-12)/4],[(CLength-12)/3,(CLength-12)/3,(CLength-12)/6,(CLength-12)/6],[(CLength-12)/3,(CLength-12)/3,(CLength-12)/6,(CLength-12)/6], [(CLength-12)/2,(CLength-12)/6,(CLength-12)/6,(CLength-12)/6],[(CLength-12)/4,(CLength-12)/4,(CLength-12)/4,(CLength-12)/4],[(CLength-12)/3,(CLength-12)/3,(CLength-12)/6,(CLength-12)/6],[(CLength-12)/3,(CLength-12)/3,(CLength-12)/6,(CLength-12)/6], [(CLength-12)/2,(CLength-12)/6,(CLength-12)/6,(CLength-12)/6],[(CLength-12)/4,(CLength-12)/4,(CLength-12)/4,(CLength-12)/4],[(CLength-12)/3,(CLength-12)/3,(CLength-12)/6,(CLength-12)/6],[(CLength-12)/3,(CLength-12)/3,(CLength-12)/6,(CLength-12)/6], [(CLength-12)/2,(CLength-12)/6,(CLength-12)/6,(CLength-12)/6],[(CLength-12)/4,(CLength-12)/4,(CLength-12)/4,(CLength-12)/4],[(CLength-12)/3,(CLength-12)/3,(CLength-12)/6,(CLength-12)/6],[(CLength-12)/3,(CLength-12)/3,(CLength-12)/6,(CLength-12)/6], [(CLength-12)/2,(CLength-12)/6,(CLength-12)/6,(CLength-12)/6],[(CLength-12)/4,(CLength-12)/4,(CLength-12)/4,(CLength-12)/4],[(CLength-12)/3,(CLength-12)/3,(CLength-12)/6,(CLength-12)/6],[(CLength-12)/3,(CLength-12)/3,(CLength-12)/6,(CLength-12)/6], [(CLength-12)/2,(CLength-12)/6,(CLength-12)/6,(CLength-12)/6]]
                    indexI11=permutation([Aseq[3][0],Aseq[3][1],Aseq[3][2],Aseq[3][3]])
                    grreenstrat11=[]
                    grreenenddd11=[]
                    for i in range(len(GI11)):
                        kokop=[]
                        kokop2=[]
                        for j in range(len(GI11[i])):
                            kokop.append([2, 5+GI11[i][j-3], 8+GI11[i][j-3]+GI11[i][j-2], 11+GI11[i][j-3]+GI11[i][j-2] +GI11[i][j-1]])
                            kokop2.append([2+GI11[i][j-3], 5+GI11[i][j-3]+GI11[i][j-2], 8+GI11[i][j-3]+GI11[i][j-2]+GI11[i][j-1], 11 +GI11[i][j-3]+GI11[i][j-2]+GI11[i][j-1] +GI11[i][j]])
 
                        grreenstrat11.append(kokop)
                        grreenenddd11.append(kokop2)




                    ddst=[]
                    varices=[]
                    for i in grreenstrat11:
                        ddst1=[]
                        varices2=[]

                        for j in i:
                            ddst1.append(Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(Aseq[3][0]).AttValue ('distributionincapacity')+Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(Aseq[3][0]).AttValue ('ArrivalRate')*((j[0]-SimSec)/3600)-0.4*GI11[grreenstrat11.index(i)][0])
                            ddst1.append(Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(Aseq[3][1]).AttValue ('distributionincapacity')+Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(Aseq[3][1]).AttValue ('ArrivalRate')*((j[1]-SimSec)/3600)-0.4*GI11[grreenstrat11.index(i)][1])
                            ddst1.append(Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(Aseq[3][2]).AttValue ('distributionincapacity')+Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(Aseq[3][2]).AttValue ('ArrivalRate')*((j[2]-SimSec)/3600)-0.4*GI11[grreenstrat11.index(i)][2])
                            ddst1.append(Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(Aseq[3][3]).AttValue ('distributionincapacity')+Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(Aseq[3][3]).AttValue ('ArrivalRate')*((j[3]-SimSec)/3600)-0.4*GI11[grreenstrat11.index(i)][3])
                            varices2.append(variance(ddst1))
                        ddst.append(ddst1)
                        varices.append(varices2)

                    varices = flatten_list (varices)                    




                    ipip= int(math.floor(varices.index(min(varices))/4))
                    jpjp= int(varices.index(min(varices))- ipip*4)






                    Aseq[3][0]= indexI11[jpjp][0]
                    Aseq[3][1]= indexI11[jpjp][1]
                    Aseq[3][2]= indexI11[jpjp][2]
                    Aseq[3][3]= indexI11[jpjp][3]

                    f2= open("Aseq.txt","w")
                    f2.write(str(Aseq))
                    f2.write("\n")
                    f2.close()



                    Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(Aseq[3][0]).SetAttValue('GreenTimeDuration',GI11[ipip][0])   
                    Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(Aseq[3][1]).SetAttValue('GreenTimeDuration',GI11[ipip][1])
                    Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(Aseq[3][2]).SetAttValue('GreenTimeDuration',GI11[ipip][2])
                    Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(Aseq[3][3]).SetAttValue('GreenTimeDuration',GI11[ipip][3])



                    Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(Aseq[3][0]).SetAttValue('GreenStart',grreenstrat11[ipip][jpjp][0])     
                    Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(Aseq[3][1]).SetAttValue('GreenStart',grreenstrat11[ipip][jpjp][1])
                    Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(Aseq[3][2]).SetAttValue('GreenStart',grreenstrat11[ipip][jpjp][2])
                    Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(Aseq[3][3]).SetAttValue('GreenStart',grreenstrat11[ipip][jpjp][3])


                    Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(Aseq[3][0]).SetAttValue('GreenEnd',grreenenddd11[ipip][jpjp][0])    
                    Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(Aseq[3][1]).SetAttValue('GreenEnd',grreenenddd11[ipip][jpjp][1])
                    Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(Aseq[3][2]).SetAttValue('GreenEnd',grreenenddd11[ipip][jpjp][2])
                    Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(Aseq[3][3]).SetAttValue('GreenEnd',grreenenddd11[ipip][jpjp][3])









                        



































        if  Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(Aseq[2][0]).AttValue ('SigState') == 'GREEN':
            Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(Aseq[2][1]).SetAttValue ('SigState','RED')
            Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(Aseq[2][2]).SetAttValue ('SigState','RED')
            Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(Aseq[2][3]).SetAttValue ('SigState','RED')
            if Seconds >= Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(Aseq[2][0]).AttValue ('GreenEnd')-1:
                if Seconds < Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(Aseq[2][0]).AttValue ('GreenEnd')+2:
                    Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(Aseq[2][1]).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(Aseq[2][0]).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(Aseq[2][2]).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(Aseq[2][3]).SetAttValue ('SigState','RED')


                    GI11=[[(CLength-12-Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(Aseq[2][0]).AttValue ('GreenTimeDuration'))/3,(CLength-12-Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(Aseq[2][0]).AttValue ('GreenTimeDuration'))/3,(CLength-12-Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(Aseq[2][0]).AttValue ('GreenTimeDuration'))/3], [(CLength-12-Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(Aseq[2][0]).AttValue ('GreenTimeDuration'))/4,(CLength-12-Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(Aseq[2][0]).AttValue ('GreenTimeDuration'))/4,(CLength-12-Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(Aseq[2][0]).AttValue ('GreenTimeDuration'))/2],[(CLength-12-Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(Aseq[2][0]).AttValue ('GreenTimeDuration'))/4,(CLength-12-Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(Aseq[2][0]).AttValue ('GreenTimeDuration'))/2,(CLength-12-Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(Aseq[2][0]).AttValue ('GreenTimeDuration'))/4],[(CLength-12-Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(Aseq[2][0]).AttValue ('GreenTimeDuration'))/5,3*(CLength-12-Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(Aseq[2][0]).AttValue ('GreenTimeDuration'))/5,(CLength-12-Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(Aseq[2][0]).AttValue ('GreenTimeDuration'))/5],[(CLength-12-Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(Aseq[2][0]).AttValue ('GreenTimeDuration'))/6,4*(CLength-12-Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(Aseq[2][0]).AttValue ('GreenTimeDuration'))/6,(CLength-12-Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(Aseq[2][0]).AttValue ('GreenTimeDuration'))/6],[(CLength-12-Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(Aseq[2][0]).AttValue ('GreenTimeDuration'))/7,5*(CLength-12-Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(Aseq[2][0]).AttValue ('GreenTimeDuration'))/7,(CLength-12-Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(Aseq[2][0]).AttValue ('GreenTimeDuration'))/7]]
                    indexI11=permutation([Aseq[2][1],Aseq[2][2],Aseq[2][3]])
                    grreenstrat11=[]
                    grreenenddd11=[]
                    for i in range(len(GI11)):
                        kokop=[]
                        kokop2=[]
                        for j in range(len(GI11[i])):
                            kokop.append([5+Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(Aseq[2][0]).AttValue ('GreenTimeDuration'), 8+Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(Aseq[2][0]).AttValue ('GreenTimeDuration')+GI11[i][j], 11+Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(Aseq[2][0]).AttValue ('GreenTimeDuration')+GI11[i][j ] +GI11[i][j-1]])
                            kokop2.append([5+Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(Aseq[2][0]).AttValue ('GreenTimeDuration')+GI11[i][j], 8+Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(Aseq[2][0]).AttValue ('GreenTimeDuration')+GI11[i][j-1] +GI11[i][j], 11+Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(Aseq[2][0]).AttValue ('GreenTimeDuration')+GI11[i][j ] +GI11[i][j-1]+GI11[i][j]])
                              
                        grreenstrat11.append(kokop)

                        grreenenddd11.append(kokop2)






                    ddst=[]
                    varices=[]
                    for i in grreenstrat11:
                        ddst1=[]
                        varices2=[]

                        for j in i:
                            ddst1.append(Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(Aseq[2][1]).AttValue ('distributionincapacity')+Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(Aseq[2][1]).AttValue ('ArrivalRate')*((j[0]-SimSec)/3600)-0.3*GI11[grreenstrat11.index(i)][0])
                            ddst1.append(Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(Aseq[2][2]).AttValue ('distributionincapacity')+Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(Aseq[2][2]).AttValue ('ArrivalRate')*((j[1]-SimSec)/3600)-0.3*GI11[grreenstrat11.index(i)][1])
                            ddst1.append(Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(Aseq[2][3]).AttValue ('distributionincapacity')+Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(Aseq[2][3]).AttValue ('ArrivalRate')*((j[2]-SimSec)/3600)-0.3*GI11[grreenstrat11.index(i)][2])
                            varices2.append(variance(ddst1))
                        ddst.append(ddst1)
                        varices.append(varices2)
                        



                    varices = flatten_list (varices)                    




                    ipip= int(math.floor(varices.index(min(varices))/3))
                    jpjp= int(varices.index(min(varices))- ipip*3)


                    Aseq[2][1]= indexI11[jpjp][0]
                    Aseq[2][2]= indexI11[jpjp][1]
                    Aseq[2][3]= indexI11[jpjp][2]

                    f2= open("Aseq.txt","w")
                    f2.write(str(Aseq))
                    f2.write("\n")
                    f2.close()






   
                    Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(Aseq[2][1]).SetAttValue('GreenTimeDuration',GI11[ipip][0])
                    Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(Aseq[2][2]).SetAttValue('GreenTimeDuration',GI11[ipip][1])
                    Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(Aseq[2][3]).SetAttValue('GreenTimeDuration',GI11[ipip][2])


     
                    Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(Aseq[2][1]).SetAttValue('GreenStart',grreenstrat11[ipip][jpjp][0])
                    Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(Aseq[2][2]).SetAttValue('GreenStart',grreenstrat11[ipip][jpjp][1])
                    Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(Aseq[2][3]).SetAttValue('GreenStart',grreenstrat11[ipip][jpjp][2])


    
                    Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(Aseq[2][1]).SetAttValue('GreenEnd',grreenenddd11[ipip][jpjp][0])
                    Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(Aseq[2][2]).SetAttValue('GreenEnd',grreenenddd11[ipip][jpjp][1])
                    Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(Aseq[2][3]).SetAttValue('GreenEnd',grreenenddd11[ipip][jpjp][2])







        if Seconds >= Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(Aseq[2][1]).AttValue ('GreenStart')-1:
            if Seconds <= Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(Aseq[2][1]).AttValue ('GreenEnd')-1:
                    Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(Aseq[2][1]).SetAttValue ('SigState','GREEN')
                    Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(Aseq[2][0]).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(Aseq[2][2]).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(Aseq[2][3]).SetAttValue ('SigState','RED')


        if  Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(Aseq[2][1]).AttValue ('SigState') == 'GREEN':
            Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(Aseq[2][0]).SetAttValue ('SigState','RED')
            Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(Aseq[2][2]).SetAttValue ('SigState','RED')
            Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(Aseq[2][3]).SetAttValue ('SigState','RED')             
            if Seconds >= Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(Aseq[2][1]).AttValue ('GreenEnd')-1:
                if Seconds < Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(Aseq[2][1]).AttValue ('GreenEnd')+2:                 
                    Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(Aseq[2][2]).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(Aseq[2][0]).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(Aseq[2][1]).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(Aseq[2][3]).SetAttValue ('SigState','RED')


                    GI11=[[(CLength-12-Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(Aseq[2][0]).AttValue ('GreenTimeDuration')-Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(Aseq[2][1]).AttValue ('GreenTimeDuration'))/2,(CLength-12-Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(Aseq[2][0]).AttValue ('GreenTimeDuration')-Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(Aseq[2][1]).AttValue ('GreenTimeDuration'))/2],[2*(CLength-12-Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(Aseq[2][0]).AttValue ('GreenTimeDuration')-Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(Aseq[2][1]).AttValue ('GreenTimeDuration'))/3,(CLength-12-Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(Aseq[2][0]).AttValue ('GreenTimeDuration')-Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(Aseq[2][1]).AttValue ('GreenTimeDuration'))/3]]
                    indexI11=permutation([Aseq[2][2],Aseq[2][3]])
                    grreenstrat11=[]
                    grreenenddd11=[]
                    for i in range(len(GI11)):
                        kokop=[]
                        kokop2=[]
                        for j in range(len(GI11[i])):

                            kokop.append([8+Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(Aseq[2][0]).AttValue ('GreenTimeDuration') + Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(Aseq[2][0]).AttValue ('GreenTimeDuration'), 11+Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(Aseq[2][0]).AttValue ('GreenTimeDuration')+Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(Aseq[2][1]).AttValue ('GreenTimeDuration')+ GI11[i][j] ])
                            kokop2.append([8+Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(Aseq[2][0]).AttValue ('GreenTimeDuration') + Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(Aseq[2][0]).AttValue ('GreenTimeDuration') + GI11[i][j], 11+Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(Aseq[2][0]).AttValue ('GreenTimeDuration')+Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(Aseq[2][1]).AttValue ('GreenTimeDuration')+ GI11[i][j-1] + GI11[i][j]])

                              
                        grreenstrat11.append(kokop)

                        grreenenddd11.append(kokop2)





                    ddst=[]
                    varices=[]
                    for i in grreenstrat11:
                        ddst1=[]
                        varices2=[]

                        for j in i:
                            ddst1.append(Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(Aseq[2][2]).AttValue ('distributionincapacity')+Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(Aseq[2][2]).AttValue ('ArrivalRate')*((j[0]-SimSec)/3600)-0.3*GI11[grreenstrat11.index(i)][0])
                            ddst1.append(Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(Aseq[2][3]).AttValue ('distributionincapacity')+Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(Aseq[2][3]).AttValue ('ArrivalRate')*((j[1]-SimSec)/3600)-0.3*GI11[grreenstrat11.index(i)][1])
                            varices2.append(variance(ddst1))
                        ddst.append(ddst1)
                        varices.append(varices2)
                        

                    varices = flatten_list (varices)                    




                    ipip= int(math.floor(varices.index(min(varices))/2))
                    jpjp= int(varices.index(min(varices))- ipip*2)







                    Aseq[2][2]= indexI11[jpjp][0]
                    Aseq[2][3]= indexI11[jpjp][1]

                    f2= open("Aseq.txt","w")
                    f2.write(str(Aseq))
                    f2.write("\n")
                    f2.close()







   

                    Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(Aseq[2][2]).SetAttValue('GreenTimeDuration',GI11[ipip][0])
                    Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(Aseq[2][3]).SetAttValue('GreenTimeDuration',GI11[ipip][1])



                    Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(Aseq[2][2]).SetAttValue('GreenStart',grreenstrat11[ipip][jpjp][0])
                    Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(Aseq[2][3]).SetAttValue('GreenStart',grreenstrat11[ipip][jpjp][1])


    

                    Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(Aseq[2][2]).SetAttValue('GreenEnd',grreenenddd11[ipip][jpjp][0])
                    Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(Aseq[2][3]).SetAttValue('GreenEnd',grreenenddd11[ipip][jpjp][1])




        if Seconds >= Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(Aseq[2][2]).AttValue ('GreenStart')-1:
            if Seconds <= Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(Aseq[2][2]).AttValue ('GreenEnd')-1:
                    Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(Aseq[2][2]).SetAttValue ('SigState','GREEN')
                    Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(Aseq[2][0]).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(Aseq[2][1]).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(Aseq[2][3]).SetAttValue ('SigState','RED')


        if  Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(Aseq[2][2]).AttValue ('SigState') == 'GREEN':
            Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(Aseq[2][0]).SetAttValue ('SigState','RED')
            Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(Aseq[2][1]).SetAttValue ('SigState','RED')
            Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(Aseq[2][3]).SetAttValue ('SigState','RED') 
            if Seconds >= Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(Aseq[2][2]).AttValue ('GreenEnd')-1:
                if Seconds < Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(Aseq[2][2]).AttValue ('GreenEnd')+2:             
                    Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(Aseq[2][3]).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(Aseq[2][0]).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(Aseq[2][1]).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(Aseq[2][2]).SetAttValue ('SigState','RED')


        if Seconds >= Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(Aseq[2][3]).AttValue ('GreenStart')-1:
            if Seconds <= Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(Aseq[2][3]).AttValue ('GreenEnd')-1:
                    Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(Aseq[2][3]).SetAttValue ('SigState','GREEN')
                    Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(Aseq[2][0]).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(Aseq[2][1]).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(Aseq[2][2]).SetAttValue ('SigState','RED')


        if  Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(Aseq[2][3]).AttValue ('SigState') == 'GREEN':
            Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(Aseq[2][0]).SetAttValue ('SigState','RED')
            Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(Aseq[2][1]).SetAttValue ('SigState','RED')
            Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(Aseq[2][2]).SetAttValue ('SigState','RED')
            if Seconds >= Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(Aseq[2][3]).AttValue ('GreenEnd')-1:             
                    Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(Aseq[2][0]).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(Aseq[2][1]).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(Aseq[2][2]).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(Aseq[2][3]).SetAttValue ('SigState','RED')







                    GI11=[[(CLength-12)/4,(CLength-12)/4,(CLength-12)/4,(CLength-12)/4],[(CLength-12)/3,(CLength-12)/3,(CLength-12)/6,(CLength-12)/6],[(CLength-12)/3,(CLength-12)/3,(CLength-12)/6,(CLength-12)/6], [(CLength-12)/2,(CLength-12)/6,(CLength-12)/6,(CLength-12)/6],[(CLength-12)/4,(CLength-12)/4,(CLength-12)/4,(CLength-12)/4],[(CLength-12)/3,(CLength-12)/3,(CLength-12)/6,(CLength-12)/6],[(CLength-12)/3,(CLength-12)/3,(CLength-12)/6,(CLength-12)/6], [(CLength-12)/2,(CLength-12)/6,(CLength-12)/6,(CLength-12)/6],[(CLength-12)/4,(CLength-12)/4,(CLength-12)/4,(CLength-12)/4],[(CLength-12)/3,(CLength-12)/3,(CLength-12)/6,(CLength-12)/6],[(CLength-12)/3,(CLength-12)/3,(CLength-12)/6,(CLength-12)/6], [(CLength-12)/2,(CLength-12)/6,(CLength-12)/6,(CLength-12)/6],[(CLength-12)/4,(CLength-12)/4,(CLength-12)/4,(CLength-12)/4],[(CLength-12)/3,(CLength-12)/3,(CLength-12)/6,(CLength-12)/6],[(CLength-12)/3,(CLength-12)/3,(CLength-12)/6,(CLength-12)/6], [(CLength-12)/2,(CLength-12)/6,(CLength-12)/6,(CLength-12)/6],[(CLength-12)/4,(CLength-12)/4,(CLength-12)/4,(CLength-12)/4],[(CLength-12)/3,(CLength-12)/3,(CLength-12)/6,(CLength-12)/6],[(CLength-12)/3,(CLength-12)/3,(CLength-12)/6,(CLength-12)/6], [(CLength-12)/2,(CLength-12)/6,(CLength-12)/6,(CLength-12)/6],[(CLength-12)/4,(CLength-12)/4,(CLength-12)/4,(CLength-12)/4],[(CLength-12)/3,(CLength-12)/3,(CLength-12)/6,(CLength-12)/6],[(CLength-12)/3,(CLength-12)/3,(CLength-12)/6,(CLength-12)/6], [(CLength-12)/2,(CLength-12)/6,(CLength-12)/6,(CLength-12)/6]]
                    indexI11=permutation([Aseq[2][0],Aseq[2][1],Aseq[2][2],Aseq[2][3]])
                    grreenstrat11=[]
                    grreenenddd11=[]
                    for i in range(len(GI11)):
                        kokop=[]
                        kokop2=[]
                        for j in range(len(GI11[i])):
                            kokop.append([2, 5+GI11[i][j-3], 8+GI11[i][j-3]+GI11[i][j-2], 11+GI11[i][j-3]+GI11[i][j-2] +GI11[i][j-1]])
                            kokop2.append([2+GI11[i][j-3], 5+GI11[i][j-3]+GI11[i][j-2], 8+GI11[i][j-3]+GI11[i][j-2]+GI11[i][j-1], 11 +GI11[i][j-3]+GI11[i][j-2]+GI11[i][j-1] +GI11[i][j]])
 
                        grreenstrat11.append(kokop)
                        grreenenddd11.append(kokop2)




                    ddst=[]
                    varices=[]
                    for i in grreenstrat11:
                        ddst1=[]
                        varices2=[]

                        for j in i:
                            ddst1.append(Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(Aseq[2][0]).AttValue ('distributionincapacity')+Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(Aseq[2][0]).AttValue ('ArrivalRate')*((j[0]-SimSec)/3600)-0.3*GI11[grreenstrat11.index(i)][0])
                            ddst1.append(Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(Aseq[2][1]).AttValue ('distributionincapacity')+Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(Aseq[2][1]).AttValue ('ArrivalRate')*((j[1]-SimSec)/3600)-0.3*GI11[grreenstrat11.index(i)][1])
                            ddst1.append(Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(Aseq[2][2]).AttValue ('distributionincapacity')+Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(Aseq[2][2]).AttValue ('ArrivalRate')*((j[2]-SimSec)/3600)-0.3*GI11[grreenstrat11.index(i)][2])
                            ddst1.append(Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(Aseq[2][3]).AttValue ('distributionincapacity')+Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(Aseq[2][3]).AttValue ('ArrivalRate')*((j[3]-SimSec)/3600)-0.3*GI11[grreenstrat11.index(i)][3])
                            varices2.append(variance(ddst1))
                        ddst.append(ddst1)
                        varices.append(varices2)

                    varices = flatten_list (varices)                    




                    ipip= int(math.floor(varices.index(min(varices))/4))
                    jpjp= int(varices.index(min(varices))- ipip*4)






                    Aseq[2][0]= indexI11[jpjp][0]
                    Aseq[2][1]= indexI11[jpjp][1]
                    Aseq[2][2]= indexI11[jpjp][2]
                    Aseq[2][3]= indexI11[jpjp][3]

                    f2= open("Aseq.txt","w")
                    f2.write(str(Aseq))
                    f2.write("\n")
                    f2.close()



                    Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(Aseq[2][0]).SetAttValue('GreenTimeDuration',GI11[ipip][0])   
                    Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(Aseq[2][1]).SetAttValue('GreenTimeDuration',GI11[ipip][1])
                    Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(Aseq[2][2]).SetAttValue('GreenTimeDuration',GI11[ipip][2])
                    Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(Aseq[2][3]).SetAttValue('GreenTimeDuration',GI11[ipip][3])



                    Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(Aseq[2][0]).SetAttValue('GreenStart',grreenstrat11[ipip][jpjp][0])     
                    Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(Aseq[2][1]).SetAttValue('GreenStart',grreenstrat11[ipip][jpjp][1])
                    Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(Aseq[2][2]).SetAttValue('GreenStart',grreenstrat11[ipip][jpjp][2])
                    Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(Aseq[2][3]).SetAttValue('GreenStart',grreenstrat11[ipip][jpjp][3])


                    Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(Aseq[2][0]).SetAttValue('GreenEnd',grreenenddd11[ipip][jpjp][0])    
                    Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(Aseq[2][1]).SetAttValue('GreenEnd',grreenenddd11[ipip][jpjp][1])
                    Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(Aseq[2][2]).SetAttValue('GreenEnd',grreenenddd11[ipip][jpjp][2])
                    Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(Aseq[2][3]).SetAttValue('GreenEnd',grreenenddd11[ipip][jpjp][3])









                        





























        if  Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(Aseq[1][0]).AttValue ('SigState') == 'GREEN':
            Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(Aseq[1][1]).SetAttValue ('SigState','RED')
            Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(Aseq[1][2]).SetAttValue ('SigState','RED')
            Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(Aseq[1][3]).SetAttValue ('SigState','RED')
            if Seconds >= Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(Aseq[1][0]).AttValue ('GreenEnd')-1:
                if Seconds < Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(Aseq[1][0]).AttValue ('GreenEnd')+2:
                    Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(Aseq[1][1]).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(Aseq[1][0]).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(Aseq[1][2]).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(Aseq[1][3]).SetAttValue ('SigState','RED')


                    GI11=[[(CLength-12-Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(Aseq[1][0]).AttValue ('GreenTimeDuration'))/3,(CLength-12-Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(Aseq[1][0]).AttValue ('GreenTimeDuration'))/3,(CLength-12-Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(Aseq[1][0]).AttValue ('GreenTimeDuration'))/3], [(CLength-12-Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(Aseq[1][0]).AttValue ('GreenTimeDuration'))/4,(CLength-12-Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(Aseq[1][0]).AttValue ('GreenTimeDuration'))/4,(CLength-12-Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(Aseq[1][0]).AttValue ('GreenTimeDuration'))/2],[(CLength-12-Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(Aseq[1][0]).AttValue ('GreenTimeDuration'))/4,(CLength-12-Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(Aseq[1][0]).AttValue ('GreenTimeDuration'))/2,(CLength-12-Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(Aseq[1][0]).AttValue ('GreenTimeDuration'))/4],[(CLength-12-Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(Aseq[1][0]).AttValue ('GreenTimeDuration'))/5,3*(CLength-12-Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(Aseq[1][0]).AttValue ('GreenTimeDuration'))/5,(CLength-12-Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(Aseq[1][0]).AttValue ('GreenTimeDuration'))/5],[(CLength-12-Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(Aseq[1][0]).AttValue ('GreenTimeDuration'))/6,4*(CLength-12-Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(Aseq[1][0]).AttValue ('GreenTimeDuration'))/6,(CLength-12-Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(Aseq[1][0]).AttValue ('GreenTimeDuration'))/6],[(CLength-12-Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(Aseq[1][0]).AttValue ('GreenTimeDuration'))/7,5*(CLength-12-Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(Aseq[1][0]).AttValue ('GreenTimeDuration'))/7,(CLength-12-Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(Aseq[1][0]).AttValue ('GreenTimeDuration'))/7]]
                    indexI11=permutation([Aseq[1][1],Aseq[1][2],Aseq[1][3]])
                    grreenstrat11=[]
                    grreenenddd11=[]
                    for i in range(len(GI11)):
                        kokop=[]
                        kokop2=[]
                        for j in range(len(GI11[i])):
                            kokop.append([5+Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(Aseq[1][0]).AttValue ('GreenTimeDuration'), 8+Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(Aseq[1][0]).AttValue ('GreenTimeDuration')+GI11[i][j], 11+Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(Aseq[1][0]).AttValue ('GreenTimeDuration')+GI11[i][j ] +GI11[i][j-1]])
                            kokop2.append([5+Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(Aseq[1][0]).AttValue ('GreenTimeDuration')+GI11[i][j], 8+Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(Aseq[1][0]).AttValue ('GreenTimeDuration')+GI11[i][j-1] +GI11[i][j], 11+Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(Aseq[1][0]).AttValue ('GreenTimeDuration')+GI11[i][j ] +GI11[i][j-1]+GI11[i][j]])
                              
                        grreenstrat11.append(kokop)

                        grreenenddd11.append(kokop2)






                    ddst=[]
                    varices=[]
                    for i in grreenstrat11:
                        ddst1=[]
                        varices2=[]

                        for j in i:
                            ddst1.append(Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(Aseq[1][1]).AttValue ('distributionincapacity')+Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(Aseq[1][1]).AttValue ('ArrivalRate')*((j[0]-SimSec)/3600)-0.2*GI11[grreenstrat11.index(i)][0])
                            ddst1.append(Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(Aseq[1][2]).AttValue ('distributionincapacity')+Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(Aseq[1][2]).AttValue ('ArrivalRate')*((j[1]-SimSec)/3600)-0.2*GI11[grreenstrat11.index(i)][1])
                            ddst1.append(Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(Aseq[1][3]).AttValue ('distributionincapacity')+Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(Aseq[1][3]).AttValue ('ArrivalRate')*((j[2]-SimSec)/3600)-0.2*GI11[grreenstrat11.index(i)][2])
                            varices2.append(variance(ddst1))
                        ddst.append(ddst1)
                        varices.append(varices2)
                        



                    varices = flatten_list (varices)                    




                    ipip= int(math.floor(varices.index(min(varices))/3))
                    jpjp= int(varices.index(min(varices))- ipip*3)


                    Aseq[1][1]= indexI11[jpjp][0]
                    Aseq[1][2]= indexI11[jpjp][1]
                    Aseq[1][3]= indexI11[jpjp][2]

                    f2= open("Aseq.txt","w")
                    f2.write(str(Aseq))
                    f2.write("\n")
                    f2.close()






   
                    Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(Aseq[1][1]).SetAttValue('GreenTimeDuration',GI11[ipip][0])
                    Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(Aseq[1][2]).SetAttValue('GreenTimeDuration',GI11[ipip][1])
                    Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(Aseq[1][3]).SetAttValue('GreenTimeDuration',GI11[ipip][2])


     
                    Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(Aseq[1][1]).SetAttValue('GreenStart',grreenstrat11[ipip][jpjp][0])
                    Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(Aseq[1][2]).SetAttValue('GreenStart',grreenstrat11[ipip][jpjp][1])
                    Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(Aseq[1][3]).SetAttValue('GreenStart',grreenstrat11[ipip][jpjp][2])


    
                    Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(Aseq[1][1]).SetAttValue('GreenEnd',grreenenddd11[ipip][jpjp][0])
                    Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(Aseq[1][2]).SetAttValue('GreenEnd',grreenenddd11[ipip][jpjp][1])
                    Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(Aseq[1][3]).SetAttValue('GreenEnd',grreenenddd11[ipip][jpjp][2])








        if Seconds >= Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(Aseq[1][1]).AttValue ('GreenStart')-1:
            if Seconds <= Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(Aseq[1][1]).AttValue ('GreenEnd')-1:
                    Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(Aseq[1][1]).SetAttValue ('SigState','GREEN')
                    Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(Aseq[1][0]).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(Aseq[1][2]).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(Aseq[1][3]).SetAttValue ('SigState','RED')


        if  Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(Aseq[1][1]).AttValue ('SigState') == 'GREEN':
            Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(Aseq[1][0]).SetAttValue ('SigState','RED')
            Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(Aseq[1][2]).SetAttValue ('SigState','RED')
            Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(Aseq[1][3]).SetAttValue ('SigState','RED')             
            if Seconds >= Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(Aseq[1][1]).AttValue ('GreenEnd')-1:
                if Seconds < Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(Aseq[1][1]).AttValue ('GreenEnd')+2:                 
                    Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(Aseq[1][2]).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(Aseq[1][0]).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(Aseq[1][1]).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(Aseq[1][3]).SetAttValue ('SigState','RED')


                    GI11=[[(CLength-12-Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(Aseq[1][0]).AttValue ('GreenTimeDuration')-Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(Aseq[1][1]).AttValue ('GreenTimeDuration'))/2,(CLength-12-Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(Aseq[1][0]).AttValue ('GreenTimeDuration')-Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(Aseq[1][1]).AttValue ('GreenTimeDuration'))/2],[2*(CLength-12-Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(Aseq[1][0]).AttValue ('GreenTimeDuration')-Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(Aseq[1][1]).AttValue ('GreenTimeDuration'))/3,(CLength-12-Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(Aseq[1][0]).AttValue ('GreenTimeDuration')-Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(Aseq[1][1]).AttValue ('GreenTimeDuration'))/3]]
                    indexI11=permutation([Aseq[1][2],Aseq[1][3]])
                    grreenstrat11=[]
                    grreenenddd11=[]
                    for i in range(len(GI11)):
                        kokop=[]
                        kokop2=[]
                        for j in range(len(GI11[i])):

                            kokop.append([8+Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(Aseq[1][0]).AttValue ('GreenTimeDuration') + Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(Aseq[1][0]).AttValue ('GreenTimeDuration'), 11+Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(Aseq[1][0]).AttValue ('GreenTimeDuration')+Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(Aseq[1][1]).AttValue ('GreenTimeDuration')+ GI11[i][j] ])
                            kokop2.append([8+Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(Aseq[1][0]).AttValue ('GreenTimeDuration') + Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(Aseq[1][0]).AttValue ('GreenTimeDuration') + GI11[i][j], 11+Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(Aseq[1][0]).AttValue ('GreenTimeDuration')+Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(Aseq[1][1]).AttValue ('GreenTimeDuration')+ GI11[i][j-1] + GI11[i][j]])

                              
                        grreenstrat11.append(kokop)

                        grreenenddd11.append(kokop2)





                    ddst=[]
                    varices=[]
                    for i in grreenstrat11:
                        ddst1=[]
                        varices2=[]

                        for j in i:
                            ddst1.append(Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(Aseq[1][2]).AttValue ('distributionincapacity')+Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(Aseq[1][2]).AttValue ('ArrivalRate')*((j[0]-SimSec)/3600)-0.2*GI11[grreenstrat11.index(i)][0])
                            ddst1.append(Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(Aseq[1][3]).AttValue ('distributionincapacity')+Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(Aseq[1][3]).AttValue ('ArrivalRate')*((j[1]-SimSec)/3600)-0.2*GI11[grreenstrat11.index(i)][1])
                            varices2.append(variance(ddst1))
                        ddst.append(ddst1)
                        varices.append(varices2)
                        

                    varices = flatten_list (varices)                    




                    ipip= int(math.floor(varices.index(min(varices))/2))
                    jpjp= int(varices.index(min(varices))- ipip*2)







                    Aseq[1][2]= indexI11[jpjp][0]
                    Aseq[1][3]= indexI11[jpjp][1]

                    f2= open("Aseq.txt","w")
                    f2.write(str(Aseq))
                    f2.write("\n")
                    f2.close()







   

                    Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(Aseq[1][2]).SetAttValue('GreenTimeDuration',GI11[ipip][0])
                    Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(Aseq[1][3]).SetAttValue('GreenTimeDuration',GI11[ipip][1])



                    Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(Aseq[1][2]).SetAttValue('GreenStart',grreenstrat11[ipip][jpjp][0])
                    Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(Aseq[1][3]).SetAttValue('GreenStart',grreenstrat11[ipip][jpjp][1])


    

                    Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(Aseq[1][2]).SetAttValue('GreenEnd',grreenenddd11[ipip][jpjp][0])
                    Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(Aseq[1][3]).SetAttValue('GreenEnd',grreenenddd11[ipip][jpjp][1])






        if Seconds >= Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(Aseq[1][2]).AttValue ('GreenStart')-1:
            if Seconds <= Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(Aseq[1][2]).AttValue ('GreenEnd')-1:
                    Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(Aseq[1][2]).SetAttValue ('SigState','GREEN')
                    Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(Aseq[1][0]).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(Aseq[1][1]).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(Aseq[1][3]).SetAttValue ('SigState','RED')


        if  Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(Aseq[1][2]).AttValue ('SigState') == 'GREEN':
            Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(Aseq[1][0]).SetAttValue ('SigState','RED')
            Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(Aseq[1][1]).SetAttValue ('SigState','RED')
            Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(Aseq[1][3]).SetAttValue ('SigState','RED') 
            if Seconds >= Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(Aseq[1][2]).AttValue ('GreenEnd')-1:
                if Seconds < Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(Aseq[1][2]).AttValue ('GreenEnd')+2:             
                    Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(Aseq[1][3]).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(Aseq[1][0]).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(Aseq[1][1]).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(Aseq[1][2]).SetAttValue ('SigState','RED')


        if Seconds >= Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(Aseq[1][3]).AttValue ('GreenStart')-1:
            if Seconds <= Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(Aseq[1][3]).AttValue ('GreenEnd')-1:
                    Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(Aseq[1][3]).SetAttValue ('SigState','GREEN')
                    Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(Aseq[1][0]).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(Aseq[1][1]).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(Aseq[1][2]).SetAttValue ('SigState','RED')


        if  Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(Aseq[1][3]).AttValue ('SigState') == 'GREEN':
            Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(Aseq[1][0]).SetAttValue ('SigState','RED')
            Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(Aseq[1][1]).SetAttValue ('SigState','RED')
            Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(Aseq[1][2]).SetAttValue ('SigState','RED')
            if Seconds >= Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(Aseq[1][3]).AttValue ('GreenEnd')-1:             
                    Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(Aseq[1][0]).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(Aseq[1][1]).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(Aseq[1][2]).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(Aseq[1][3]).SetAttValue ('SigState','RED')







                    GI11=[[(CLength-12)/4,(CLength-12)/4,(CLength-12)/4,(CLength-12)/4],[(CLength-12)/3,(CLength-12)/3,(CLength-12)/6,(CLength-12)/6],[(CLength-12)/3,(CLength-12)/3,(CLength-12)/6,(CLength-12)/6], [(CLength-12)/2,(CLength-12)/6,(CLength-12)/6,(CLength-12)/6],[(CLength-12)/4,(CLength-12)/4,(CLength-12)/4,(CLength-12)/4],[(CLength-12)/3,(CLength-12)/3,(CLength-12)/6,(CLength-12)/6],[(CLength-12)/3,(CLength-12)/3,(CLength-12)/6,(CLength-12)/6], [(CLength-12)/2,(CLength-12)/6,(CLength-12)/6,(CLength-12)/6],[(CLength-12)/4,(CLength-12)/4,(CLength-12)/4,(CLength-12)/4],[(CLength-12)/3,(CLength-12)/3,(CLength-12)/6,(CLength-12)/6],[(CLength-12)/3,(CLength-12)/3,(CLength-12)/6,(CLength-12)/6], [(CLength-12)/2,(CLength-12)/6,(CLength-12)/6,(CLength-12)/6],[(CLength-12)/4,(CLength-12)/4,(CLength-12)/4,(CLength-12)/4],[(CLength-12)/3,(CLength-12)/3,(CLength-12)/6,(CLength-12)/6],[(CLength-12)/3,(CLength-12)/3,(CLength-12)/6,(CLength-12)/6], [(CLength-12)/2,(CLength-12)/6,(CLength-12)/6,(CLength-12)/6],[(CLength-12)/4,(CLength-12)/4,(CLength-12)/4,(CLength-12)/4],[(CLength-12)/3,(CLength-12)/3,(CLength-12)/6,(CLength-12)/6],[(CLength-12)/3,(CLength-12)/3,(CLength-12)/6,(CLength-12)/6], [(CLength-12)/2,(CLength-12)/6,(CLength-12)/6,(CLength-12)/6],[(CLength-12)/4,(CLength-12)/4,(CLength-12)/4,(CLength-12)/4],[(CLength-12)/3,(CLength-12)/3,(CLength-12)/6,(CLength-12)/6],[(CLength-12)/3,(CLength-12)/3,(CLength-12)/6,(CLength-12)/6], [(CLength-12)/2,(CLength-12)/6,(CLength-12)/6,(CLength-12)/6]]
                    indexI11=permutation([Aseq[1][0],Aseq[1][1],Aseq[1][2],Aseq[1][3]])
                    grreenstrat11=[]
                    grreenenddd11=[]
                    for i in range(len(GI11)):
                        kokop=[]
                        kokop2=[]
                        for j in range(len(GI11[i])):
                            kokop.append([2, 5+GI11[i][j-3], 8+GI11[i][j-3]+GI11[i][j-2], 11+GI11[i][j-3]+GI11[i][j-2] +GI11[i][j-1]])
                            kokop2.append([2+GI11[i][j-3], 5+GI11[i][j-3]+GI11[i][j-2], 8+GI11[i][j-3]+GI11[i][j-2]+GI11[i][j-1], 11 +GI11[i][j-3]+GI11[i][j-2]+GI11[i][j-1] +GI11[i][j]])
 
                        grreenstrat11.append(kokop)
                        grreenenddd11.append(kokop2)




                    ddst=[]
                    varices=[]
                    for i in grreenstrat11:
                        ddst1=[]
                        varices2=[]

                        for j in i:
                            ddst1.append(Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(Aseq[1][0]).AttValue ('distributionincapacity')+Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(Aseq[1][0]).AttValue ('ArrivalRate')*((j[0]-SimSec)/3600)-0.5*GI11[grreenstrat11.index(i)][0])
                            ddst1.append(Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(Aseq[1][1]).AttValue ('distributionincapacity')+Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(Aseq[1][1]).AttValue ('ArrivalRate')*((j[1]-SimSec)/3600)-0.5*GI11[grreenstrat11.index(i)][1])
                            ddst1.append(Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(Aseq[1][2]).AttValue ('distributionincapacity')+Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(Aseq[1][2]).AttValue ('ArrivalRate')*((j[2]-SimSec)/3600)-0.5*GI11[grreenstrat11.index(i)][2])
                            ddst1.append(Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(Aseq[1][3]).AttValue ('distributionincapacity')+Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(Aseq[1][3]).AttValue ('ArrivalRate')*((j[3]-SimSec)/3600)-0.5*GI11[grreenstrat11.index(i)][3])
                            varices2.append(variance(ddst1))
                        ddst.append(ddst1)
                        varices.append(varices2)

                    varices = flatten_list (varices)                    




                    ipip= int(math.floor(varices.index(min(varices))/4))
                    jpjp= int(varices.index(min(varices))- ipip*4)






                    Aseq[1][0]= indexI11[jpjp][0]
                    Aseq[1][1]= indexI11[jpjp][1]
                    Aseq[1][2]= indexI11[jpjp][2]
                    Aseq[1][3]= indexI11[jpjp][3]

                    f2= open("Aseq.txt","w")
                    f2.write(str(Aseq))
                    f2.write("\n")
                    f2.close()



                    Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(Aseq[1][0]).SetAttValue('GreenTimeDuration',GI11[ipip][0])   
                    Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(Aseq[1][1]).SetAttValue('GreenTimeDuration',GI11[ipip][1])
                    Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(Aseq[1][2]).SetAttValue('GreenTimeDuration',GI11[ipip][2])
                    Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(Aseq[1][3]).SetAttValue('GreenTimeDuration',GI11[ipip][3])



                    Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(Aseq[1][0]).SetAttValue('GreenStart',grreenstrat11[ipip][jpjp][0])     
                    Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(Aseq[1][1]).SetAttValue('GreenStart',grreenstrat11[ipip][jpjp][1])
                    Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(Aseq[1][2]).SetAttValue('GreenStart',grreenstrat11[ipip][jpjp][2])
                    Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(Aseq[1][3]).SetAttValue('GreenStart',grreenstrat11[ipip][jpjp][3])


                    Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(Aseq[1][0]).SetAttValue('GreenEnd',grreenenddd11[ipip][jpjp][0])    
                    Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(Aseq[1][1]).SetAttValue('GreenEnd',grreenenddd11[ipip][jpjp][1])
                    Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(Aseq[1][2]).SetAttValue('GreenEnd',grreenenddd11[ipip][jpjp][2])
                    Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(Aseq[1][3]).SetAttValue('GreenEnd',grreenenddd11[ipip][jpjp][3])









                        














































        if  Vissim.Net.SignalControllers.ItemByKey(5).SGs.ItemByKey(1).AttValue ('SigState') == 'GREEN':
            Vissim.Net.SignalControllers.ItemByKey(5).SGs.ItemByKey(2).SetAttValue ('SigState','RED')
            Vissim.Net.SignalControllers.ItemByKey(5).SGs.ItemByKey(3).SetAttValue ('SigState','RED')
            Vissim.Net.SignalControllers.ItemByKey(5).SGs.ItemByKey(4).SetAttValue ('SigState','RED')
            if Seconds >= Vissim.Net.SignalControllers.ItemByKey(5).SGs.ItemByKey(1).AttValue ('GreenEnd')-1:
                if Seconds <= Vissim.Net.SignalControllers.ItemByKey(5).SGs.ItemByKey(1).AttValue ('GreenEnd')+2:
                    Vissim.Net.SignalControllers.ItemByKey(5).SGs.ItemByKey(1).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(5).SGs.ItemByKey(2).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(5).SGs.ItemByKey(3).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(5).SGs.ItemByKey(4).SetAttValue ('SigState','RED')





        if Seconds >= Vissim.Net.SignalControllers.ItemByKey(5).SGs.ItemByKey(2).AttValue ('GreenStart')-1:
            if Seconds <= Vissim.Net.SignalControllers.ItemByKey(5).SGs.ItemByKey(2).AttValue ('GreenEnd')-1:
                    Vissim.Net.SignalControllers.ItemByKey(5).SGs.ItemByKey(1).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(5).SGs.ItemByKey(2).SetAttValue ('SigState','GREEN')
                    Vissim.Net.SignalControllers.ItemByKey(5).SGs.ItemByKey(3).SetAttValue ('SigState','GREEN')
                    Vissim.Net.SignalControllers.ItemByKey(5).SGs.ItemByKey(4).SetAttValue ('SigState','GREEN')



        if  Vissim.Net.SignalControllers.ItemByKey(5).SGs.ItemByKey(2).AttValue ('SigState') == 'GREEN':
            Vissim.Net.SignalControllers.ItemByKey(5).SGs.ItemByKey(1).SetAttValue ('SigState','RED')
            if Seconds >= Vissim.Net.SignalControllers.ItemByKey(5).SGs.ItemByKey(2).AttValue ('GreenEnd')-1:
                    Vissim.Net.SignalControllers.ItemByKey(5).SGs.ItemByKey(1).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(5).SGs.ItemByKey(2).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(5).SGs.ItemByKey(3).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(5).SGs.ItemByKey(4).SetAttValue ('SigState','RED')






        if  Vissim.Net.SignalControllers.ItemByKey(12).SGs.ItemByKey(1).AttValue ('SigState') == 'GREEN':
            Vissim.Net.SignalControllers.ItemByKey(12).SGs.ItemByKey(2).SetAttValue ('SigState','RED')
            Vissim.Net.SignalControllers.ItemByKey(12).SGs.ItemByKey(3).SetAttValue ('SigState','RED')
            Vissim.Net.SignalControllers.ItemByKey(12).SGs.ItemByKey(4).SetAttValue ('SigState','RED')
            if Seconds >= Vissim.Net.SignalControllers.ItemByKey(12).SGs.ItemByKey(1).AttValue ('GreenEnd')-1:
                if Seconds <= Vissim.Net.SignalControllers.ItemByKey(12).SGs.ItemByKey(1).AttValue ('GreenEnd')+2:
                    Vissim.Net.SignalControllers.ItemByKey(12).SGs.ItemByKey(1).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(12).SGs.ItemByKey(2).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(12).SGs.ItemByKey(3).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(12).SGs.ItemByKey(4).SetAttValue ('SigState','RED')



        if Seconds >= Vissim.Net.SignalControllers.ItemByKey(12).SGs.ItemByKey(2).AttValue ('GreenStart')-1:
            if Seconds <= Vissim.Net.SignalControllers.ItemByKey(12).SGs.ItemByKey(2).AttValue ('GreenEnd')-1:
                    Vissim.Net.SignalControllers.ItemByKey(12).SGs.ItemByKey(1).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(12).SGs.ItemByKey(2).SetAttValue ('SigState','GREEN')
                    Vissim.Net.SignalControllers.ItemByKey(12).SGs.ItemByKey(3).SetAttValue ('SigState','GREEN')
                    Vissim.Net.SignalControllers.ItemByKey(12).SGs.ItemByKey(4).SetAttValue ('SigState','GREEN')



        if  Vissim.Net.SignalControllers.ItemByKey(12).SGs.ItemByKey(2).AttValue ('SigState') == 'GREEN':
            Vissim.Net.SignalControllers.ItemByKey(12).SGs.ItemByKey(1).SetAttValue ('SigState','RED')
            if Seconds >= Vissim.Net.SignalControllers.ItemByKey(12).SGs.ItemByKey(2).AttValue ('GreenEnd')-1:
                    Vissim.Net.SignalControllers.ItemByKey(12).SGs.ItemByKey(1).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(12).SGs.ItemByKey(2).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(12).SGs.ItemByKey(3).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(12).SGs.ItemByKey(4).SetAttValue ('SigState','RED')





        if  Vissim.Net.SignalControllers.ItemByKey(13).SGs.ItemByKey(1).AttValue ('SigState') == 'GREEN':
            Vissim.Net.SignalControllers.ItemByKey(13).SGs.ItemByKey(2).SetAttValue ('SigState','RED')
            Vissim.Net.SignalControllers.ItemByKey(13).SGs.ItemByKey(3).SetAttValue ('SigState','RED')
            Vissim.Net.SignalControllers.ItemByKey(13).SGs.ItemByKey(4).SetAttValue ('SigState','RED')
            if Seconds >= Vissim.Net.SignalControllers.ItemByKey(13).SGs.ItemByKey(1).AttValue ('GreenEnd')-1:
                if Seconds <= Vissim.Net.SignalControllers.ItemByKey(13).SGs.ItemByKey(1).AttValue ('GreenEnd')+2:
                    Vissim.Net.SignalControllers.ItemByKey(13).SGs.ItemByKey(1).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(13).SGs.ItemByKey(2).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(13).SGs.ItemByKey(3).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(13).SGs.ItemByKey(4).SetAttValue ('SigState','RED')




        if Seconds >= Vissim.Net.SignalControllers.ItemByKey(13).SGs.ItemByKey(2).AttValue ('GreenStart')-1:
            if Seconds <= Vissim.Net.SignalControllers.ItemByKey(13).SGs.ItemByKey(2).AttValue ('GreenEnd')-1:
                    Vissim.Net.SignalControllers.ItemByKey(13).SGs.ItemByKey(1).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(13).SGs.ItemByKey(2).SetAttValue ('SigState','GREEN')
                    Vissim.Net.SignalControllers.ItemByKey(13).SGs.ItemByKey(3).SetAttValue ('SigState','GREEN')
                    Vissim.Net.SignalControllers.ItemByKey(13).SGs.ItemByKey(4).SetAttValue ('SigState','GREEN')



        if  Vissim.Net.SignalControllers.ItemByKey(13).SGs.ItemByKey(2).AttValue ('SigState') == 'GREEN':
            Vissim.Net.SignalControllers.ItemByKey(13).SGs.ItemByKey(1).SetAttValue ('SigState','RED')
            if Seconds >= Vissim.Net.SignalControllers.ItemByKey(13).SGs.ItemByKey(2).AttValue ('GreenEnd')-1:
                    Vissim.Net.SignalControllers.ItemByKey(13).SGs.ItemByKey(1).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(13).SGs.ItemByKey(2).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(13).SGs.ItemByKey(3).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(13).SGs.ItemByKey(4).SetAttValue ('SigState','RED')







    if Seconds >=79:

        f2 = open("Aseq.txt","r")  
        ggg = f2.readline()
        f2.close()
        Aseq= ast.literal_eval(ggg)


        Vissim.Net.SignalControllers.ItemByKey(13).SGs.ItemByKey(1).SetAttValue ('ContrByCOM',True)
        Vissim.Net.SignalControllers.ItemByKey(13).SGs.ItemByKey(2).SetAttValue ('ContrByCOM',True)
        Vissim.Net.SignalControllers.ItemByKey(13).SGs.ItemByKey(3).SetAttValue ('ContrByCOM',True)
        Vissim.Net.SignalControllers.ItemByKey(13).SGs.ItemByKey(4).SetAttValue ('ContrByCOM',True)
        Vissim.Net.SignalControllers.ItemByKey(13).SGs.ItemByKey(Aseq[12][0]).SetAttValue ('SigState','GREEN')


        Vissim.Net.SignalControllers.ItemByKey(12).SGs.ItemByKey(1).SetAttValue ('ContrByCOM',True)
        Vissim.Net.SignalControllers.ItemByKey(12).SGs.ItemByKey(2).SetAttValue ('ContrByCOM',True)
        Vissim.Net.SignalControllers.ItemByKey(12).SGs.ItemByKey(3).SetAttValue ('ContrByCOM',True)
        Vissim.Net.SignalControllers.ItemByKey(12).SGs.ItemByKey(4).SetAttValue ('ContrByCOM',True)
        Vissim.Net.SignalControllers.ItemByKey(12).SGs.ItemByKey(Aseq[11][0]).SetAttValue ('SigState','GREEN')



        Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(1).SetAttValue ('ContrByCOM',True)
        Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(2).SetAttValue ('ContrByCOM',True)
        Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(3).SetAttValue ('ContrByCOM',True)
        Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(4).SetAttValue ('ContrByCOM',True)
        Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(Aseq[10][0]).SetAttValue ('SigState','GREEN')


        Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(1).SetAttValue ('ContrByCOM',True)
        Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(2).SetAttValue ('ContrByCOM',True)
        Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(3).SetAttValue ('ContrByCOM',True)
        Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(4).SetAttValue ('ContrByCOM',True)
        Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(Aseq[9][0]).SetAttValue ('SigState','GREEN')


        Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(1).SetAttValue ('ContrByCOM',True)
        Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(2).SetAttValue ('ContrByCOM',True)
        Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(3).SetAttValue ('ContrByCOM',True)
        Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(4).SetAttValue ('ContrByCOM',True)
        Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(Aseq[8][0]).SetAttValue ('SigState','GREEN')

        Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(1).SetAttValue ('ContrByCOM',True)
        Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(2).SetAttValue ('ContrByCOM',True)
        Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(3).SetAttValue ('ContrByCOM',True)
        Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(4).SetAttValue ('ContrByCOM',True)
        Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(Aseq[7][0]).SetAttValue ('SigState','GREEN')

        Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(1).SetAttValue ('ContrByCOM',True)
        Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(2).SetAttValue ('ContrByCOM',True)
        Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(3).SetAttValue ('ContrByCOM',True)
        Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(4).SetAttValue ('ContrByCOM',True)
        Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(Aseq[6][0]).SetAttValue ('SigState','GREEN')

        Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(1).SetAttValue ('ContrByCOM',True)
        Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(2).SetAttValue ('ContrByCOM',True)
        Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(3).SetAttValue ('ContrByCOM',True)
        Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(4).SetAttValue ('ContrByCOM',True)
        Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(Aseq[5][0]).SetAttValue ('SigState','GREEN')


        Vissim.Net.SignalControllers.ItemByKey(5).SGs.ItemByKey(1).SetAttValue ('ContrByCOM',True)
        Vissim.Net.SignalControllers.ItemByKey(5).SGs.ItemByKey(2).SetAttValue ('ContrByCOM',True)
        Vissim.Net.SignalControllers.ItemByKey(5).SGs.ItemByKey(3).SetAttValue ('ContrByCOM',True)
        Vissim.Net.SignalControllers.ItemByKey(5).SGs.ItemByKey(4).SetAttValue ('ContrByCOM',True)
        Vissim.Net.SignalControllers.ItemByKey(5).SGs.ItemByKey(Aseq[4][0]).SetAttValue ('SigState','GREEN')


        Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(1).SetAttValue ('ContrByCOM',True)
        Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(2).SetAttValue ('ContrByCOM',True)
        Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(3).SetAttValue ('ContrByCOM',True)
        Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(4).SetAttValue ('ContrByCOM',True)
        Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(Aseq[3][0]).SetAttValue ('SigState','GREEN')

        Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(1).SetAttValue ('ContrByCOM',True)
        Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(2).SetAttValue ('ContrByCOM',True)
        Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(3).SetAttValue ('ContrByCOM',True)
        Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(4).SetAttValue ('ContrByCOM',True)
        Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(Aseq[2][0]).SetAttValue ('SigState','GREEN')


        Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(1).SetAttValue ('ContrByCOM',True)
        Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(2).SetAttValue ('ContrByCOM',True)
        Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(3).SetAttValue ('ContrByCOM',True)
        Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(4).SetAttValue ('ContrByCOM',True)
        Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(Aseq[1][0]).SetAttValue ('SigState','GREEN')


        Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).SetAttValue ('ContrByCOM',True)
        Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(2).SetAttValue ('ContrByCOM',True)
        Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(3).SetAttValue ('ContrByCOM',True)
        Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(4).SetAttValue ('ContrByCOM',True)
        Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(Aseq[0][0]).SetAttValue ('SigState','GREEN')






    if SimSec > Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).AttValue('ittearrivalnumber')*ittearrival+3:
        if SimSec<= Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).AttValue('ittearrivalnumber')*ittearrival+4:


            Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).SetAttValue ('distributionincapacity', Vissim.Net.Links.ItemByKey(109).AttValue ('Count:Vehs')+ round(Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).AttValue ('ArrivalRate')*ittearrival/3600))
            Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(2).SetAttValue ('distributionincapacity', (Vissim.Net.Links.ItemByKey(91).AttValue ('Count:Vehs')+ round(Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(2).AttValue ('ArrivalRate')*ittearrival/3600))*4)
            Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(3).SetAttValue ('distributionincapacity', (Vissim.Net.Links.ItemByKey(89).AttValue ('Count:Vehs')+ round(Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(3).AttValue ('ArrivalRate')*ittearrival/3600))*4)
            Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(4).SetAttValue ('distributionincapacity', (Vissim.Net.Links.ItemByKey(100).AttValue ('Count:Vehs')+ round(Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(4).AttValue ('ArrivalRate')*ittearrival/3600))*4)





            Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(1).SetAttValue ('distributionincapacity', (Vissim.Net.Links.ItemByKey(90).AttValue ('Count:Vehs')+ round(Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(1).AttValue ('ArrivalRate')*ittearrival/3600))*4)
            Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(2).SetAttValue ('distributionincapacity', (Vissim.Net.Links.ItemByKey(66).AttValue ('Count:Vehs')+ round(Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(2).AttValue ('ArrivalRate')*ittearrival/3600))*4)
            Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(3).SetAttValue ('distributionincapacity', (Vissim.Net.Links.ItemByKey(79).AttValue ('Count:Vehs')+ round(Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(3).AttValue ('ArrivalRate')*ittearrival/3600))*4)
            Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(4).SetAttValue ('distributionincapacity', (Vissim.Net.Links.ItemByKey(59).AttValue ('Count:Vehs')+ round(Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(4).AttValue ('ArrivalRate')*ittearrival/3600))*4)



            Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(1).SetAttValue ('distributionincapacity', (Vissim.Net.Links.ItemByKey(80).AttValue ('Count:Vehs')+ round(Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(1).AttValue ('ArrivalRate')*ittearrival/3600))*4)
            Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(2).SetAttValue ('distributionincapacity', (Vissim.Net.Links.ItemByKey(68).AttValue ('Count:Vehs')+ round(Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(2).AttValue ('ArrivalRate')*ittearrival/3600))*4)
            Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(3).SetAttValue ('distributionincapacity', (Vissim.Net.Links.ItemByKey(81).AttValue ('Count:Vehs')+ round(Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(3).AttValue ('ArrivalRate')*ittearrival/3600))*4)
            Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(4).SetAttValue ('distributionincapacity', (Vissim.Net.Links.ItemByKey(61).AttValue ('Count:Vehs')+ round(Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(4).AttValue ('ArrivalRate')*ittearrival/3600))*4)


            Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(1).SetAttValue ('distributionincapacity', (Vissim.Net.Links.ItemByKey(82).AttValue ('Count:Vehs')+ round(Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(1).AttValue ('ArrivalRate')*ittearrival/3600))*4)
            Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(2).SetAttValue ('distributionincapacity', (Vissim.Net.Links.ItemByKey(70).AttValue ('Count:Vehs')+ round(Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(2).AttValue ('ArrivalRate')*ittearrival/3600))*4)
            Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(3).SetAttValue ('distributionincapacity', (Vissim.Net.Links.ItemByKey(87).AttValue ('Count:Vehs')+ round(Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(3).AttValue ('ArrivalRate')*ittearrival/3600))*4)
            Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(4).SetAttValue ('distributionincapacity', (Vissim.Net.Links.ItemByKey(63).AttValue ('Count:Vehs')+ round(Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(4).AttValue ('ArrivalRate')*ittearrival/3600))*4)



            Vissim.Net.SignalControllers.ItemByKey(5).SGs.ItemByKey(1).SetAttValue ('distributionincapacity', Vissim.Net.Links.ItemByKey(108).AttValue ('Count:Vehs')+ round(Vissim.Net.SignalControllers.ItemByKey(5).SGs.ItemByKey(1).AttValue ('ArrivalRate')*ittearrival/3600))
            Vissim.Net.SignalControllers.ItemByKey(5).SGs.ItemByKey(2).SetAttValue ('distributionincapacity', (Vissim.Net.Links.ItemByKey(103).AttValue ('Count:Vehs')+ round(Vissim.Net.SignalControllers.ItemByKey(5).SGs.ItemByKey(2).AttValue ('ArrivalRate')*ittearrival/3600))*4)
            Vissim.Net.SignalControllers.ItemByKey(5).SGs.ItemByKey(3).SetAttValue ('distributionincapacity', (Vissim.Net.Links.ItemByKey(88).AttValue ('Count:Vehs')+ round(Vissim.Net.SignalControllers.ItemByKey(5).SGs.ItemByKey(3).AttValue ('ArrivalRate')*ittearrival/3600))*4)
            Vissim.Net.SignalControllers.ItemByKey(5).SGs.ItemByKey(4).SetAttValue ('distributionincapacity', (Vissim.Net.Links.ItemByKey(98).AttValue ('Count:Vehs')+ round(Vissim.Net.SignalControllers.ItemByKey(5).SGs.ItemByKey(4).AttValue ('ArrivalRate')*ittearrival/3600))*4)


            Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(1).SetAttValue ('distributionincapacity', (Vissim.Net.Links.ItemByKey(92).AttValue ('Count:Vehs')+ round(Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(1).AttValue ('ArrivalRate')*ittearrival/3600))*4)
            Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(2).SetAttValue ('distributionincapacity', (Vissim.Net.Links.ItemByKey(60).AttValue ('Count:Vehs')+ round(Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(2).AttValue ('ArrivalRate')*ittearrival/3600))*4)
            Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(3).SetAttValue ('distributionincapacity', (Vissim.Net.Links.ItemByKey(71).AttValue ('Count:Vehs')+ round(Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(3).AttValue ('ArrivalRate')*ittearrival/3600))*4)
            Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(4).SetAttValue ('distributionincapacity', (Vissim.Net.Links.ItemByKey(93).AttValue ('Count:Vehs')+ round(Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(4).AttValue ('ArrivalRate')*ittearrival/3600))*4)


            Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(1).SetAttValue ('distributionincapacity', (Vissim.Net.Links.ItemByKey(72).AttValue ('Count:Vehs')+ round(Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(1).AttValue ('ArrivalRate')*ittearrival/3600))*4)
            Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(2).SetAttValue ('distributionincapacity', (Vissim.Net.Links.ItemByKey(62).AttValue ('Count:Vehs')+ round(Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(2).AttValue ('ArrivalRate')*ittearrival/3600))*4)
            Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(3).SetAttValue ('distributionincapacity', (Vissim.Net.Links.ItemByKey(73).AttValue ('Count:Vehs')+ round(Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(3).AttValue ('ArrivalRate')*ittearrival/3600))*4)
            Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(4).SetAttValue ('distributionincapacity', (Vissim.Net.Links.ItemByKey(83).AttValue ('Count:Vehs')+ round(Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(4).AttValue ('ArrivalRate')*ittearrival/3600))*4)

            Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(1).SetAttValue ('distributionincapacity', (Vissim.Net.Links.ItemByKey(74).AttValue ('Count:Vehs')+ round(Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(1).AttValue ('ArrivalRate')*ittearrival/3600))*4)
            Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(2).SetAttValue ('distributionincapacity', (Vissim.Net.Links.ItemByKey(64).AttValue ('Count:Vehs')+ round(Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(2).AttValue ('ArrivalRate')*ittearrival/3600))*4)
            Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(3).SetAttValue ('distributionincapacity', (Vissim.Net.Links.ItemByKey(104).AttValue ('Count:Vehs')+ round(Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(3).AttValue ('ArrivalRate')*ittearrival/3600))*4)
            Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(4).SetAttValue ('distributionincapacity', (Vissim.Net.Links.ItemByKey(105).AttValue ('Count:Vehs')+ round(Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(4).AttValue ('ArrivalRate')*ittearrival/3600))*4)


            Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(1).SetAttValue ('distributionincapacity', (Vissim.Net.Links.ItemByKey(99).AttValue ('Count:Vehs')+ round(Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(1).AttValue ('ArrivalRate')*ittearrival/3600))*4)
            Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(2).SetAttValue ('distributionincapacity', (Vissim.Net.Links.ItemByKey(75).AttValue ('Count:Vehs')+ round(Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(2).AttValue ('ArrivalRate')*ittearrival/3600))*4)
            Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(3).SetAttValue ('distributionincapacity', (Vissim.Net.Links.ItemByKey(65).AttValue ('Count:Vehs')+ round(Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(3).AttValue ('ArrivalRate')*ittearrival/3600))*4)
            Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(4).SetAttValue ('distributionincapacity', (Vissim.Net.Links.ItemByKey(102).AttValue ('Count:Vehs')+ round(Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(4).AttValue ('ArrivalRate')*ittearrival/3600))*4)



            Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(1).SetAttValue ('distributionincapacity', (Vissim.Net.Links.ItemByKey(76).AttValue ('Count:Vehs')+ round(Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(1).AttValue ('ArrivalRate')*ittearrival/3600))*4)
            Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(2).SetAttValue ('distributionincapacity', (Vissim.Net.Links.ItemByKey(77).AttValue ('Count:Vehs')+ round(Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(2).AttValue ('ArrivalRate')*ittearrival/3600))*4)
            Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(3).SetAttValue ('distributionincapacity', (Vissim.Net.Links.ItemByKey(67).AttValue ('Count:Vehs')+ round(Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(3).AttValue ('ArrivalRate')*ittearrival/3600))*4)
            Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(4).SetAttValue ('distributionincapacity', (Vissim.Net.Links.ItemByKey(86).AttValue ('Count:Vehs')+ round(Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(4).AttValue ('ArrivalRate')*ittearrival/3600))*4)


            Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(1).SetAttValue ('distributionincapacity', (Vissim.Net.Links.ItemByKey(78).AttValue ('Count:Vehs')+ round(Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(1).AttValue ('ArrivalRate')*ittearrival/3600))*4)
            Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(2).SetAttValue ('distributionincapacity', (Vissim.Net.Links.ItemByKey(97).AttValue ('Count:Vehs')+ round(Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(2).AttValue ('ArrivalRate')*ittearrival/3600))*4)
            Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(3).SetAttValue ('distributionincapacity', (Vissim.Net.Links.ItemByKey(69).AttValue ('Count:Vehs')+ round(Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(3).AttValue ('ArrivalRate')*ittearrival/3600))*4)
            Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(4).SetAttValue ('distributionincapacity', (Vissim.Net.Links.ItemByKey(96).AttValue ('Count:Vehs')+ round(Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(4).AttValue ('ArrivalRate')*ittearrival/3600))*4)




            Vissim.Net.SignalControllers.ItemByKey(12).SGs.ItemByKey(1).SetAttValue ('distributionincapacity', Vissim.Net.Links.ItemByKey(112).AttValue ('Count:Vehs')+ round(Vissim.Net.SignalControllers.ItemByKey(12).SGs.ItemByKey(1).AttValue ('ArrivalRate')*ittearrival/3600))
            Vissim.Net.SignalControllers.ItemByKey(12).SGs.ItemByKey(2).SetAttValue ('distributionincapacity', (Vissim.Net.Links.ItemByKey(95).AttValue ('Count:Vehs')+ round(Vissim.Net.SignalControllers.ItemByKey(12).SGs.ItemByKey(2).AttValue ('ArrivalRate')*ittearrival/3600))*4)
            Vissim.Net.SignalControllers.ItemByKey(12).SGs.ItemByKey(3).SetAttValue ('distributionincapacity', (Vissim.Net.Links.ItemByKey(85).AttValue ('Count:Vehs')+ round(Vissim.Net.SignalControllers.ItemByKey(12).SGs.ItemByKey(3).AttValue ('ArrivalRate')*ittearrival/3600))*4)
            Vissim.Net.SignalControllers.ItemByKey(12).SGs.ItemByKey(4).SetAttValue ('distributionincapacity', (Vissim.Net.Links.ItemByKey(101).AttValue ('Count:Vehs')+ round(Vissim.Net.SignalControllers.ItemByKey(12).SGs.ItemByKey(4).AttValue ('ArrivalRate')*ittearrival/3600))*4)


            Vissim.Net.SignalControllers.ItemByKey(13).SGs.ItemByKey(1).SetAttValue ('distributionincapacity', Vissim.Net.Links.ItemByKey(113).AttValue ('Count:Vehs')+round(Vissim.Net.SignalControllers.ItemByKey(13).SGs.ItemByKey(1).AttValue ('ArrivalRate')*ittearrival/3600))
            Vissim.Net.SignalControllers.ItemByKey(13).SGs.ItemByKey(2).SetAttValue ('distributionincapacity', (Vissim.Net.Links.ItemByKey(106).AttValue ('Count:Vehs')+round(Vissim.Net.SignalControllers.ItemByKey(13).SGs.ItemByKey(2).AttValue ('ArrivalRate')*ittearrival/3600))*4)
            Vissim.Net.SignalControllers.ItemByKey(13).SGs.ItemByKey(3).SetAttValue ('distributionincapacity', (Vissim.Net.Links.ItemByKey(84).AttValue ('Count:Vehs')+round(Vissim.Net.SignalControllers.ItemByKey(13).SGs.ItemByKey(3).AttValue ('ArrivalRate')*ittearrival/3600))*4)
            Vissim.Net.SignalControllers.ItemByKey(13).SGs.ItemByKey(4).SetAttValue ('distributionincapacity', (Vissim.Net.Links.ItemByKey(94).AttValue ('Count:Vehs')+round(Vissim.Net.SignalControllers.ItemByKey(13).SGs.ItemByKey(4).AttValue ('ArrivalRate')*ittearrival/3600))*4)































def lambdaRate():
    GetVissimDataVehicles()
    KalmanGain = 0.5
    proportion_of_CAVs=1
    CLength=80
    Seconds = Vissim.Net.SignalControllers.ItemByKey(1).AttValue ('CycSec')
    InitialArrival=10
    InitialArrival2=140
    ittearrival=10

    
    Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).SetAttValue('Seconds',Vissim.Net.Simulation.SimulationSecond)
    CySec = Vissim.Net.SignalControllers.ItemByKey(1).AttValue ('CycSec')
    SimSec = Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).AttValue('Seconds')

    #Reseting values befor each iteration of simulation

    if Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).AttValue('Seconds')<=1:
        f2= open("Aseq.txt","w")
        f2.write(str([[1, 2, 3, 4],[1, 2, 3, 4],[1, 2, 3, 4],[1, 2, 3, 4],[1, 2, 3, 4],[1, 2, 3, 4],[1, 2, 3, 4],[1, 2, 3, 4],[1, 2, 3, 4],[1, 2, 3, 4],[1, 2, 3, 4],[1, 2, 3, 4],[1, 2, 3, 4]]))
        f2.write("\n")
        f2.close()

 
        Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).SetAttValue('ittearrivalnumber',0)
        Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).SetAttValue('DB', 0)

        Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).SetAttValue('ittearrivalnumber2',0)
        Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).SetAttValue('DB2', 0)



        Vissim.Net.SignalControllers.ItemByKey(13).SGs.ItemByKey(1).SetAttValue ('ContrByCOM',True)
        Vissim.Net.SignalControllers.ItemByKey(13).SGs.ItemByKey(2).SetAttValue ('ContrByCOM',True)
        Vissim.Net.SignalControllers.ItemByKey(13).SGs.ItemByKey(3).SetAttValue ('ContrByCOM',True)
        Vissim.Net.SignalControllers.ItemByKey(13).SGs.ItemByKey(4).SetAttValue ('ContrByCOM',True)
        Vissim.Net.SignalControllers.ItemByKey(13).SGs.ItemByKey(1).SetAttValue ('SigState','GREEN')


        Vissim.Net.SignalControllers.ItemByKey(12).SGs.ItemByKey(1).SetAttValue ('ContrByCOM',True)
        Vissim.Net.SignalControllers.ItemByKey(12).SGs.ItemByKey(2).SetAttValue ('ContrByCOM',True)
        Vissim.Net.SignalControllers.ItemByKey(12).SGs.ItemByKey(3).SetAttValue ('ContrByCOM',True)
        Vissim.Net.SignalControllers.ItemByKey(12).SGs.ItemByKey(4).SetAttValue ('ContrByCOM',True)
        Vissim.Net.SignalControllers.ItemByKey(12).SGs.ItemByKey(1).SetAttValue ('SigState','GREEN')



        Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(1).SetAttValue ('ContrByCOM',True)
        Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(2).SetAttValue ('ContrByCOM',True)
        Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(3).SetAttValue ('ContrByCOM',True)
        Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(4).SetAttValue ('ContrByCOM',True)
        Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(1).SetAttValue ('SigState','GREEN')


        Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(1).SetAttValue ('ContrByCOM',True)
        Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(2).SetAttValue ('ContrByCOM',True)
        Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(3).SetAttValue ('ContrByCOM',True)
        Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(4).SetAttValue ('ContrByCOM',True)
        Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(1).SetAttValue ('SigState','GREEN')


        Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(1).SetAttValue ('ContrByCOM',True)
        Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(2).SetAttValue ('ContrByCOM',True)
        Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(3).SetAttValue ('ContrByCOM',True)
        Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(4).SetAttValue ('ContrByCOM',True)
        Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(1).SetAttValue ('SigState','GREEN')

        Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(1).SetAttValue ('ContrByCOM',True)
        Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(2).SetAttValue ('ContrByCOM',True)
        Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(3).SetAttValue ('ContrByCOM',True)
        Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(4).SetAttValue ('ContrByCOM',True)
        Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(1).SetAttValue ('SigState','GREEN')

        Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(1).SetAttValue ('ContrByCOM',True)
        Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(2).SetAttValue ('ContrByCOM',True)
        Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(3).SetAttValue ('ContrByCOM',True)
        Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(4).SetAttValue ('ContrByCOM',True)
        Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(1).SetAttValue ('SigState','GREEN')

        Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(1).SetAttValue ('ContrByCOM',True)
        Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(2).SetAttValue ('ContrByCOM',True)
        Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(3).SetAttValue ('ContrByCOM',True)
        Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(4).SetAttValue ('ContrByCOM',True)
        Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(1).SetAttValue ('SigState','GREEN')


        Vissim.Net.SignalControllers.ItemByKey(5).SGs.ItemByKey(1).SetAttValue ('ContrByCOM',True)
        Vissim.Net.SignalControllers.ItemByKey(5).SGs.ItemByKey(2).SetAttValue ('ContrByCOM',True)
        Vissim.Net.SignalControllers.ItemByKey(5).SGs.ItemByKey(3).SetAttValue ('ContrByCOM',True)
        Vissim.Net.SignalControllers.ItemByKey(5).SGs.ItemByKey(4).SetAttValue ('ContrByCOM',True)
        Vissim.Net.SignalControllers.ItemByKey(5).SGs.ItemByKey(1).SetAttValue ('SigState','GREEN')


        Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(1).SetAttValue ('ContrByCOM',True)
        Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(2).SetAttValue ('ContrByCOM',True)
        Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(3).SetAttValue ('ContrByCOM',True)
        Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(4).SetAttValue ('ContrByCOM',True)
        Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(1).SetAttValue ('SigState','GREEN')

        Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(1).SetAttValue ('ContrByCOM',True)
        Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(2).SetAttValue ('ContrByCOM',True)
        Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(3).SetAttValue ('ContrByCOM',True)
        Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(4).SetAttValue ('ContrByCOM',True)
        Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(1).SetAttValue ('SigState','GREEN')


        Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(1).SetAttValue ('ContrByCOM',True)
        Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(2).SetAttValue ('ContrByCOM',True)
        Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(3).SetAttValue ('ContrByCOM',True)
        Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(4).SetAttValue ('ContrByCOM',True)
        Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(1).SetAttValue ('SigState','GREEN')


        Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).SetAttValue ('ContrByCOM',True)
        Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(2).SetAttValue ('ContrByCOM',True)
        Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(3).SetAttValue ('ContrByCOM',True)
        Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(4).SetAttValue ('ContrByCOM',True)
        Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).SetAttValue ('SigState','GREEN')


        Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).SetAttValue('GreenTimeDuration',37)      
        Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(2).SetAttValue('GreenTimeDuration',37)
        Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(3).SetAttValue('GreenTimeDuration',37)
        Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(4).SetAttValue('GreenTimeDuration',37)

        Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).SetAttValue('GreenStart',2)      
        Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(2).SetAttValue('GreenStart',42)
        Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(3).SetAttValue('GreenStart',42)
        Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(4).SetAttValue('GreenStart',42)

        Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).SetAttValue('GreenEnd',39)      
        Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(2).SetAttValue('GreenEnd',79)
        Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(3).SetAttValue('GreenEnd',79)
        Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(4).SetAttValue('GreenEnd',79)

        Vissim.Net.SignalControllers.ItemByKey(5).SGs.ItemByKey(1).SetAttValue('GreenTimeDuration',37)      
        Vissim.Net.SignalControllers.ItemByKey(5).SGs.ItemByKey(2).SetAttValue('GreenTimeDuration',37)
        Vissim.Net.SignalControllers.ItemByKey(5).SGs.ItemByKey(3).SetAttValue('GreenTimeDuration',37)
        Vissim.Net.SignalControllers.ItemByKey(5).SGs.ItemByKey(4).SetAttValue('GreenTimeDuration',37)

        Vissim.Net.SignalControllers.ItemByKey(5).SGs.ItemByKey(1).SetAttValue('GreenStart',2)      
        Vissim.Net.SignalControllers.ItemByKey(5).SGs.ItemByKey(2).SetAttValue('GreenStart',42)
        Vissim.Net.SignalControllers.ItemByKey(5).SGs.ItemByKey(3).SetAttValue('GreenStart',42)
        Vissim.Net.SignalControllers.ItemByKey(5).SGs.ItemByKey(4).SetAttValue('GreenStart',42)

        Vissim.Net.SignalControllers.ItemByKey(5).SGs.ItemByKey(1).SetAttValue('GreenEnd',39)      
        Vissim.Net.SignalControllers.ItemByKey(5).SGs.ItemByKey(2).SetAttValue('GreenEnd',79)
        Vissim.Net.SignalControllers.ItemByKey(5).SGs.ItemByKey(3).SetAttValue('GreenEnd',79)
        Vissim.Net.SignalControllers.ItemByKey(5).SGs.ItemByKey(4).SetAttValue('GreenEnd',79)

        Vissim.Net.SignalControllers.ItemByKey(12).SGs.ItemByKey(1).SetAttValue('GreenTimeDuration',37)      
        Vissim.Net.SignalControllers.ItemByKey(12).SGs.ItemByKey(2).SetAttValue('GreenTimeDuration',37)
        Vissim.Net.SignalControllers.ItemByKey(12).SGs.ItemByKey(3).SetAttValue('GreenTimeDuration',37)
        Vissim.Net.SignalControllers.ItemByKey(12).SGs.ItemByKey(4).SetAttValue('GreenTimeDuration',37)

        Vissim.Net.SignalControllers.ItemByKey(12).SGs.ItemByKey(1).SetAttValue('GreenStart',2)      
        Vissim.Net.SignalControllers.ItemByKey(12).SGs.ItemByKey(2).SetAttValue('GreenStart',42)
        Vissim.Net.SignalControllers.ItemByKey(12).SGs.ItemByKey(3).SetAttValue('GreenStart',42)
        Vissim.Net.SignalControllers.ItemByKey(12).SGs.ItemByKey(4).SetAttValue('GreenStart',42)

        Vissim.Net.SignalControllers.ItemByKey(12).SGs.ItemByKey(1).SetAttValue('GreenEnd',39)      
        Vissim.Net.SignalControllers.ItemByKey(12).SGs.ItemByKey(2).SetAttValue('GreenEnd',79)
        Vissim.Net.SignalControllers.ItemByKey(12).SGs.ItemByKey(3).SetAttValue('GreenEnd',79)
        Vissim.Net.SignalControllers.ItemByKey(12).SGs.ItemByKey(4).SetAttValue('GreenEnd',79)

        Vissim.Net.SignalControllers.ItemByKey(13).SGs.ItemByKey(1).SetAttValue('GreenTimeDuration',37)      
        Vissim.Net.SignalControllers.ItemByKey(13).SGs.ItemByKey(2).SetAttValue('GreenTimeDuration',37)
        Vissim.Net.SignalControllers.ItemByKey(13).SGs.ItemByKey(3).SetAttValue('GreenTimeDuration',37)
        Vissim.Net.SignalControllers.ItemByKey(13).SGs.ItemByKey(4).SetAttValue('GreenTimeDuration',37)

        Vissim.Net.SignalControllers.ItemByKey(13).SGs.ItemByKey(1).SetAttValue('GreenStart',2)      
        Vissim.Net.SignalControllers.ItemByKey(13).SGs.ItemByKey(2).SetAttValue('GreenStart',42)
        Vissim.Net.SignalControllers.ItemByKey(13).SGs.ItemByKey(3).SetAttValue('GreenStart',42)
        Vissim.Net.SignalControllers.ItemByKey(13).SGs.ItemByKey(4).SetAttValue('GreenStart',42)

        Vissim.Net.SignalControllers.ItemByKey(13).SGs.ItemByKey(1).SetAttValue('GreenEnd',39)      
        Vissim.Net.SignalControllers.ItemByKey(13).SGs.ItemByKey(2).SetAttValue('GreenEnd',79)
        Vissim.Net.SignalControllers.ItemByKey(13).SGs.ItemByKey(3).SetAttValue('GreenEnd',79)
        Vissim.Net.SignalControllers.ItemByKey(13).SGs.ItemByKey(4).SetAttValue('GreenEnd',79)

        Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(1).SetAttValue('GreenTimeDuration',17)      
        Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(2).SetAttValue('GreenTimeDuration',17)
        Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(3).SetAttValue('GreenTimeDuration',17)
        Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(4).SetAttValue('GreenTimeDuration',17)

        Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(1).SetAttValue('GreenStart',2)      
        Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(2).SetAttValue('GreenStart',22)
        Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(3).SetAttValue('GreenStart',42)
        Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(4).SetAttValue('GreenStart',62)

        Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(1).SetAttValue('GreenEnd',19)      
        Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(2).SetAttValue('GreenEnd',39)
        Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(3).SetAttValue('GreenEnd',59)
        Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(4).SetAttValue('GreenEnd',79)

        Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(1).SetAttValue('GreenTimeDuration',17)      
        Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(2).SetAttValue('GreenTimeDuration',17)
        Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(3).SetAttValue('GreenTimeDuration',17)
        Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(4).SetAttValue('GreenTimeDuration',17)

        Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(1).SetAttValue('GreenStart',2)      
        Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(2).SetAttValue('GreenStart',22)
        Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(3).SetAttValue('GreenStart',42)
        Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(4).SetAttValue('GreenStart',62)

        Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(1).SetAttValue('GreenEnd',19)      
        Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(2).SetAttValue('GreenEnd',39)
        Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(3).SetAttValue('GreenEnd',59)
        Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(4).SetAttValue('GreenEnd',79)


        Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(1).SetAttValue('GreenTimeDuration',17)      
        Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(2).SetAttValue('GreenTimeDuration',17)
        Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(3).SetAttValue('GreenTimeDuration',17)
        Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(4).SetAttValue('GreenTimeDuration',17)

        Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(1).SetAttValue('GreenStart',2)      
        Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(2).SetAttValue('GreenStart',22)
        Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(3).SetAttValue('GreenStart',42)
        Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(4).SetAttValue('GreenStart',62)

        Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(1).SetAttValue('GreenEnd',19)      
        Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(2).SetAttValue('GreenEnd',39)
        Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(3).SetAttValue('GreenEnd',59)
        Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(4).SetAttValue('GreenEnd',79)

        Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(1).SetAttValue('GreenTimeDuration',17)      
        Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(2).SetAttValue('GreenTimeDuration',17)
        Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(3).SetAttValue('GreenTimeDuration',17)
        Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(4).SetAttValue('GreenTimeDuration',17)

        Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(1).SetAttValue('GreenStart',2)      
        Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(2).SetAttValue('GreenStart',22)
        Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(3).SetAttValue('GreenStart',42)
        Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(4).SetAttValue('GreenStart',62)

        Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(1).SetAttValue('GreenEnd',19)      
        Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(2).SetAttValue('GreenEnd',39)
        Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(3).SetAttValue('GreenEnd',59)
        Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(4).SetAttValue('GreenEnd',79)


        Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(1).SetAttValue('GreenTimeDuration',17)      
        Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(2).SetAttValue('GreenTimeDuration',17)
        Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(3).SetAttValue('GreenTimeDuration',17)
        Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(4).SetAttValue('GreenTimeDuration',17)

        Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(1).SetAttValue('GreenStart',2)      
        Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(2).SetAttValue('GreenStart',22)
        Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(3).SetAttValue('GreenStart',42)
        Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(4).SetAttValue('GreenStart',62)

        Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(1).SetAttValue('GreenEnd',19)      
        Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(2).SetAttValue('GreenEnd',39)
        Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(3).SetAttValue('GreenEnd',59)
        Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(4).SetAttValue('GreenEnd',79)


        Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(1).SetAttValue('GreenTimeDuration',17)      
        Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(2).SetAttValue('GreenTimeDuration',17)
        Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(3).SetAttValue('GreenTimeDuration',17)
        Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(4).SetAttValue('GreenTimeDuration',17)

        Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(1).SetAttValue('GreenStart',2)      
        Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(2).SetAttValue('GreenStart',22)
        Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(3).SetAttValue('GreenStart',42)
        Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(4).SetAttValue('GreenStart',62)

        Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(1).SetAttValue('GreenEnd',19)      
        Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(2).SetAttValue('GreenEnd',39)
        Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(3).SetAttValue('GreenEnd',59)
        Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(4).SetAttValue('GreenEnd',79)



        Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(1).SetAttValue('GreenTimeDuration',17)      
        Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(2).SetAttValue('GreenTimeDuration',17)
        Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(3).SetAttValue('GreenTimeDuration',17)
        Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(4).SetAttValue('GreenTimeDuration',17)

        Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(1).SetAttValue('GreenStart',2)      
        Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(2).SetAttValue('GreenStart',22)
        Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(3).SetAttValue('GreenStart',42)
        Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(4).SetAttValue('GreenStart',62)

        Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(1).SetAttValue('GreenEnd',19)      
        Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(2).SetAttValue('GreenEnd',39)
        Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(3).SetAttValue('GreenEnd',59)
        Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(4).SetAttValue('GreenEnd',79)


        Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(1).SetAttValue('GreenTimeDuration',17)      
        Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(2).SetAttValue('GreenTimeDuration',17)
        Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(3).SetAttValue('GreenTimeDuration',17)
        Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(4).SetAttValue('GreenTimeDuration',17)

        Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(1).SetAttValue('GreenStart',2)      
        Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(2).SetAttValue('GreenStart',22)
        Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(3).SetAttValue('GreenStart',42)
        Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(4).SetAttValue('GreenStart',62)

        Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(1).SetAttValue('GreenEnd',19)      
        Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(2).SetAttValue('GreenEnd',39)
        Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(3).SetAttValue('GreenEnd',59)
        Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(4).SetAttValue('GreenEnd',79)


        Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(1).SetAttValue('GreenTimeDuration',17)      
        Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(2).SetAttValue('GreenTimeDuration',17)
        Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(3).SetAttValue('GreenTimeDuration',17)
        Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(4).SetAttValue('GreenTimeDuration',17)

        Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(1).SetAttValue('GreenStart',2)      
        Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(2).SetAttValue('GreenStart',22)
        Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(3).SetAttValue('GreenStart',42)
        Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(4).SetAttValue('GreenStart',62)

        Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(1).SetAttValue('GreenEnd',19)      
        Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(2).SetAttValue('GreenEnd',39)
        Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(3).SetAttValue('GreenEnd',59)
        Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(4).SetAttValue('GreenEnd',79)




    

        Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).SetAttValue('ArrivalRate',100)      
        Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(2).SetAttValue('ArrivalRate',0)
        Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(3).SetAttValue('ArrivalRate',0)
        Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(4).SetAttValue('ArrivalRate',0)
        Vissim.Net.SignalControllers.ItemByKey(5).SGs.ItemByKey(1).SetAttValue('ArrivalRate',100)      
        Vissim.Net.SignalControllers.ItemByKey(5).SGs.ItemByKey(2).SetAttValue('ArrivalRate',0)
        Vissim.Net.SignalControllers.ItemByKey(5).SGs.ItemByKey(3).SetAttValue('ArrivalRate',0)
        Vissim.Net.SignalControllers.ItemByKey(5).SGs.ItemByKey(4).SetAttValue('ArrivalRate',0)
        Vissim.Net.SignalControllers.ItemByKey(12).SGs.ItemByKey(1).SetAttValue('ArrivalRate',100)      
        Vissim.Net.SignalControllers.ItemByKey(12).SGs.ItemByKey(2).SetAttValue('ArrivalRate',0)
        Vissim.Net.SignalControllers.ItemByKey(12).SGs.ItemByKey(3).SetAttValue('ArrivalRate',0)
        Vissim.Net.SignalControllers.ItemByKey(12).SGs.ItemByKey(4).SetAttValue('ArrivalRate',0)
        Vissim.Net.SignalControllers.ItemByKey(13).SGs.ItemByKey(1).SetAttValue('ArrivalRate',100)      
        Vissim.Net.SignalControllers.ItemByKey(13).SGs.ItemByKey(2).SetAttValue('ArrivalRate',0)
        Vissim.Net.SignalControllers.ItemByKey(13).SGs.ItemByKey(3).SetAttValue('ArrivalRate',0)
        Vissim.Net.SignalControllers.ItemByKey(13).SGs.ItemByKey(4).SetAttValue('ArrivalRate',0)

        Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(1).SetAttValue('ArrivalRate',0)      
        Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(2).SetAttValue('ArrivalRate',0)
        Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(3).SetAttValue('ArrivalRate',0)
        Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(4).SetAttValue('ArrivalRate',0)

        Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(1).SetAttValue('ArrivalRate',0)      
        Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(2).SetAttValue('ArrivalRate',0)
        Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(3).SetAttValue('ArrivalRate',0)
        Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(4).SetAttValue('ArrivalRate',0)

        Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(1).SetAttValue('ArrivalRate',0)      
        Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(2).SetAttValue('ArrivalRate',0)
        Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(3).SetAttValue('ArrivalRate',0)
        Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(4).SetAttValue('ArrivalRate',0)

        Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(1).SetAttValue('ArrivalRate',0)      
        Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(2).SetAttValue('ArrivalRate',0)
        Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(3).SetAttValue('ArrivalRate',0)
        Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(4).SetAttValue('ArrivalRate',0)

        Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(1).SetAttValue('ArrivalRate',0)      
        Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(2).SetAttValue('ArrivalRate',0)
        Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(3).SetAttValue('ArrivalRate',0)
        Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(4).SetAttValue('ArrivalRate',0)

        Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(1).SetAttValue('ArrivalRate',0)      
        Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(2).SetAttValue('ArrivalRate',0)
        Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(3).SetAttValue('ArrivalRate',0)
        Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(4).SetAttValue('ArrivalRate',0)

        Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(1).SetAttValue('ArrivalRate',0)      
        Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(2).SetAttValue('ArrivalRate',0)
        Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(3).SetAttValue('ArrivalRate',0)
        Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(4).SetAttValue('ArrivalRate',0)

        Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(1).SetAttValue('ArrivalRate',0)      
        Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(2).SetAttValue('ArrivalRate',0)
        Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(3).SetAttValue('ArrivalRate',0)
        Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(4).SetAttValue('ArrivalRate',0)

        Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(1).SetAttValue('ArrivalRate',0)      
        Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(2).SetAttValue('ArrivalRate',0)
        Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(3).SetAttValue('ArrivalRate',0)
        Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(4).SetAttValue('ArrivalRate',0)









    if SimSec > Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).AttValue('ittearrivalnumber')*ittearrival and SimSec<= (Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).AttValue('ittearrivalnumber')+1)*ittearrival:
        if SimSec<= Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).AttValue('ittearrivalnumber')*ittearrival+1:
            f2= open("109.txt","w")
            f2.close()
            Vissim.Net.Detectors.ItemByKey(1).SetAttValue ('vh',0)

            f2= open("91.txt","w")
            f2.close()
            Vissim.Net.Detectors.ItemByKey(2).SetAttValue ('vh',0)

            f2= open("89.txt","w")
            f2.close()
            Vissim.Net.Detectors.ItemByKey(3).SetAttValue ('vh',0)


            f2= open("100.txt","w")
            f2.close()
            Vissim.Net.Detectors.ItemByKey(4).SetAttValue ('vh',0)

            f2= open("90.txt","w")
            f2.close()
            Vissim.Net.Detectors.ItemByKey(5).SetAttValue ('vh',0)

            f2= open("66.txt","w")
            f2.close()
            Vissim.Net.Detectors.ItemByKey(6).SetAttValue ('vh',0)

            f2= open("79.txt","w")
            f2.close()
            Vissim.Net.Detectors.ItemByKey(7).SetAttValue ('vh',0)


            f2= open("59.txt","w")
            f2.close()
            Vissim.Net.Detectors.ItemByKey(8).SetAttValue ('vh',0)




            f2= open("80.txt","w")
            f2.close()
            Vissim.Net.Detectors.ItemByKey(9).SetAttValue ('vh',0)



            f2= open("68.txt","w")
            f2.close()
            Vissim.Net.Detectors.ItemByKey(10).SetAttValue ('vh',0)



            f2= open("81.txt","w")
            f2.close()
            Vissim.Net.Detectors.ItemByKey(11).SetAttValue ('vh',0)



            f2= open("61.txt","w")
            f2.close()
            Vissim.Net.Detectors.ItemByKey(12).SetAttValue ('vh',0)




            f2= open("82.txt","w")
            f2.close()
            Vissim.Net.Detectors.ItemByKey(13).SetAttValue ('vh',0)



            f2= open("70.txt","w")
            f2.close()
            Vissim.Net.Detectors.ItemByKey(14).SetAttValue ('vh',0)



            f2= open("87.txt","w")
            f2.close()
            Vissim.Net.Detectors.ItemByKey(15).SetAttValue ('vh',0)



            f2= open("63.txt","w")
            f2.close()
            Vissim.Net.Detectors.ItemByKey(16).SetAttValue ('vh',0)


            f2= open("108.txt","w")
            f2.close()
            Vissim.Net.Detectors.ItemByKey(17).SetAttValue ('vh',0)

            f2= open("103.txt","w")
            f2.close()
            Vissim.Net.Detectors.ItemByKey(18).SetAttValue ('vh',0)


            f2= open("88.txt","w")
            f2.close()
            Vissim.Net.Detectors.ItemByKey(19).SetAttValue ('vh',0)


            f2= open("98.txt","w")
            f2.close()
            Vissim.Net.Detectors.ItemByKey(20).SetAttValue ('vh',0)


            f2= open("92.txt","w")
            f2.close()
            Vissim.Net.Detectors.ItemByKey(21).SetAttValue ('vh',0)

            f2= open("60.txt","w")
            f2.close()
            Vissim.Net.Detectors.ItemByKey(22).SetAttValue ('vh',0)

            f2= open("71.txt","w")
            f2.close()
            Vissim.Net.Detectors.ItemByKey(23).SetAttValue ('vh',0)

            f2= open("93.txt","w")
            f2.close()
            Vissim.Net.Detectors.ItemByKey(24).SetAttValue ('vh',0)


            f2= open("72.txt","w")
            f2.close()
            Vissim.Net.Detectors.ItemByKey(25).SetAttValue ('vh',0)

            f2= open("62.txt","w")
            f2.close()
            Vissim.Net.Detectors.ItemByKey(26).SetAttValue ('vh',0)

            f2= open("73.txt","w")
            f2.close()
            Vissim.Net.Detectors.ItemByKey(27).SetAttValue ('vh',0)

            f2= open("83.txt","w")
            f2.close()
            Vissim.Net.Detectors.ItemByKey(28).SetAttValue ('vh',0)



            f2= open("74.txt","w")
            f2.close()
            Vissim.Net.Detectors.ItemByKey(29).SetAttValue ('vh',0)

            f2= open("64.txt","w")
            f2.close()
            Vissim.Net.Detectors.ItemByKey(30).SetAttValue ('vh',0)

            f2= open("104.txt","w")
            f2.close()
            Vissim.Net.Detectors.ItemByKey(31).SetAttValue ('vh',0)

            f2= open("105.txt","w")
            f2.close()
            Vissim.Net.Detectors.ItemByKey(32).SetAttValue ('vh',0)

            f2= open("99.txt","w")
            f2.close()
            Vissim.Net.Detectors.ItemByKey(33).SetAttValue ('vh',0)

            f2= open("75.txt","w")
            f2.close()
            Vissim.Net.Detectors.ItemByKey(34).SetAttValue ('vh',0)


            f2= open("65.txt","w")
            f2.close()
            Vissim.Net.Detectors.ItemByKey(35).SetAttValue ('vh',0)

            f2= open("102.txt","w")
            f2.close()
            Vissim.Net.Detectors.ItemByKey(36).SetAttValue ('vh',0)

            f2= open("76.txt","w")
            f2.close()
            Vissim.Net.Detectors.ItemByKey(37).SetAttValue ('vh',0)


            f2= open("77.txt","w")
            f2.close()
            Vissim.Net.Detectors.ItemByKey(38).SetAttValue ('vh',0)


            f2= open("67.txt","w")
            f2.close()
            Vissim.Net.Detectors.ItemByKey(39).SetAttValue ('vh',0)

            f2= open("86.txt","w")
            f2.close()
            Vissim.Net.Detectors.ItemByKey(40).SetAttValue ('vh',0)

            f2= open("78.txt","w")
            f2.close()
            Vissim.Net.Detectors.ItemByKey(41).SetAttValue ('vh',0)

            f2= open("97.txt","w")
            f2.close()
            Vissim.Net.Detectors.ItemByKey(42).SetAttValue ('vh',0)

            f2= open("69.txt","w")
            f2.close()
            Vissim.Net.Detectors.ItemByKey(43).SetAttValue ('vh',0)

            f2= open("96.txt","w")
            f2.close()
            Vissim.Net.Detectors.ItemByKey(44).SetAttValue ('vh',0)


            f2= open("112.txt","w")
            f2.close()
            Vissim.Net.Detectors.ItemByKey(45).SetAttValue ('vh',0)

            f2= open("95.txt","w")
            f2.close()
            Vissim.Net.Detectors.ItemByKey(46).SetAttValue ('vh',0)


            f2= open("85.txt","w")
            f2.close()
            Vissim.Net.Detectors.ItemByKey(47).SetAttValue ('vh',0)

            f2= open("101.txt","w")
            f2.close()
            Vissim.Net.Detectors.ItemByKey(48).SetAttValue ('vh',0)

            f2= open("113.txt","w")
            f2.close()
            Vissim.Net.Detectors.ItemByKey(49).SetAttValue ('vh',0)


            f2= open("106.txt","w")
            f2.close()
            Vissim.Net.Detectors.ItemByKey(50).SetAttValue ('vh',0)


            f2= open("84.txt","w")
            f2.close()
            Vissim.Net.Detectors.ItemByKey(51).SetAttValue ('vh',0)


            f2= open("94.txt","w")
            f2.close()
            Vissim.Net.Detectors.ItemByKey(52).SetAttValue ('vh',0)
















            Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).SetAttValue('DB', Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).AttValue('ittearrivalnumber')+1)



            Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).SetAttValue('preARR', Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).AttValue('ArrivalRate'))
            Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(2).SetAttValue('preARR', Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(2).AttValue('ArrivalRate'))
            Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(3).SetAttValue('preARR', Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(3).AttValue('ArrivalRate'))
            Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(4).SetAttValue('preARR', Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(4).AttValue('ArrivalRate'))





            Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(1).SetAttValue('preARR', Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(1).AttValue('ArrivalRate'))
            Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(2).SetAttValue('preARR', Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(2).AttValue('ArrivalRate'))
            Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(3).SetAttValue('preARR', Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(3).AttValue('ArrivalRate'))
            Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(4).SetAttValue('preARR', Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(4).AttValue('ArrivalRate'))




            Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(1).SetAttValue('preARR', Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(1).AttValue('ArrivalRate'))
            Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(2).SetAttValue('preARR', Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(2).AttValue('ArrivalRate'))
            Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(3).SetAttValue('preARR', Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(3).AttValue('ArrivalRate'))
            Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(4).SetAttValue('preARR', Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(4).AttValue('ArrivalRate'))

            Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(1).SetAttValue('preARR', Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(1).AttValue('ArrivalRate'))
            Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(2).SetAttValue('preARR', Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(2).AttValue('ArrivalRate'))
            Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(3).SetAttValue('preARR', Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(3).AttValue('ArrivalRate'))
            Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(4).SetAttValue('preARR', Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(4).AttValue('ArrivalRate'))

            Vissim.Net.SignalControllers.ItemByKey(5).SGs.ItemByKey(1).SetAttValue('preARR', Vissim.Net.SignalControllers.ItemByKey(5).SGs.ItemByKey(1).AttValue('ArrivalRate'))
            Vissim.Net.SignalControllers.ItemByKey(5).SGs.ItemByKey(2).SetAttValue('preARR', Vissim.Net.SignalControllers.ItemByKey(5).SGs.ItemByKey(2).AttValue('ArrivalRate'))
            Vissim.Net.SignalControllers.ItemByKey(5).SGs.ItemByKey(3).SetAttValue('preARR', Vissim.Net.SignalControllers.ItemByKey(5).SGs.ItemByKey(3).AttValue('ArrivalRate'))
            Vissim.Net.SignalControllers.ItemByKey(5).SGs.ItemByKey(4).SetAttValue('preARR', Vissim.Net.SignalControllers.ItemByKey(5).SGs.ItemByKey(4).AttValue('ArrivalRate'))



            Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(1).SetAttValue('preARR', Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(1).AttValue('ArrivalRate'))
            Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(2).SetAttValue('preARR', Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(2).AttValue('ArrivalRate'))
            Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(3).SetAttValue('preARR', Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(3).AttValue('ArrivalRate'))
            Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(4).SetAttValue('preARR', Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(4).AttValue('ArrivalRate'))

            Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(1).SetAttValue('preARR', Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(1).AttValue('ArrivalRate'))
            Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(2).SetAttValue('preARR', Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(2).AttValue('ArrivalRate'))
            Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(3).SetAttValue('preARR', Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(3).AttValue('ArrivalRate'))
            Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(4).SetAttValue('preARR', Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(4).AttValue('ArrivalRate'))

            Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(1).SetAttValue('preARR', Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(1).AttValue('ArrivalRate'))
            Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(2).SetAttValue('preARR', Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(2).AttValue('ArrivalRate'))
            Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(3).SetAttValue('preARR', Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(3).AttValue('ArrivalRate'))
            Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(4).SetAttValue('preARR', Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(4).AttValue('ArrivalRate'))



            Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(1).SetAttValue('preARR', Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(1).AttValue('ArrivalRate'))
            Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(2).SetAttValue('preARR', Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(2).AttValue('ArrivalRate'))
            Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(3).SetAttValue('preARR', Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(3).AttValue('ArrivalRate'))
            Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(4).SetAttValue('preARR', Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(4).AttValue('ArrivalRate'))





            Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(1).SetAttValue('preARR', Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(1).AttValue('ArrivalRate'))
            Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(2).SetAttValue('preARR', Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(2).AttValue('ArrivalRate'))
            Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(3).SetAttValue('preARR', Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(3).AttValue('ArrivalRate'))
            Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(4).SetAttValue('preARR', Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(4).AttValue('ArrivalRate'))


            Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(1).SetAttValue('preARR', Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(1).AttValue('ArrivalRate'))
            Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(2).SetAttValue('preARR', Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(2).AttValue('ArrivalRate'))
            Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(3).SetAttValue('preARR', Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(3).AttValue('ArrivalRate'))
            Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(4).SetAttValue('preARR', Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(4).AttValue('ArrivalRate'))




            Vissim.Net.SignalControllers.ItemByKey(12).SGs.ItemByKey(1).SetAttValue('preARR', Vissim.Net.SignalControllers.ItemByKey(12).SGs.ItemByKey(1).AttValue('ArrivalRate'))
            Vissim.Net.SignalControllers.ItemByKey(12).SGs.ItemByKey(2).SetAttValue('preARR', Vissim.Net.SignalControllers.ItemByKey(12).SGs.ItemByKey(2).AttValue('ArrivalRate'))
            Vissim.Net.SignalControllers.ItemByKey(12).SGs.ItemByKey(3).SetAttValue('preARR', Vissim.Net.SignalControllers.ItemByKey(12).SGs.ItemByKey(3).AttValue('ArrivalRate'))
            Vissim.Net.SignalControllers.ItemByKey(12).SGs.ItemByKey(4).SetAttValue('preARR', Vissim.Net.SignalControllers.ItemByKey(12).SGs.ItemByKey(4).AttValue('ArrivalRate'))


            Vissim.Net.SignalControllers.ItemByKey(13).SGs.ItemByKey(1).SetAttValue('preARR', Vissim.Net.SignalControllers.ItemByKey(13).SGs.ItemByKey(1).AttValue('ArrivalRate'))
            Vissim.Net.SignalControllers.ItemByKey(13).SGs.ItemByKey(2).SetAttValue('preARR', Vissim.Net.SignalControllers.ItemByKey(13).SGs.ItemByKey(2).AttValue('ArrivalRate'))
            Vissim.Net.SignalControllers.ItemByKey(13).SGs.ItemByKey(3).SetAttValue('preARR', Vissim.Net.SignalControllers.ItemByKey(13).SGs.ItemByKey(3).AttValue('ArrivalRate'))
            Vissim.Net.SignalControllers.ItemByKey(13).SGs.ItemByKey(4).SetAttValue('preARR', Vissim.Net.SignalControllers.ItemByKey(13).SGs.ItemByKey(4).AttValue('ArrivalRate'))







        if SimSec <= (Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).AttValue('ittearrivalnumber')+1)*ittearrival:            
            for vehAttributes in vehsAttributes:
                if vehAttributes[vehsAttNames['VehType\No']] in vehTypesEquipped:       
                    if vehAttributes[vehsAttNames['Pos']] != None:
                        Link = vehAttributes[vehsAttNames['Lane\Link']]
                        Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).SetAttValue ('LinkNo2',Link)


                        if Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).AttValue ('LinkNo2') == 109:
                            kp109 = Vissim.Net.Detectors.ItemByKey(1).AttValue ('VehNo')        
                            if kp109 > 0:
                                f109= open("109.txt","a")
                                f109.write(str(kp109))
                                f109.write("\n")
                                f109.close()
                                Vissim.Net.Detectors.ItemByKey(1).SetAttValue ('vh',1)



                        if Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).AttValue ('LinkNo2') == 91:
                            kp91 = Vissim.Net.Detectors.ItemByKey(2).AttValue ('VehNo')        
                            if kp91 > 0:
                                f91= open("91.txt","a")
                                f91.write(str(kp91))
                                f91.write("\n")
                                f91.close()
                                Vissim.Net.Detectors.ItemByKey(2).SetAttValue ('vh',1)


                        if Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).AttValue ('LinkNo2') == 89:
                            kp89 = Vissim.Net.Detectors.ItemByKey(3).AttValue ('VehNo')        
                            if kp89 > 0:
                                f89= open("89.txt","a")
                                f89.write(str(kp89))
                                f89.write("\n")
                                f89.close()
                                Vissim.Net.Detectors.ItemByKey(3).SetAttValue ('vh',1)

                        if Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).AttValue ('LinkNo2') == 100:
                            kp100 = Vissim.Net.Detectors.ItemByKey(4).AttValue ('VehNo')        
                            if kp100 > 0:
                                f100= open("100.txt","a")
                                f100.write(str(kp100))
                                f100.write("\n")
                                f100.close()
                                Vissim.Net.Detectors.ItemByKey(4).SetAttValue ('vh',1)







                        if Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).AttValue ('LinkNo2') == 90:
                            kp90 = Vissim.Net.Detectors.ItemByKey(5).AttValue ('VehNo')        
                            if kp90 > 0:
                                f90= open("90.txt","a")
                                f90.write(str(kp90))
                                f90.write("\n")
                                f90.close()
                                Vissim.Net.Detectors.ItemByKey(5).SetAttValue ('vh',1)


                        if Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).AttValue ('LinkNo2') == 66:
                            kp66 = Vissim.Net.Detectors.ItemByKey(6).AttValue ('VehNo')        
                            if kp66 > 0:
                                f66= open("66.txt","a")
                                f66.write(str(kp66))
                                f66.write("\n")
                                f66.close()
                                Vissim.Net.Detectors.ItemByKey(6).SetAttValue ('vh',1)




                        if Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).AttValue ('LinkNo2') == 79:
                            kp79 = Vissim.Net.Detectors.ItemByKey(7).AttValue ('VehNo')        
                            if kp79 > 0:
                                f79= open("79.txt","a")
                                f79.write(str(kp79))
                                f79.write("\n")
                                f79.close()
                                Vissim.Net.Detectors.ItemByKey(7).SetAttValue ('vh',1)


                        if Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).AttValue ('LinkNo2') == 59:
                            kp59 = Vissim.Net.Detectors.ItemByKey(8).AttValue ('VehNo')        
                            if kp59 > 0:
                                f59= open("59.txt","a")
                                f59.write(str(kp59))
                                f59.write("\n")
                                f59.close()
                                Vissim.Net.Detectors.ItemByKey(8).SetAttValue ('vh',1)

                        if Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).AttValue ('LinkNo2') == 80:
                            kp80 = Vissim.Net.Detectors.ItemByKey(9).AttValue ('VehNo')        
                            if kp80 > 0:
                                f80= open("80.txt","a")
                                f80.write(str(kp80))
                                f80.write("\n")
                                f80.close()
                                Vissim.Net.Detectors.ItemByKey(9).SetAttValue ('vh',1)


                        if Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).AttValue ('LinkNo2') == 68:
                            kp68 = Vissim.Net.Detectors.ItemByKey(10).AttValue ('VehNo')        
                            if kp68 > 0:
                                f68= open("68.txt","a")
                                f68.write(str(kp68))
                                f68.write("\n")
                                f68.close()
                                Vissim.Net.Detectors.ItemByKey(10).SetAttValue ('vh',1)



                        if Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).AttValue ('LinkNo2') == 81:
                            kp81 = Vissim.Net.Detectors.ItemByKey(11).AttValue ('VehNo')        
                            if kp81 > 0:
                                f81= open("81.txt","a")
                                f81.write(str(kp81))
                                f81.write("\n")
                                f81.close()
                                Vissim.Net.Detectors.ItemByKey(11).SetAttValue ('vh',1)

                        if Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).AttValue ('LinkNo2') == 61:
                            kp61 = Vissim.Net.Detectors.ItemByKey(12).AttValue ('VehNo')        
                            if kp61 > 0:
                                f61= open("61.txt","a")
                                f61.write(str(kp61))
                                f61.write("\n")
                                f61.close()
                                Vissim.Net.Detectors.ItemByKey(12).SetAttValue ('vh',1)




                        if Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).AttValue ('LinkNo2') == 61:
                            kp61 = Vissim.Net.Detectors.ItemByKey(12).AttValue ('VehNo')        
                            if kp61 > 0:
                                f61= open("61.txt","a")
                                f61.write(str(kp61))
                                f61.write("\n")
                                f61.close()
                                Vissim.Net.Detectors.ItemByKey(12).SetAttValue ('vh',1)



                        if Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).AttValue ('LinkNo2') == 82:
                            kp82 = Vissim.Net.Detectors.ItemByKey(13).AttValue ('VehNo')        
                            if kp82 > 0:
                                f82= open("82.txt","a")
                                f82.write(str(kp82))
                                f82.write("\n")
                                f82.close()
                                Vissim.Net.Detectors.ItemByKey(13).SetAttValue ('vh',1)


                        if Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).AttValue ('LinkNo2') == 70:
                            kp70 = Vissim.Net.Detectors.ItemByKey(14).AttValue ('VehNo')        
                            if kp70 > 0:
                                f70= open("70.txt","a")
                                f70.write(str(kp70))
                                f70.write("\n")
                                f70.close()
                                Vissim.Net.Detectors.ItemByKey(14).SetAttValue ('vh',1)


                        if Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).AttValue ('LinkNo2') == 87:
                            kp87 = Vissim.Net.Detectors.ItemByKey(15).AttValue ('VehNo')        
                            if kp87 > 0:
                                f87= open("87.txt","a")
                                f87.write(str(kp87))
                                f87.write("\n")
                                f87.close()
                                Vissim.Net.Detectors.ItemByKey(15).SetAttValue ('vh',1)

                        if Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).AttValue ('LinkNo2') == 63:
                            kp63 = Vissim.Net.Detectors.ItemByKey(16).AttValue ('VehNo')        
                            if kp63 > 0:
                                f63= open("63.txt","a")
                                f63.write(str(kp63))
                                f63.write("\n")
                                f63.close()
                                Vissim.Net.Detectors.ItemByKey(16).SetAttValue ('vh',1)






                        if Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).AttValue ('LinkNo2') == 108:
                            kp108 = Vissim.Net.Detectors.ItemByKey(17).AttValue ('VehNo')        
                            if kp108 > 0:
                                f108= open("108.txt","a")
                                f108.write(str(kp108))
                                f108.write("\n")
                                f108.close()
                                Vissim.Net.Detectors.ItemByKey(17).SetAttValue ('vh',1)

                        if Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).AttValue ('LinkNo2') == 103:
                            kp103 = Vissim.Net.Detectors.ItemByKey(18).AttValue ('VehNo')        
                            if kp103 > 0:
                                f103= open("103.txt","a")
                                f103.write(str(kp103))
                                f103.write("\n")
                                f103.close()
                                Vissim.Net.Detectors.ItemByKey(18).SetAttValue ('vh',1)


                        if Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).AttValue ('LinkNo2') == 88:
                            kp88 = Vissim.Net.Detectors.ItemByKey(19).AttValue ('VehNo')        
                            if kp88 > 0:
                                f88= open("88.txt","a")
                                f88.write(str(kp88))
                                f88.write("\n")
                                f88.close()
                                Vissim.Net.Detectors.ItemByKey(19).SetAttValue ('vh',1)

                        if Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).AttValue ('LinkNo2') == 98:
                            kp98 = Vissim.Net.Detectors.ItemByKey(20).AttValue ('VehNo')        
                            if kp98 > 0:
                                f98= open("98.txt","a")
                                f98.write(str(kp98))
                                f98.write("\n")
                                f98.close()
                                Vissim.Net.Detectors.ItemByKey(20).SetAttValue ('vh',1)


                        if Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).AttValue ('LinkNo2') == 92:
                            kp92 = Vissim.Net.Detectors.ItemByKey(21).AttValue ('VehNo')        
                            if kp92 > 0:
                                f92= open("92.txt","a")
                                f92.write(str(kp92))
                                f92.write("\n")
                                f92.close()
                                Vissim.Net.Detectors.ItemByKey(21).SetAttValue ('vh',1)


                        if Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).AttValue ('LinkNo2') == 60:
                            kp60 = Vissim.Net.Detectors.ItemByKey(22).AttValue ('VehNo')        
                            if kp60 > 0:
                                f60= open("60.txt","a")
                                f60.write(str(kp60))
                                f60.write("\n")
                                f60.close()
                                Vissim.Net.Detectors.ItemByKey(22).SetAttValue ('vh',1)

                        if Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).AttValue ('LinkNo2') == 71:
                            kp71 = Vissim.Net.Detectors.ItemByKey(23).AttValue ('VehNo')        
                            if kp71 > 0:
                                f71= open("71.txt","a")
                                f71.write(str(kp71))
                                f71.write("\n")
                                f71.close()
                                Vissim.Net.Detectors.ItemByKey(23).SetAttValue ('vh',1)


                        if Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).AttValue ('LinkNo2') == 93:
                            kp93 = Vissim.Net.Detectors.ItemByKey(24).AttValue ('VehNo')        
                            if kp93 > 0:
                                f93= open("93.txt","a")
                                f93.write(str(kp93))
                                f93.write("\n")
                                f93.close()
                                Vissim.Net.Detectors.ItemByKey(24).SetAttValue ('vh',1)


                        if Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).AttValue ('LinkNo2') == 72:
                            kp72 = Vissim.Net.Detectors.ItemByKey(25).AttValue ('VehNo')        
                            if kp72 > 0:
                                f72= open("72.txt","a")
                                f72.write(str(kp72))
                                f72.write("\n")
                                f72.close()
                                Vissim.Net.Detectors.ItemByKey(25).SetAttValue ('vh',1)

                        if Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).AttValue ('LinkNo2') == 62:
                            kp62 = Vissim.Net.Detectors.ItemByKey(26).AttValue ('VehNo')        
                            if kp62 > 0:
                                f62= open("62.txt","a")
                                f62.write(str(kp62))
                                f62.write("\n")
                                f62.close()
                                Vissim.Net.Detectors.ItemByKey(26).SetAttValue ('vh',1)

                        if Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).AttValue ('LinkNo2') == 73:
                            kp73 = Vissim.Net.Detectors.ItemByKey(27).AttValue ('VehNo')        
                            if kp73 > 0:
                                f73= open("73.txt","a")
                                f73.write(str(kp73))
                                f73.write("\n")
                                f73.close()
                                Vissim.Net.Detectors.ItemByKey(27).SetAttValue ('vh',1)

                        if Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).AttValue ('LinkNo2') == 83:
                            kp83 = Vissim.Net.Detectors.ItemByKey(28).AttValue ('VehNo')        
                            if kp83 > 0:
                                f83= open("83.txt","a")
                                f83.write(str(kp83))
                                f83.write("\n")
                                f83.close()
                                Vissim.Net.Detectors.ItemByKey(28).SetAttValue ('vh',1)


                        if Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).AttValue ('LinkNo2') == 74:
                            kp74 = Vissim.Net.Detectors.ItemByKey(29).AttValue ('VehNo')        
                            if kp74 > 0:
                                f74= open("74.txt","a")
                                f74.write(str(kp74))
                                f74.write("\n")
                                f74.close()
                                Vissim.Net.Detectors.ItemByKey(29).SetAttValue ('vh',1)

                        if Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).AttValue ('LinkNo2') == 64:
                            kp64 = Vissim.Net.Detectors.ItemByKey(30).AttValue ('VehNo')        
                            if kp64 > 0:
                                f64= open("64.txt","a")
                                f64.write(str(kp64))
                                f64.write("\n")
                                f64.close()
                                Vissim.Net.Detectors.ItemByKey(30).SetAttValue ('vh',1)

                        if Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).AttValue ('LinkNo2') == 104:
                            kp104 = Vissim.Net.Detectors.ItemByKey(31).AttValue ('VehNo')        
                            if kp104 > 0:
                                f104= open("104.txt","a")
                                f104.write(str(kp104))
                                f104.write("\n")
                                f104.close()
                                Vissim.Net.Detectors.ItemByKey(31).SetAttValue ('vh',1)



                        if Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).AttValue ('LinkNo2') == 105:
                            kp105 = Vissim.Net.Detectors.ItemByKey(32).AttValue ('VehNo')        
                            if kp105 > 0:
                                f105= open("105.txt","a")
                                f105.write(str(kp105))
                                f105.write("\n")
                                f105.close()
                                Vissim.Net.Detectors.ItemByKey(32).SetAttValue ('vh',1)



                        if Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).AttValue ('LinkNo2') == 99:
                            kp99 = Vissim.Net.Detectors.ItemByKey(33).AttValue ('VehNo')        
                            if kp99 > 0:
                                f99= open("99.txt","a")
                                f99.write(str(kp99))
                                f99.write("\n")
                                f99.close()
                                Vissim.Net.Detectors.ItemByKey(33).SetAttValue ('vh',1)

                        if Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).AttValue ('LinkNo2') == 75:
                            kp75 = Vissim.Net.Detectors.ItemByKey(34).AttValue ('VehNo')        
                            if kp75 > 0:
                                f75= open("75.txt","a")
                                f75.write(str(kp75))
                                f75.write("\n")
                                f75.close()
                                Vissim.Net.Detectors.ItemByKey(34).SetAttValue ('vh',1)


                        if Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).AttValue ('LinkNo2') == 65:
                            kp65 = Vissim.Net.Detectors.ItemByKey(35).AttValue ('VehNo')        
                            if kp65 > 0:
                                f65= open("65.txt","a")
                                f65.write(str(kp65))
                                f65.write("\n")
                                f65.close()
                                Vissim.Net.Detectors.ItemByKey(35).SetAttValue ('vh',1)


                        if Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).AttValue ('LinkNo2') == 102:
                            kp102 = Vissim.Net.Detectors.ItemByKey(36).AttValue ('VehNo')        
                            if kp102 > 0:
                                f102= open("102.txt","a")
                                f102.write(str(kp102))
                                f102.write("\n")
                                f102.close()
                                Vissim.Net.Detectors.ItemByKey(36).SetAttValue ('vh',1)


                        if Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).AttValue ('LinkNo2') == 76:
                            kp76 = Vissim.Net.Detectors.ItemByKey(37).AttValue ('VehNo')        
                            if kp76 > 0:
                                f76= open("76.txt","a")
                                f76.write(str(kp76))
                                f76.write("\n")
                                f76.close()
                                Vissim.Net.Detectors.ItemByKey(37).SetAttValue ('vh',1)

                        if Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).AttValue ('LinkNo2') == 76:
                            kp76 = Vissim.Net.Detectors.ItemByKey(37).AttValue ('VehNo')        
                            if kp76 > 0:
                                f76= open("76.txt","a")
                                f76.write(str(kp76))
                                f76.write("\n")
                                f76.close()
                                Vissim.Net.Detectors.ItemByKey(37).SetAttValue ('vh',1)


                        if Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).AttValue ('LinkNo2') == 67:
                            kp67 = Vissim.Net.Detectors.ItemByKey(39).AttValue ('VehNo')        
                            if kp67 > 0:
                                f67= open("67.txt","a")
                                f67.write(str(kp67))
                                f67.write("\n")
                                f67.close()
                                Vissim.Net.Detectors.ItemByKey(39).SetAttValue ('vh',1)


                        if Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).AttValue ('LinkNo2') == 86:
                            kp86 = Vissim.Net.Detectors.ItemByKey(40).AttValue ('VehNo')        
                            if kp86 > 0:
                                f86= open("86.txt","a")
                                f86.write(str(kp86))
                                f86.write("\n")
                                f86.close()
                                Vissim.Net.Detectors.ItemByKey(40).SetAttValue ('vh',1)


                        if Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).AttValue ('LinkNo2') == 78:
                            kp78 = Vissim.Net.Detectors.ItemByKey(41).AttValue ('VehNo')        
                            if kp78 > 0:
                                f78= open("78.txt","a")
                                f78.write(str(kp78))
                                f78.write("\n")
                                f78.close()
                                Vissim.Net.Detectors.ItemByKey(41).SetAttValue ('vh',1)

                        if Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).AttValue ('LinkNo2') == 97:
                            kp97 = Vissim.Net.Detectors.ItemByKey(42).AttValue ('VehNo')        
                            if kp97 > 0:
                                f97= open("97.txt","a")
                                f97.write(str(kp97))
                                f97.write("\n")
                                f97.close()
                                Vissim.Net.Detectors.ItemByKey(42).SetAttValue ('vh',1)


                        if Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).AttValue ('LinkNo2') == 69:
                            kp69 = Vissim.Net.Detectors.ItemByKey(43).AttValue ('VehNo')        
                            if kp69 > 0:
                                f69= open("69.txt","a")
                                f69.write(str(kp69))
                                f69.write("\n")
                                f69.close()
                                Vissim.Net.Detectors.ItemByKey(43).SetAttValue ('vh',1)


                        if Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).AttValue ('LinkNo2') == 96:
                            kp96 = Vissim.Net.Detectors.ItemByKey(44).AttValue ('VehNo')        
                            if kp96 > 0:
                                f96= open("96.txt","a")
                                f96.write(str(kp96))
                                f96.write("\n")
                                f96.close()
                                Vissim.Net.Detectors.ItemByKey(44).SetAttValue ('vh',1)


                        if Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).AttValue ('LinkNo2') == 112:
                            kp112 = Vissim.Net.Detectors.ItemByKey(45).AttValue ('VehNo')        
                            if kp112 > 0:
                                f112= open("112.txt","a")
                                f112.write(str(kp112))
                                f112.write("\n")
                                f112.close()
                                Vissim.Net.Detectors.ItemByKey(45).SetAttValue ('vh',1)

                        if Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).AttValue ('LinkNo2') == 95:
                            kp95 = Vissim.Net.Detectors.ItemByKey(46).AttValue ('VehNo')        
                            if kp95 > 0:
                                f95= open("95.txt","a")
                                f95.write(str(kp95))
                                f95.write("\n")
                                f95.close()
                                Vissim.Net.Detectors.ItemByKey(46).SetAttValue ('vh',1)

                        if Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).AttValue ('LinkNo2') == 85:
                            kp85 = Vissim.Net.Detectors.ItemByKey(47).AttValue ('VehNo')        
                            if kp85 > 0:
                                f85= open("85.txt","a")
                                f85.write(str(kp85))
                                f85.write("\n")
                                f85.close()
                                Vissim.Net.Detectors.ItemByKey(47).SetAttValue ('vh',1)


                        if Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).AttValue ('LinkNo2') == 101:
                            kp101 = Vissim.Net.Detectors.ItemByKey(48).AttValue ('VehNo')        
                            if kp101 > 0:
                                f101= open("101.txt","a")
                                f101.write(str(kp101))
                                f101.write("\n")
                                f101.close()
                                Vissim.Net.Detectors.ItemByKey(48).SetAttValue ('vh',1)


                        if Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).AttValue ('LinkNo2') == 113:
                            kp113 = Vissim.Net.Detectors.ItemByKey(49).AttValue ('VehNo')        
                            if kp113 > 0:
                                f113= open("113.txt","a")
                                f113.write(str(kp113))
                                f113.write("\n")
                                f113.close()
                                Vissim.Net.Detectors.ItemByKey(49).SetAttValue ('vh',1)


                        if Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).AttValue ('LinkNo2') == 106:
                            kp106 = Vissim.Net.Detectors.ItemByKey(50).AttValue ('VehNo')        
                            if kp106 > 0:
                                f106= open("106.txt","a")
                                f106.write(str(kp106))
                                f106.write("\n")
                                f106.close()
                                Vissim.Net.Detectors.ItemByKey(50).SetAttValue ('vh',1)

                        if Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).AttValue ('LinkNo2') == 84:
                            kp84 = Vissim.Net.Detectors.ItemByKey(51).AttValue ('VehNo')        
                            if kp84 > 0:
                                f84= open("84.txt","a")
                                f84.write(str(kp84))
                                f84.write("\n")
                                f84.close()
                                Vissim.Net.Detectors.ItemByKey(51).SetAttValue ('vh',1)

                        if Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).AttValue ('LinkNo2') == 94:
                            kp94 = Vissim.Net.Detectors.ItemByKey(52).AttValue ('VehNo')        
                            if kp94 > 0:
                                f94= open("94.txt","a")
                                f94.write(str(kp94))
                                f94.write("\n")
                                f94.close()
                                Vissim.Net.Detectors.ItemByKey(52).SetAttValue ('vh',1)






















                continue



        if SimSec >= (Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).AttValue('ittearrivalnumber')+1)*ittearrival-1:

                Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).SetAttValue('ittearrivalnumber',Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).AttValue('DB'))

                if Vissim.Net.Detectors.ItemByKey(1).AttValue ('vh')==1:
                    f109 = open("109.txt","r")                        
                    ggg109 = f109.readlines()
                    f109.close()
                    s109=[]
                    for x in ggg109:
                        if x not in s109:
                            s109.append(x)
                    kk109=len(s109)
                    Vissim.Net.Detectors.ItemByKey(1).SetAttValue ('VehicleNumber',kk109)
                    arrivalrate109=round(Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).AttValue('preARR')+  KalmanGain* (((Vissim.Net.Detectors.ItemByKey(1).AttValue ('VehicleNumber')/(proportion_of_CAVs*ittearrival))*3600)- Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).AttValue('preARR')))
                    Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).SetAttValue ('ArrivalRate',arrivalrate109)


                if Vissim.Net.Detectors.ItemByKey(1).AttValue ('vh')==0:
                    s109=[]                    
                    kk109=len(s109)
                    Vissim.Net.Detectors.ItemByKey(1).SetAttValue ('VehicleNumber',kk109)
                    arrivalrate109=round(Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).AttValue('preARR')+  KalmanGain* (((Vissim.Net.Detectors.ItemByKey(1).AttValue ('VehicleNumber')/(proportion_of_CAVs*ittearrival))*3600)- Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).AttValue('preARR')))
                    Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).SetAttValue ('ArrivalRate',arrivalrate109)



                if Vissim.Net.Detectors.ItemByKey(2).AttValue ('vh')==1:
                    f91 = open("91.txt","r")                        
                    ggg91 = f91.readlines()
                    f91.close()
                    s91=[]
                    for x in ggg91:
                        if x not in s91:
                            s91.append(x)
                    kk91=len(s91)
                    Vissim.Net.Detectors.ItemByKey(2).SetAttValue ('VehicleNumber',kk91)
                    arrivalrate91=round(Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(2).AttValue('preARR')+  KalmanGain* (((Vissim.Net.Detectors.ItemByKey(2).AttValue ('VehicleNumber')/(proportion_of_CAVs*ittearrival))*3600)- Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(2).AttValue('preARR')))
                    Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(2).SetAttValue ('ArrivalRate',arrivalrate91)     
                if Vissim.Net.Detectors.ItemByKey(2).AttValue ('vh')==0:
                    s91=[]                    
                    kk91=len(s91)
                    Vissim.Net.Detectors.ItemByKey(2).SetAttValue ('VehicleNumber',kk91)
                    arrivalrate91=round(Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(2).AttValue('preARR')+  KalmanGain* (((Vissim.Net.Detectors.ItemByKey(2).AttValue ('VehicleNumber')/(proportion_of_CAVs*ittearrival))*3600)- Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(2).AttValue('preARR')))
                    Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(2).SetAttValue ('ArrivalRate',arrivalrate91)


                if Vissim.Net.Detectors.ItemByKey(3).AttValue ('vh')==1:
                    f89 = open("89.txt","r")                        
                    ggg89 = f89.readlines()
                    f89.close()
                    s89=[]
                    for x in ggg89:
                        if x not in s89:
                            s89.append(x)
                    kk89=len(s89)
                    Vissim.Net.Detectors.ItemByKey(3).SetAttValue ('VehicleNumber',kk89)
                    arrivalrate89=round(Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(3).AttValue('preARR')+  KalmanGain* (((Vissim.Net.Detectors.ItemByKey(3).AttValue ('VehicleNumber')/(proportion_of_CAVs*ittearrival))*3600)- Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(3).AttValue('preARR')))
                    Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(3).SetAttValue ('ArrivalRate',arrivalrate89)     
                if Vissim.Net.Detectors.ItemByKey(3).AttValue ('vh')==0:
                    s89=[]                    
                    kk89=len(s89)
                    Vissim.Net.Detectors.ItemByKey(3).SetAttValue ('VehicleNumber',kk89)
                    arrivalrate89=round(Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(3).AttValue('preARR')+  KalmanGain* (((Vissim.Net.Detectors.ItemByKey(3).AttValue ('VehicleNumber')/(proportion_of_CAVs*ittearrival))*3600)- Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(3).AttValue('preARR')))
                    Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(3).SetAttValue ('ArrivalRate',arrivalrate89)


                if Vissim.Net.Detectors.ItemByKey(4).AttValue ('vh')==1:
                    f100 = open("100.txt","r")                        
                    ggg100 = f100.readlines()
                    f100.close()
                    s100=[]
                    for x in ggg100:
                        if x not in s100:
                            s100.append(x)
                    kk100=len(s100)
                    Vissim.Net.Detectors.ItemByKey(4).SetAttValue ('VehicleNumber',kk100)
                    arrivalrate100=round(Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(4).AttValue('preARR')+  KalmanGain* (((Vissim.Net.Detectors.ItemByKey(4).AttValue ('VehicleNumber')/(proportion_of_CAVs*ittearrival))*3600)- Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(4).AttValue('preARR')))
                    Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(4).SetAttValue ('ArrivalRate',arrivalrate100)     
                if Vissim.Net.Detectors.ItemByKey(4).AttValue ('vh')==0:
                    s100=[]                    
                    kk100=len(s100)
                    Vissim.Net.Detectors.ItemByKey(4).SetAttValue ('VehicleNumber',kk100)
                    arrivalrate100=round(Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(4).AttValue('preARR')+  KalmanGain* (((Vissim.Net.Detectors.ItemByKey(4).AttValue ('VehicleNumber')/(proportion_of_CAVs*ittearrival))*3600)- Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(4).AttValue('preARR')))

                    Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(4).SetAttValue ('ArrivalRate',arrivalrate100)




                if Vissim.Net.Detectors.ItemByKey(5).AttValue ('vh')==1:
                    f90 = open("90.txt","r")                        
                    ggg90 = f90.readlines()
                    f90.close()
                    s90=[]
                    for x in ggg90:
                        if x not in s90:
                            s90.append(x)
                    kk90=len(s90)
                    Vissim.Net.Detectors.ItemByKey(5).SetAttValue ('VehicleNumber',kk90)
                    arrivalrate90=round(Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(1).AttValue('preARR')+  KalmanGain* (((Vissim.Net.Detectors.ItemByKey(5).AttValue ('VehicleNumber')/(proportion_of_CAVs*ittearrival))*3600)- Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(1).AttValue('preARR')))
                    Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(1).SetAttValue ('ArrivalRate',arrivalrate90)     
                if Vissim.Net.Detectors.ItemByKey(5).AttValue ('vh')==0:
                    s90=[]                    
                    kk90=len(s90)
                    Vissim.Net.Detectors.ItemByKey(5).SetAttValue ('VehicleNumber',kk90)
                    arrivalrate90=round(Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(1).AttValue('preARR')+  KalmanGain* (((Vissim.Net.Detectors.ItemByKey(5).AttValue ('VehicleNumber')/(proportion_of_CAVs*ittearrival))*3600)- Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(1).AttValue('preARR')))

                    Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(1).SetAttValue ('ArrivalRate',arrivalrate90)








                if Vissim.Net.Detectors.ItemByKey(6).AttValue ('vh')==1:
                    f66 = open("66.txt","r")                        
                    ggg66 = f66.readlines()
                    f66.close()
                    s66=[]
                    for x in ggg66:
                        if x not in s66:
                            s66.append(x)
                    kk66=len(s66)
                    Vissim.Net.Detectors.ItemByKey(6).SetAttValue ('VehicleNumber',kk66)
                    arrivalrate66=round(Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(2).AttValue('preARR')+  KalmanGain* (((Vissim.Net.Detectors.ItemByKey(6).AttValue ('VehicleNumber')/(proportion_of_CAVs*ittearrival))*3600)- Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(2).AttValue('preARR')))
                    Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(2).SetAttValue ('ArrivalRate',arrivalrate66)     
                if Vissim.Net.Detectors.ItemByKey(6).AttValue ('vh')==0:
                    s66=[]                    
                    kk66=len(s66)
                    Vissim.Net.Detectors.ItemByKey(6).SetAttValue ('VehicleNumber',kk66)
                    arrivalrate66=round(Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(2).AttValue('preARR')+  KalmanGain* (((Vissim.Net.Detectors.ItemByKey(6).AttValue ('VehicleNumber')/(proportion_of_CAVs*ittearrival))*3600)- Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(2).AttValue('preARR')))

                    Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(2).SetAttValue ('ArrivalRate',arrivalrate66)




                if Vissim.Net.Detectors.ItemByKey(7).AttValue ('vh')==1:
                    f79 = open("79.txt","r")                        
                    ggg79 = f79.readlines()
                    f79.close()
                    s79=[]
                    for x in ggg79:
                        if x not in s79:
                            s79.append(x)
                    kk79=len(s79)
                    Vissim.Net.Detectors.ItemByKey(7).SetAttValue ('VehicleNumber',kk79)
                    arrivalrate79=round(Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(3).AttValue('preARR')+  KalmanGain* (((Vissim.Net.Detectors.ItemByKey(7).AttValue ('VehicleNumber')/(proportion_of_CAVs*ittearrival))*3600)- Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(3).AttValue('preARR')))
                    Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(3).SetAttValue ('ArrivalRate',arrivalrate79)     
                if Vissim.Net.Detectors.ItemByKey(7).AttValue ('vh')==0:
                    s79=[]                    
                    kk79=len(s79)
                    Vissim.Net.Detectors.ItemByKey(7).SetAttValue ('VehicleNumber',kk79)
                    arrivalrate79=round(Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(3).AttValue('preARR')+  KalmanGain* (((Vissim.Net.Detectors.ItemByKey(7).AttValue ('VehicleNumber')/(proportion_of_CAVs*ittearrival))*3600)- Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(3).AttValue('preARR')))

                    Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(3).SetAttValue ('ArrivalRate',arrivalrate79)





                if Vissim.Net.Detectors.ItemByKey(8).AttValue ('vh')==1:
                    f59 = open("59.txt","r")                        
                    ggg59 = f59.readlines()
                    f59.close()
                    s59=[]
                    for x in ggg59:
                        if x not in s59:
                            s59.append(x)
                    kk59=len(s59)
                    Vissim.Net.Detectors.ItemByKey(8).SetAttValue ('VehicleNumber',kk59)
                    arrivalrate59=round(Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(4).AttValue('preARR')+  KalmanGain* (((Vissim.Net.Detectors.ItemByKey(8).AttValue ('VehicleNumber')/(proportion_of_CAVs*ittearrival))*3600)- Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(4).AttValue('preARR')))
                    Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(4).SetAttValue ('ArrivalRate',arrivalrate59)     
                if Vissim.Net.Detectors.ItemByKey(8).AttValue ('vh')==0:
                    s59=[]                    
                    kk59=len(s59)
                    Vissim.Net.Detectors.ItemByKey(8).SetAttValue ('VehicleNumber',kk59)
                    arrivalrate59=round(Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(4).AttValue('preARR')+  KalmanGain* (((Vissim.Net.Detectors.ItemByKey(8).AttValue ('VehicleNumber')/(proportion_of_CAVs*ittearrival))*3600)- Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(4).AttValue('preARR')))

                    Vissim.Net.SignalControllers.ItemByKey(2).SGs.ItemByKey(4).SetAttValue ('ArrivalRate',arrivalrate59)



                if Vissim.Net.Detectors.ItemByKey(9).AttValue ('vh')==1:
                    f80 = open("80.txt","r")                        
                    ggg80 = f80.readlines()
                    f80.close()
                    s80=[]
                    for x in ggg80:
                        if x not in s80:
                            s80.append(x)
                    kk80=len(s80)
                    Vissim.Net.Detectors.ItemByKey(9).SetAttValue ('VehicleNumber',kk80)
                    arrivalrate80=round(Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(1).AttValue('preARR')+  KalmanGain* (((Vissim.Net.Detectors.ItemByKey(9).AttValue ('VehicleNumber')/(proportion_of_CAVs*ittearrival))*3600)- Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(1).AttValue('preARR')))
                    Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(1).SetAttValue ('ArrivalRate',arrivalrate80)     
                if Vissim.Net.Detectors.ItemByKey(9).AttValue ('vh')==0:
                    s80=[]                    
                    kk80=len(s80)
                    Vissim.Net.Detectors.ItemByKey(9).SetAttValue ('VehicleNumber',kk80)
                    arrivalrate80=round(Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(1).AttValue('preARR')+  KalmanGain* (((Vissim.Net.Detectors.ItemByKey(9).AttValue ('VehicleNumber')/(proportion_of_CAVs*ittearrival))*3600)- Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(1).AttValue('preARR')))
                    Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(1).SetAttValue ('ArrivalRate',arrivalrate80)   



                if Vissim.Net.Detectors.ItemByKey(10).AttValue ('vh')==1:
                    f68 = open("68.txt","r")                        
                    ggg68 = f68.readlines()
                    f68.close()
                    s68=[]
                    for x in ggg68:
                        if x not in s68:
                            s68.append(x)
                    kk68=len(s68)
                    Vissim.Net.Detectors.ItemByKey(10).SetAttValue ('VehicleNumber',kk68)
                    arrivalrate68=round(Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(2).AttValue('preARR')+  KalmanGain* (((Vissim.Net.Detectors.ItemByKey(10).AttValue ('VehicleNumber')/(proportion_of_CAVs*ittearrival))*3600)- Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(2).AttValue('preARR')))
                    Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(2).SetAttValue ('ArrivalRate',arrivalrate68)     
                if Vissim.Net.Detectors.ItemByKey(10).AttValue ('vh')==0:
                    s68=[]                    
                    kk68=len(s68)
                    Vissim.Net.Detectors.ItemByKey(10).SetAttValue ('VehicleNumber',kk68)
                    arrivalrate68=round(Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(2).AttValue('preARR')+  KalmanGain* (((Vissim.Net.Detectors.ItemByKey(10).AttValue ('VehicleNumber')/(proportion_of_CAVs*ittearrival))*3600)- Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(2).AttValue('preARR')))
                    Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(2).SetAttValue ('ArrivalRate',arrivalrate68) 



                if Vissim.Net.Detectors.ItemByKey(11).AttValue ('vh')==1:
                    f81 = open("81.txt","r")                        
                    ggg81 = f81.readlines()
                    f81.close()
                    s81=[]
                    for x in ggg81:
                        if x not in s81:
                            s81.append(x)
                    kk81=len(s81)
                    Vissim.Net.Detectors.ItemByKey(11).SetAttValue ('VehicleNumber',kk81)
                    arrivalrate81=round(Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(3).AttValue('preARR')+  KalmanGain* (((Vissim.Net.Detectors.ItemByKey(11).AttValue ('VehicleNumber')/(proportion_of_CAVs*ittearrival))*3600)- Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(3).AttValue('preARR')))
                    Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(3).SetAttValue ('ArrivalRate',arrivalrate81)     
                if Vissim.Net.Detectors.ItemByKey(11).AttValue ('vh')==0:
                    s81=[]                    
                    kk81=len(s81)
                    Vissim.Net.Detectors.ItemByKey(11).SetAttValue ('VehicleNumber',kk81)
                    arrivalrate81=round(Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(3).AttValue('preARR')+  KalmanGain* (((Vissim.Net.Detectors.ItemByKey(11).AttValue ('VehicleNumber')/(proportion_of_CAVs*ittearrival))*3600)- Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(3).AttValue('preARR')))
                    Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(3).SetAttValue ('ArrivalRate',arrivalrate81)    



                if Vissim.Net.Detectors.ItemByKey(12).AttValue ('vh')==1:
                    f61 = open("61.txt","r")                        
                    ggg61 = f61.readlines()
                    f61.close()
                    s61=[]
                    for x in ggg61:
                        if x not in s61:
                            s61.append(x)
                    kk61=len(s61)
                    Vissim.Net.Detectors.ItemByKey(12).SetAttValue ('VehicleNumber',kk61)
                    arrivalrate61=round(Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(4).AttValue('preARR')+  KalmanGain* (((Vissim.Net.Detectors.ItemByKey(12).AttValue ('VehicleNumber')/(proportion_of_CAVs*ittearrival))*3600)- Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(4).AttValue('preARR')))
                    Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(4).SetAttValue ('ArrivalRate',arrivalrate61)     
                if Vissim.Net.Detectors.ItemByKey(12).AttValue ('vh')==0:
                    s61=[]                    
                    kk61=len(s61)
                    Vissim.Net.Detectors.ItemByKey(12).SetAttValue ('VehicleNumber',kk61)
                    arrivalrate61=round(Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(4).AttValue('preARR')+  KalmanGain* (((Vissim.Net.Detectors.ItemByKey(12).AttValue ('VehicleNumber')/(proportion_of_CAVs*ittearrival))*3600)- Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(4).AttValue('preARR')))
                    Vissim.Net.SignalControllers.ItemByKey(3).SGs.ItemByKey(4).SetAttValue ('ArrivalRate',arrivalrate61) 




                if Vissim.Net.Detectors.ItemByKey(13).AttValue ('vh')==1:
                    f82 = open("82.txt","r")                        
                    ggg82 = f82.readlines()
                    f82.close()
                    s82=[]
                    for x in ggg82:
                        if x not in s82:
                            s82.append(x)
                    kk82=len(s82)
                    Vissim.Net.Detectors.ItemByKey(13).SetAttValue ('VehicleNumber',kk82)
                    arrivalrate82=round(Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(1).AttValue('preARR')+  KalmanGain* (((Vissim.Net.Detectors.ItemByKey(13).AttValue ('VehicleNumber')/(proportion_of_CAVs*ittearrival))*3600)- Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(1).AttValue('preARR')))
                    Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(1).SetAttValue ('ArrivalRate',arrivalrate82)


                if Vissim.Net.Detectors.ItemByKey(13).AttValue ('vh')==0:
                    s82=[]                    
                    kk82=len(s82)
                    Vissim.Net.Detectors.ItemByKey(13).SetAttValue ('VehicleNumber',kk82)
                    arrivalrate82=round(Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(1).AttValue('preARR')+  KalmanGain* (((Vissim.Net.Detectors.ItemByKey(13).AttValue ('VehicleNumber')/(proportion_of_CAVs*ittearrival))*3600)- Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(1).AttValue('preARR')))
                    Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(1).SetAttValue ('ArrivalRate',arrivalrate82)



                if Vissim.Net.Detectors.ItemByKey(14).AttValue ('vh')==1:
                    f70 = open("70.txt","r")                        
                    ggg70 = f70.readlines()
                    f70.close()
                    s70=[]
                    for x in ggg70:
                        if x not in s70:
                            s70.append(x)
                    kk70=len(s70)
                    Vissim.Net.Detectors.ItemByKey(14).SetAttValue ('VehicleNumber',kk70)
                    arrivalrate70=round(Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(2).AttValue('preARR')+  KalmanGain* (((Vissim.Net.Detectors.ItemByKey(14).AttValue ('VehicleNumber')/(proportion_of_CAVs*ittearrival))*3600)- Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(2).AttValue('preARR')))
                    Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(2).SetAttValue ('ArrivalRate',arrivalrate70)


                if Vissim.Net.Detectors.ItemByKey(14).AttValue ('vh')==0:
                    s70=[]                    
                    kk70=len(s70)
                    Vissim.Net.Detectors.ItemByKey(14).SetAttValue ('VehicleNumber',kk70)
                    arrivalrate70=round(Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(2).AttValue('preARR')+  KalmanGain* (((Vissim.Net.Detectors.ItemByKey(14).AttValue ('VehicleNumber')/(proportion_of_CAVs*ittearrival))*3600)- Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(2).AttValue('preARR')))
                    Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(2).SetAttValue ('ArrivalRate',arrivalrate70)



                if Vissim.Net.Detectors.ItemByKey(15).AttValue ('vh')==1:
                    f87 = open("87.txt","r")                        
                    ggg87 = f87.readlines()
                    f87.close()
                    s87=[]
                    for x in ggg87:
                        if x not in s87:
                            s87.append(x)
                    kk87=len(s87)
                    Vissim.Net.Detectors.ItemByKey(15).SetAttValue ('VehicleNumber',kk87)
                    arrivalrate87=round(Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(3).AttValue('preARR')+  KalmanGain* (((Vissim.Net.Detectors.ItemByKey(15).AttValue ('VehicleNumber')/(proportion_of_CAVs*ittearrival))*3600)- Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(3).AttValue('preARR')))
                    Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(3).SetAttValue ('ArrivalRate',arrivalrate87)


                if Vissim.Net.Detectors.ItemByKey(15).AttValue ('vh')==0:
                    s87=[]                    
                    kk87=len(s87)
                    Vissim.Net.Detectors.ItemByKey(15).SetAttValue ('VehicleNumber',kk87)
                    arrivalrate87=round(Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(3).AttValue('preARR')+  KalmanGain* (((Vissim.Net.Detectors.ItemByKey(15).AttValue ('VehicleNumber')/(proportion_of_CAVs*ittearrival))*3600)- Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(3).AttValue('preARR')))
                    Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(3).SetAttValue ('ArrivalRate',arrivalrate87)


                if Vissim.Net.Detectors.ItemByKey(16).AttValue ('vh')==1:
                    f63 = open("63.txt","r")                        
                    ggg63 = f63.readlines()
                    f63.close()
                    s63=[]
                    for x in ggg63:
                        if x not in s63:
                            s63.append(x)
                    kk63=len(s63)
                    Vissim.Net.Detectors.ItemByKey(16).SetAttValue ('VehicleNumber',kk63)
                    arrivalrate63=round(Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(4).AttValue('preARR')+  KalmanGain* (((Vissim.Net.Detectors.ItemByKey(16).AttValue ('VehicleNumber')/(proportion_of_CAVs*ittearrival))*3600)- Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(4).AttValue('preARR')))
                    Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(4).SetAttValue ('ArrivalRate',arrivalrate63)


                if Vissim.Net.Detectors.ItemByKey(16).AttValue ('vh')==0:
                    s63=[]                    
                    kk63=len(s63)
                    Vissim.Net.Detectors.ItemByKey(16).SetAttValue ('VehicleNumber',kk63)
                    arrivalrate63=round(Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(4).AttValue('preARR')+  KalmanGain* (((Vissim.Net.Detectors.ItemByKey(16).AttValue ('VehicleNumber')/(proportion_of_CAVs*ittearrival))*3600)- Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(4).AttValue('preARR')))
                    Vissim.Net.SignalControllers.ItemByKey(4).SGs.ItemByKey(4).SetAttValue ('ArrivalRate',arrivalrate63)


                if Vissim.Net.Detectors.ItemByKey(17).AttValue ('vh')==1:
                    f108 = open("108.txt","r")                        
                    ggg108 = f108.readlines()
                    f108.close()
                    s108=[]
                    for x in ggg108:
                        if x not in s108:
                            s108.append(x)
                    kk108=len(s108)
                    Vissim.Net.Detectors.ItemByKey(17).SetAttValue ('VehicleNumber',kk108)
                    arrivalrate108=round(Vissim.Net.SignalControllers.ItemByKey(5).SGs.ItemByKey(1).AttValue('preARR')+  KalmanGain* (((Vissim.Net.Detectors.ItemByKey(17).AttValue ('VehicleNumber')/(proportion_of_CAVs*ittearrival))*3600)- Vissim.Net.SignalControllers.ItemByKey(5).SGs.ItemByKey(1).AttValue('preARR')))
                    Vissim.Net.SignalControllers.ItemByKey(5).SGs.ItemByKey(1).SetAttValue ('ArrivalRate',arrivalrate108)


                if Vissim.Net.Detectors.ItemByKey(17).AttValue ('vh')==0:
                    s108=[]                    
                    kk108=len(s108)
                    Vissim.Net.Detectors.ItemByKey(17).SetAttValue ('VehicleNumber',kk108)
                    arrivalrate108=round(Vissim.Net.SignalControllers.ItemByKey(5).SGs.ItemByKey(1).AttValue('preARR')+  KalmanGain* (((Vissim.Net.Detectors.ItemByKey(17).AttValue ('VehicleNumber')/(proportion_of_CAVs*ittearrival))*3600)- Vissim.Net.SignalControllers.ItemByKey(5).SGs.ItemByKey(1).AttValue('preARR')))
                    Vissim.Net.SignalControllers.ItemByKey(5).SGs.ItemByKey(1).SetAttValue ('ArrivalRate',arrivalrate108)


                if Vissim.Net.Detectors.ItemByKey(18).AttValue ('vh')==1:
                    f103 = open("103.txt","r")                        
                    ggg103 = f103.readlines()
                    f103.close()
                    s103=[]
                    for x in ggg103:
                        if x not in s103:
                            s103.append(x)
                    kk103=len(s103)
                    Vissim.Net.Detectors.ItemByKey(18).SetAttValue ('VehicleNumber',kk103)
                    arrivalrate103=round(Vissim.Net.SignalControllers.ItemByKey(5).SGs.ItemByKey(2).AttValue('preARR')+  KalmanGain* (((Vissim.Net.Detectors.ItemByKey(18).AttValue ('VehicleNumber')/(proportion_of_CAVs*ittearrival))*3600)- Vissim.Net.SignalControllers.ItemByKey(5).SGs.ItemByKey(2).AttValue('preARR')))
                    Vissim.Net.SignalControllers.ItemByKey(5).SGs.ItemByKey(2).SetAttValue ('ArrivalRate',arrivalrate103)


                if Vissim.Net.Detectors.ItemByKey(18).AttValue ('vh')==0:
                    s103=[]                    
                    kk103=len(s103)
                    Vissim.Net.Detectors.ItemByKey(18).SetAttValue ('VehicleNumber',kk103)
                    arrivalrate103=round(Vissim.Net.SignalControllers.ItemByKey(5).SGs.ItemByKey(2).AttValue('preARR')+  KalmanGain* (((Vissim.Net.Detectors.ItemByKey(18).AttValue ('VehicleNumber')/(proportion_of_CAVs*ittearrival))*3600)- Vissim.Net.SignalControllers.ItemByKey(5).SGs.ItemByKey(2).AttValue('preARR')))
                    Vissim.Net.SignalControllers.ItemByKey(5).SGs.ItemByKey(2).SetAttValue ('ArrivalRate',arrivalrate103)



                if Vissim.Net.Detectors.ItemByKey(19).AttValue ('vh')==1:
                    f88 = open("88.txt","r")                        
                    ggg88 = f88.readlines()
                    f88.close()
                    s88=[]
                    for x in ggg88:
                        if x not in s88:
                            s88.append(x)
                    kk88=len(s88)
                    Vissim.Net.Detectors.ItemByKey(19).SetAttValue ('VehicleNumber',kk88)
                    arrivalrate88=round(Vissim.Net.SignalControllers.ItemByKey(5).SGs.ItemByKey(3).AttValue('preARR')+  KalmanGain* (((Vissim.Net.Detectors.ItemByKey(19).AttValue ('VehicleNumber')/(proportion_of_CAVs*ittearrival))*3600)- Vissim.Net.SignalControllers.ItemByKey(5).SGs.ItemByKey(3).AttValue('preARR')))
                    Vissim.Net.SignalControllers.ItemByKey(5).SGs.ItemByKey(3).SetAttValue ('ArrivalRate',arrivalrate88)


                if Vissim.Net.Detectors.ItemByKey(19).AttValue ('vh')==0:
                    s88=[]                    
                    kk88=len(s88)
                    Vissim.Net.Detectors.ItemByKey(19).SetAttValue ('VehicleNumber',kk88)
                    arrivalrate88=round(Vissim.Net.SignalControllers.ItemByKey(5).SGs.ItemByKey(3).AttValue('preARR')+  KalmanGain* (((Vissim.Net.Detectors.ItemByKey(19).AttValue ('VehicleNumber')/(proportion_of_CAVs*ittearrival))*3600)- Vissim.Net.SignalControllers.ItemByKey(5).SGs.ItemByKey(3).AttValue('preARR')))
                    Vissim.Net.SignalControllers.ItemByKey(5).SGs.ItemByKey(3).SetAttValue ('ArrivalRate',arrivalrate88)


                if Vissim.Net.Detectors.ItemByKey(20).AttValue ('vh')==1:
                    f98 = open("98.txt","r")                        
                    ggg98 = f98.readlines()
                    f98.close()
                    s98=[]
                    for x in ggg98:
                        if x not in s98:
                            s98.append(x)
                    kk98=len(s98)
                    Vissim.Net.Detectors.ItemByKey(20).SetAttValue ('VehicleNumber',kk98)
                    arrivalrate98=round(Vissim.Net.SignalControllers.ItemByKey(5).SGs.ItemByKey(4).AttValue('preARR')+  KalmanGain* (((Vissim.Net.Detectors.ItemByKey(20).AttValue ('VehicleNumber')/(proportion_of_CAVs*ittearrival))*3600)- Vissim.Net.SignalControllers.ItemByKey(5).SGs.ItemByKey(4).AttValue('preARR')))
                    Vissim.Net.SignalControllers.ItemByKey(5).SGs.ItemByKey(4).SetAttValue ('ArrivalRate',arrivalrate98)


                if Vissim.Net.Detectors.ItemByKey(20).AttValue ('vh')==0:
                    s98=[]                    
                    kk98=len(s98)
                    Vissim.Net.Detectors.ItemByKey(20).SetAttValue ('VehicleNumber',kk98)
                    arrivalrate98=round(Vissim.Net.SignalControllers.ItemByKey(5).SGs.ItemByKey(4).AttValue('preARR')+  KalmanGain* (((Vissim.Net.Detectors.ItemByKey(20).AttValue ('VehicleNumber')/(proportion_of_CAVs*ittearrival))*3600)- Vissim.Net.SignalControllers.ItemByKey(5).SGs.ItemByKey(4).AttValue('preARR')))
                    Vissim.Net.SignalControllers.ItemByKey(5).SGs.ItemByKey(4).SetAttValue ('ArrivalRate',arrivalrate98)




                if Vissim.Net.Detectors.ItemByKey(21).AttValue ('vh')==1:
                    f92 = open("92.txt","r")                        
                    ggg92 = f92.readlines()
                    f92.close()
                    s92=[]
                    for x in ggg92:
                        if x not in s92:
                            s92.append(x)
                    kk92=len(s92)
                    Vissim.Net.Detectors.ItemByKey(21).SetAttValue ('VehicleNumber',kk92)
                    arrivalrate92=round(Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(1).AttValue('preARR')+  KalmanGain* (((Vissim.Net.Detectors.ItemByKey(21).AttValue ('VehicleNumber')/(proportion_of_CAVs*ittearrival))*3600)- Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(1).AttValue('preARR')))
                    Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(1).SetAttValue ('ArrivalRate',arrivalrate92)


                if Vissim.Net.Detectors.ItemByKey(21).AttValue ('vh')==0:
                    s92=[]                    
                    kk92=len(s92)
                    Vissim.Net.Detectors.ItemByKey(21).SetAttValue ('VehicleNumber',kk92)
                    arrivalrate92=round(Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(1).AttValue('preARR')+  KalmanGain* (((Vissim.Net.Detectors.ItemByKey(21).AttValue ('VehicleNumber')/(proportion_of_CAVs*ittearrival))*3600)- Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(1).AttValue('preARR')))
                    Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(1).SetAttValue ('ArrivalRate',arrivalrate92)


                if Vissim.Net.Detectors.ItemByKey(22).AttValue ('vh')==1:
                    f60 = open("60.txt","r")                        
                    ggg60 = f60.readlines()
                    f60.close()
                    s60=[]
                    for x in ggg60:
                        if x not in s60:
                            s60.append(x)
                    kk60=len(s60)
                    Vissim.Net.Detectors.ItemByKey(22).SetAttValue ('VehicleNumber',kk60)
                    arrivalrate60=round(Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(2).AttValue('preARR')+  KalmanGain* (((Vissim.Net.Detectors.ItemByKey(22).AttValue ('VehicleNumber')/(proportion_of_CAVs*ittearrival))*3600)- Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(2).AttValue('preARR')))
                    Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(2).SetAttValue ('ArrivalRate',arrivalrate60)


                if Vissim.Net.Detectors.ItemByKey(22).AttValue ('vh')==0:
                    s60=[]                    
                    kk60=len(s60)
                    Vissim.Net.Detectors.ItemByKey(22).SetAttValue ('VehicleNumber',kk60)
                    arrivalrate60=round(Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(2).AttValue('preARR')+  KalmanGain* (((Vissim.Net.Detectors.ItemByKey(22).AttValue ('VehicleNumber')/(proportion_of_CAVs*ittearrival))*3600)- Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(2).AttValue('preARR')))
                    Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(2).SetAttValue ('ArrivalRate',arrivalrate60)



                if Vissim.Net.Detectors.ItemByKey(23).AttValue ('vh')==1:
                    f71 = open("71.txt","r")                        
                    ggg71 = f71.readlines()
                    f71.close()
                    s71=[]
                    for x in ggg71:
                        if x not in s71:
                            s71.append(x)
                    kk71=len(s71)
                    Vissim.Net.Detectors.ItemByKey(23).SetAttValue ('VehicleNumber',kk71)
                    arrivalrate71=round(Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(3).AttValue('preARR')+  KalmanGain* (((Vissim.Net.Detectors.ItemByKey(23).AttValue ('VehicleNumber')/(proportion_of_CAVs*ittearrival))*3600)- Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(3).AttValue('preARR')))
                    Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(3).SetAttValue ('ArrivalRate',arrivalrate71)


                if Vissim.Net.Detectors.ItemByKey(23).AttValue ('vh')==0:
                    s71=[]                    
                    kk71=len(s71)
                    Vissim.Net.Detectors.ItemByKey(23).SetAttValue ('VehicleNumber',kk71)
                    arrivalrate71=round(Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(3).AttValue('preARR')+  KalmanGain* (((Vissim.Net.Detectors.ItemByKey(23).AttValue ('VehicleNumber')/(proportion_of_CAVs*ittearrival))*3600)- Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(3).AttValue('preARR')))
                    Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(3).SetAttValue ('ArrivalRate',arrivalrate71)



                if Vissim.Net.Detectors.ItemByKey(24).AttValue ('vh')==1:
                    f93 = open("93.txt","r")                        
                    ggg93 = f93.readlines()
                    f93.close()
                    s93=[]
                    for x in ggg93:
                        if x not in s93:
                            s93.append(x)
                    kk93=len(s93)
                    Vissim.Net.Detectors.ItemByKey(24).SetAttValue ('VehicleNumber',kk93)
                    arrivalrate93=round(Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(4).AttValue('preARR')+  KalmanGain* (((Vissim.Net.Detectors.ItemByKey(24).AttValue ('VehicleNumber')/(proportion_of_CAVs*ittearrival))*3600)- Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(4).AttValue('preARR')))
                    Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(4).SetAttValue ('ArrivalRate',arrivalrate93)


                if Vissim.Net.Detectors.ItemByKey(24).AttValue ('vh')==0:
                    s93=[]                    
                    kk93=len(s93)
                    Vissim.Net.Detectors.ItemByKey(24).SetAttValue ('VehicleNumber',kk93)
                    arrivalrate93=round(Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(4).AttValue('preARR')+  KalmanGain* (((Vissim.Net.Detectors.ItemByKey(24).AttValue ('VehicleNumber')/(proportion_of_CAVs*ittearrival))*3600)- Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(4).AttValue('preARR')))
                    Vissim.Net.SignalControllers.ItemByKey(6).SGs.ItemByKey(4).SetAttValue ('ArrivalRate',arrivalrate93)



                if Vissim.Net.Detectors.ItemByKey(25).AttValue ('vh')==1:
                    f72 = open("72.txt","r")                        
                    ggg72 = f72.readlines()
                    f72.close()
                    s72=[]
                    for x in ggg72:
                        if x not in s72:
                            s72.append(x)
                    kk72=len(s72)
                    Vissim.Net.Detectors.ItemByKey(25).SetAttValue ('VehicleNumber',kk72)
                    arrivalrate72=round(Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(1).AttValue('preARR')+  KalmanGain* (((Vissim.Net.Detectors.ItemByKey(25).AttValue ('VehicleNumber')/(proportion_of_CAVs*ittearrival))*3600)- Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(1).AttValue('preARR')))
                    Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(1).SetAttValue ('ArrivalRate',arrivalrate72)


                if Vissim.Net.Detectors.ItemByKey(25).AttValue ('vh')==0:
                    s72=[]                    
                    kk72=len(s72)
                    Vissim.Net.Detectors.ItemByKey(25).SetAttValue ('VehicleNumber',kk72)
                    arrivalrate72=round(Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(1).AttValue('preARR')+  KalmanGain* (((Vissim.Net.Detectors.ItemByKey(25).AttValue ('VehicleNumber')/(proportion_of_CAVs*ittearrival))*3600)- Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(1).AttValue('preARR')))
                    Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(1).SetAttValue ('ArrivalRate',arrivalrate72)



                if Vissim.Net.Detectors.ItemByKey(26).AttValue ('vh')==1:
                    f62 = open("62.txt","r")                        
                    ggg62 = f62.readlines()
                    f62.close()
                    s62=[]
                    for x in ggg62:
                        if x not in s62:
                            s62.append(x)
                    kk62=len(s62)
                    Vissim.Net.Detectors.ItemByKey(26).SetAttValue ('VehicleNumber',kk62)
                    arrivalrate62=round(Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(2).AttValue('preARR')+  KalmanGain* (((Vissim.Net.Detectors.ItemByKey(26).AttValue ('VehicleNumber')/(proportion_of_CAVs*ittearrival))*3600)- Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(2).AttValue('preARR')))
                    Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(2).SetAttValue ('ArrivalRate',arrivalrate62)


                if Vissim.Net.Detectors.ItemByKey(26).AttValue ('vh')==0:
                    s62=[]                    
                    kk62=len(s62)
                    Vissim.Net.Detectors.ItemByKey(26).SetAttValue ('VehicleNumber',kk62)
                    arrivalrate62=round(Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(2).AttValue('preARR')+  KalmanGain* (((Vissim.Net.Detectors.ItemByKey(26).AttValue ('VehicleNumber')/(proportion_of_CAVs*ittearrival))*3600)- Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(2).AttValue('preARR')))
                    Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(2).SetAttValue ('ArrivalRate',arrivalrate62)






                if Vissim.Net.Detectors.ItemByKey(27).AttValue ('vh')==1:
                    f73 = open("73.txt","r")                        
                    ggg73 = f73.readlines()
                    f73.close()
                    s73=[]
                    for x in ggg73:
                        if x not in s73:
                            s73.append(x)
                    kk73=len(s73)
                    Vissim.Net.Detectors.ItemByKey(27).SetAttValue ('VehicleNumber',kk73)
                    arrivalrate73=round(Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(3).AttValue('preARR')+  KalmanGain* (((Vissim.Net.Detectors.ItemByKey(27).AttValue ('VehicleNumber')/(proportion_of_CAVs*ittearrival))*3600)- Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(3).AttValue('preARR')))
                    Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(3).SetAttValue ('ArrivalRate',arrivalrate73)


                if Vissim.Net.Detectors.ItemByKey(27).AttValue ('vh')==0:
                    s73=[]                    
                    kk73=len(s73)
                    Vissim.Net.Detectors.ItemByKey(27).SetAttValue ('VehicleNumber',kk73)
                    arrivalrate73=round(Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(3).AttValue('preARR')+  KalmanGain* (((Vissim.Net.Detectors.ItemByKey(27).AttValue ('VehicleNumber')/(proportion_of_CAVs*ittearrival))*3600)- Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(3).AttValue('preARR')))
                    Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(3).SetAttValue ('ArrivalRate',arrivalrate73)



                if Vissim.Net.Detectors.ItemByKey(28).AttValue ('vh')==1:
                    f83 = open("83.txt","r")                        
                    ggg83 = f83.readlines()
                    f83.close()
                    s83=[]
                    for x in ggg83:
                        if x not in s83:
                            s83.append(x)
                    kk83=len(s83)
                    Vissim.Net.Detectors.ItemByKey(28).SetAttValue ('VehicleNumber',kk83)
                    arrivalrate83=round(Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(4).AttValue('preARR')+  KalmanGain* (((Vissim.Net.Detectors.ItemByKey(28).AttValue ('VehicleNumber')/(proportion_of_CAVs*ittearrival))*3600)- Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(4).AttValue('preARR')))
                    Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(4).SetAttValue ('ArrivalRate',arrivalrate83)


                if Vissim.Net.Detectors.ItemByKey(28).AttValue ('vh')==0:
                    s83=[]                    
                    kk83=len(s83)
                    Vissim.Net.Detectors.ItemByKey(28).SetAttValue ('VehicleNumber',kk83)
                    arrivalrate83=round(Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(4).AttValue('preARR')+  KalmanGain* (((Vissim.Net.Detectors.ItemByKey(28).AttValue ('VehicleNumber')/(proportion_of_CAVs*ittearrival))*3600)- Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(4).AttValue('preARR')))
                    Vissim.Net.SignalControllers.ItemByKey(7).SGs.ItemByKey(4).SetAttValue ('ArrivalRate',arrivalrate83)





                if Vissim.Net.Detectors.ItemByKey(29).AttValue ('vh')==1:
                    f74 = open("74.txt","r")                        
                    ggg74 = f74.readlines()
                    f74.close()
                    s74=[]
                    for x in ggg74:
                        if x not in s74:
                            s74.append(x)
                    kk74=len(s74)
                    Vissim.Net.Detectors.ItemByKey(29).SetAttValue ('VehicleNumber',kk74)
                    arrivalrate74=round(Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(1).AttValue('preARR')+  KalmanGain* (((Vissim.Net.Detectors.ItemByKey(29).AttValue ('VehicleNumber')/(proportion_of_CAVs*ittearrival))*3600)- Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(1).AttValue('preARR')))
                    Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(1).SetAttValue ('ArrivalRate',arrivalrate74)


                if Vissim.Net.Detectors.ItemByKey(29).AttValue ('vh')==0:
                    s74=[]                    
                    kk74=len(s74)
                    Vissim.Net.Detectors.ItemByKey(29).SetAttValue ('VehicleNumber',kk74)
                    arrivalrate74=round(Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(1).AttValue('preARR')+  KalmanGain* (((Vissim.Net.Detectors.ItemByKey(29).AttValue ('VehicleNumber')/(proportion_of_CAVs*ittearrival))*3600)- Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(1).AttValue('preARR')))
                    Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(1).SetAttValue ('ArrivalRate',arrivalrate74)





                if Vissim.Net.Detectors.ItemByKey(30).AttValue ('vh')==1:
                    f64 = open("64.txt","r")                        
                    ggg64 = f64.readlines()
                    f64.close()
                    s64=[]
                    for x in ggg64:
                        if x not in s64:
                            s64.append(x)
                    kk64=len(s64)
                    Vissim.Net.Detectors.ItemByKey(30).SetAttValue ('VehicleNumber',kk64)
                    arrivalrate64=round(Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(2).AttValue('preARR')+  KalmanGain* (((Vissim.Net.Detectors.ItemByKey(30).AttValue ('VehicleNumber')/(proportion_of_CAVs*ittearrival))*3600)- Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(2).AttValue('preARR')))
                    Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(2).SetAttValue ('ArrivalRate',arrivalrate64)


                if Vissim.Net.Detectors.ItemByKey(30).AttValue ('vh')==0:
                    s64=[]                    
                    kk64=len(s64)
                    Vissim.Net.Detectors.ItemByKey(30).SetAttValue ('VehicleNumber',kk64)
                    arrivalrate64=round(Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(2).AttValue('preARR')+  KalmanGain* (((Vissim.Net.Detectors.ItemByKey(30).AttValue ('VehicleNumber')/(proportion_of_CAVs*ittearrival))*3600)- Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(2).AttValue('preARR')))
                    Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(2).SetAttValue ('ArrivalRate',arrivalrate64)



                if Vissim.Net.Detectors.ItemByKey(31).AttValue ('vh')==1:
                    f104 = open("104.txt","r")                        
                    ggg104 = f104.readlines()
                    f104.close()
                    s104=[]
                    for x in ggg104:
                        if x not in s104:
                            s104.append(x)
                    kk104=len(s104)
                    Vissim.Net.Detectors.ItemByKey(31).SetAttValue ('VehicleNumber',kk104)
                    arrivalrate104=round(Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(3).AttValue('preARR')+  KalmanGain* (((Vissim.Net.Detectors.ItemByKey(31).AttValue ('VehicleNumber')/(proportion_of_CAVs*ittearrival))*3600)- Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(3).AttValue('preARR')))
                    Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(3).SetAttValue ('ArrivalRate',arrivalrate104)


                if Vissim.Net.Detectors.ItemByKey(31).AttValue ('vh')==0:
                    s104=[]                    
                    kk104=len(s104)
                    Vissim.Net.Detectors.ItemByKey(31).SetAttValue ('VehicleNumber',kk104)
                    arrivalrate104=round(Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(3).AttValue('preARR')+  KalmanGain* (((Vissim.Net.Detectors.ItemByKey(31).AttValue ('VehicleNumber')/(proportion_of_CAVs*ittearrival))*3600)- Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(3).AttValue('preARR')))
                    Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(3).SetAttValue ('ArrivalRate',arrivalrate104)



                if Vissim.Net.Detectors.ItemByKey(32).AttValue ('vh')==1:
                    f105 = open("105.txt","r")                        
                    ggg105 = f105.readlines()
                    f105.close()
                    s105=[]
                    for x in ggg105:
                        if x not in s105:
                            s105.append(x)
                    kk105=len(s105)
                    Vissim.Net.Detectors.ItemByKey(32).SetAttValue ('VehicleNumber',kk105)
                    arrivalrate105=round(Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(4).AttValue('preARR')+  KalmanGain* (((Vissim.Net.Detectors.ItemByKey(32).AttValue ('VehicleNumber')/(proportion_of_CAVs*ittearrival))*3600)- Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(4).AttValue('preARR')))
                    Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(4).SetAttValue ('ArrivalRate',arrivalrate105)


                if Vissim.Net.Detectors.ItemByKey(32).AttValue ('vh')==0:
                    s105=[]                    
                    kk105=len(s105)
                    Vissim.Net.Detectors.ItemByKey(32).SetAttValue ('VehicleNumber',kk105)
                    arrivalrate105=round(Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(4).AttValue('preARR')+  KalmanGain* (((Vissim.Net.Detectors.ItemByKey(32).AttValue ('VehicleNumber')/(proportion_of_CAVs*ittearrival))*3600)- Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(4).AttValue('preARR')))
                    Vissim.Net.SignalControllers.ItemByKey(8).SGs.ItemByKey(4).SetAttValue ('ArrivalRate',arrivalrate105)





                if Vissim.Net.Detectors.ItemByKey(33).AttValue ('vh')==1:
                    f99 = open("99.txt","r")                        
                    ggg99 = f99.readlines()
                    f99.close()
                    s99=[]
                    for x in ggg99:
                        if x not in s99:
                            s99.append(x)
                    kk99=len(s99)
                    Vissim.Net.Detectors.ItemByKey(33).SetAttValue ('VehicleNumber',kk99)
                    arrivalrate99=round(Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(1).AttValue('preARR')+  KalmanGain* (((Vissim.Net.Detectors.ItemByKey(33).AttValue ('VehicleNumber')/(proportion_of_CAVs*ittearrival))*3600)- Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(1).AttValue('preARR')))
                    Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(1).SetAttValue ('ArrivalRate',arrivalrate99)


                if Vissim.Net.Detectors.ItemByKey(33).AttValue ('vh')==0:
                    s99=[]                    
                    kk99=len(s99)
                    Vissim.Net.Detectors.ItemByKey(33).SetAttValue ('VehicleNumber',kk99)
                    arrivalrate99=round(Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(1).AttValue('preARR')+  KalmanGain* (((Vissim.Net.Detectors.ItemByKey(33).AttValue ('VehicleNumber')/(proportion_of_CAVs*ittearrival))*3600)- Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(1).AttValue('preARR')))
                    Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(1).SetAttValue ('ArrivalRate',arrivalrate99)






                if Vissim.Net.Detectors.ItemByKey(34).AttValue ('vh')==1:
                    f75 = open("75.txt","r")                        
                    ggg75 = f75.readlines()
                    f75.close()
                    s75=[]
                    for x in ggg75:
                        if x not in s75:
                            s75.append(x)
                    kk75=len(s75)
                    Vissim.Net.Detectors.ItemByKey(34).SetAttValue ('VehicleNumber',kk75)
                    arrivalrate75=round(Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(2).AttValue('preARR')+  KalmanGain* (((Vissim.Net.Detectors.ItemByKey(34).AttValue ('VehicleNumber')/(proportion_of_CAVs*ittearrival))*3600)- Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(2).AttValue('preARR')))
                    Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(2).SetAttValue ('ArrivalRate',arrivalrate75)


                if Vissim.Net.Detectors.ItemByKey(34).AttValue ('vh')==0:
                    s75=[]                    
                    kk75=len(s75)
                    Vissim.Net.Detectors.ItemByKey(34).SetAttValue ('VehicleNumber',kk75)
                    arrivalrate75=round(Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(2).AttValue('preARR')+  KalmanGain* (((Vissim.Net.Detectors.ItemByKey(34).AttValue ('VehicleNumber')/(proportion_of_CAVs*ittearrival))*3600)- Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(2).AttValue('preARR')))
                    Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(2).SetAttValue ('ArrivalRate',arrivalrate75)









                if Vissim.Net.Detectors.ItemByKey(35).AttValue ('vh')==1:
                    f65 = open("65.txt","r")                        
                    ggg65 = f65.readlines()
                    f65.close()
                    s65=[]
                    for x in ggg65:
                        if x not in s65:
                            s65.append(x)
                    kk65=len(s65)
                    Vissim.Net.Detectors.ItemByKey(35).SetAttValue ('VehicleNumber',kk65)
                    arrivalrate65=round(Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(3).AttValue('preARR')+  KalmanGain* (((Vissim.Net.Detectors.ItemByKey(35).AttValue ('VehicleNumber')/(proportion_of_CAVs*ittearrival))*3600)- Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(3).AttValue('preARR')))
                    Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(3).SetAttValue ('ArrivalRate',arrivalrate65)


                if Vissim.Net.Detectors.ItemByKey(35).AttValue ('vh')==0:
                    s65=[]                    
                    kk65=len(s65)
                    Vissim.Net.Detectors.ItemByKey(35).SetAttValue ('VehicleNumber',kk65)
                    arrivalrate65=round(Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(3).AttValue('preARR')+  KalmanGain* (((Vissim.Net.Detectors.ItemByKey(35).AttValue ('VehicleNumber')/(proportion_of_CAVs*ittearrival))*3600)- Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(3).AttValue('preARR')))
                    Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(3).SetAttValue ('ArrivalRate',arrivalrate65)






                if Vissim.Net.Detectors.ItemByKey(36).AttValue ('vh')==1:
                    f102 = open("102.txt","r")                        
                    ggg102 = f102.readlines()
                    f102.close()
                    s102=[]
                    for x in ggg102:
                        if x not in s102:
                            s102.append(x)
                    kk102=len(s102)
                    Vissim.Net.Detectors.ItemByKey(36).SetAttValue ('VehicleNumber',kk102)
                    arrivalrate102=round(Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(2).AttValue('preARR')+  KalmanGain* (((Vissim.Net.Detectors.ItemByKey(36).AttValue ('VehicleNumber')/(proportion_of_CAVs*ittearrival))*3600)- Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(2).AttValue('preARR')))
                    Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(2).SetAttValue ('ArrivalRate',arrivalrate102)


                if Vissim.Net.Detectors.ItemByKey(36).AttValue ('vh')==0:
                    s102=[]                    
                    kk102=len(s102)
                    Vissim.Net.Detectors.ItemByKey(36).SetAttValue ('VehicleNumber',kk102)
                    arrivalrate102=round(Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(2).AttValue('preARR')+  KalmanGain* (((Vissim.Net.Detectors.ItemByKey(36).AttValue ('VehicleNumber')/(proportion_of_CAVs*ittearrival))*3600)- Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(2).AttValue('preARR')))
                    Vissim.Net.SignalControllers.ItemByKey(9).SGs.ItemByKey(2).SetAttValue ('ArrivalRate',arrivalrate102)





                if Vissim.Net.Detectors.ItemByKey(37).AttValue ('vh')==1:
                    f76 = open("76.txt","r")                        
                    ggg76 = f76.readlines()
                    f76.close()
                    s76=[]
                    for x in ggg76:
                        if x not in s76:
                            s76.append(x)
                    kk76=len(s76)
                    Vissim.Net.Detectors.ItemByKey(37).SetAttValue ('VehicleNumber',kk76)
                    arrivalrate76=round(Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(1).AttValue('preARR')+  KalmanGain* (((Vissim.Net.Detectors.ItemByKey(37).AttValue ('VehicleNumber')/(proportion_of_CAVs*ittearrival))*3600)- Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(1).AttValue('preARR')))
                    Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(1).SetAttValue ('ArrivalRate',arrivalrate76)


                if Vissim.Net.Detectors.ItemByKey(37).AttValue ('vh')==0:
                    s76=[]                    
                    kk76=len(s76)
                    Vissim.Net.Detectors.ItemByKey(37).SetAttValue ('VehicleNumber',kk76)
                    arrivalrate76=round(Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(1).AttValue('preARR')+  KalmanGain* (((Vissim.Net.Detectors.ItemByKey(37).AttValue ('VehicleNumber')/(proportion_of_CAVs*ittearrival))*3600)- Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(1).AttValue('preARR')))
                    Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(1).SetAttValue ('ArrivalRate',arrivalrate76)


                if Vissim.Net.Detectors.ItemByKey(38).AttValue ('vh')==1:
                    f77 = open("77.txt","r")                        
                    ggg77 = f77.readlines()
                    f77.close()
                    s77=[]
                    for x in ggg77:
                        if x not in s77:
                            s77.append(x)
                    kk77=len(s77)
                    Vissim.Net.Detectors.ItemByKey(38).SetAttValue ('VehicleNumber',kk77)
                    arrivalrate77=round(Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(2).AttValue('preARR')+  KalmanGain* (((Vissim.Net.Detectors.ItemByKey(38).AttValue ('VehicleNumber')/(proportion_of_CAVs*ittearrival))*3600)- Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(2).AttValue('preARR')))
                    Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(2).SetAttValue ('ArrivalRate',arrivalrate77)


                if Vissim.Net.Detectors.ItemByKey(38).AttValue ('vh')==0:
                    s77=[]                    
                    kk77=len(s77)
                    Vissim.Net.Detectors.ItemByKey(38).SetAttValue ('VehicleNumber',kk77)
                    arrivalrate77=round(Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(2).AttValue('preARR')+  KalmanGain* (((Vissim.Net.Detectors.ItemByKey(38).AttValue ('VehicleNumber')/(proportion_of_CAVs*ittearrival))*3600)- Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(2).AttValue('preARR')))
                    Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(2).SetAttValue ('ArrivalRate',arrivalrate77)


                if Vissim.Net.Detectors.ItemByKey(39).AttValue ('vh')==1:
                    f67 = open("67.txt","r")                        
                    ggg67 = f67.readlines()
                    f67.close()
                    s67=[]
                    for x in ggg67:
                        if x not in s67:
                            s67.append(x)
                    kk67=len(s67)
                    Vissim.Net.Detectors.ItemByKey(39).SetAttValue ('VehicleNumber',kk67)
                    arrivalrate67=round(Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(3).AttValue('preARR')+  KalmanGain* (((Vissim.Net.Detectors.ItemByKey(39).AttValue ('VehicleNumber')/(proportion_of_CAVs*ittearrival))*3600)- Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(3).AttValue('preARR')))
                    Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(3).SetAttValue ('ArrivalRate',arrivalrate67)


                if Vissim.Net.Detectors.ItemByKey(39).AttValue ('vh')==0:
                    s67=[]                    
                    kk67=len(s67)
                    Vissim.Net.Detectors.ItemByKey(39).SetAttValue ('VehicleNumber',kk67)
                    arrivalrate67=round(Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(3).AttValue('preARR')+  KalmanGain* (((Vissim.Net.Detectors.ItemByKey(39).AttValue ('VehicleNumber')/(proportion_of_CAVs*ittearrival))*3600)- Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(3).AttValue('preARR')))
                    Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(3).SetAttValue ('ArrivalRate',arrivalrate67)





                if Vissim.Net.Detectors.ItemByKey(40).AttValue ('vh')==1:
                    f86 = open("86.txt","r")                        
                    ggg86 = f86.readlines()
                    f86.close()
                    s86=[]
                    for x in ggg86:
                        if x not in s86:
                            s86.append(x)
                    kk86=len(s86)
                    Vissim.Net.Detectors.ItemByKey(40).SetAttValue ('VehicleNumber',kk86)
                    arrivalrate86=round(Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(4).AttValue('preARR')+  KalmanGain* (((Vissim.Net.Detectors.ItemByKey(40).AttValue ('VehicleNumber')/(proportion_of_CAVs*ittearrival))*3600)- Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(4).AttValue('preARR')))
                    Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(4).SetAttValue ('ArrivalRate',arrivalrate86)


                if Vissim.Net.Detectors.ItemByKey(40).AttValue ('vh')==0:
                    s86=[]                    
                    kk86=len(s86)
                    Vissim.Net.Detectors.ItemByKey(40).SetAttValue ('VehicleNumber',kk86)
                    arrivalrate86=round(Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(4).AttValue('preARR')+  KalmanGain* (((Vissim.Net.Detectors.ItemByKey(40).AttValue ('VehicleNumber')/(proportion_of_CAVs*ittearrival))*3600)- Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(4).AttValue('preARR')))
                    Vissim.Net.SignalControllers.ItemByKey(10).SGs.ItemByKey(4).SetAttValue ('ArrivalRate',arrivalrate86)






                if Vissim.Net.Detectors.ItemByKey(41).AttValue ('vh')==1:
                    f78 = open("78.txt","r")                        
                    ggg78 = f78.readlines()
                    f78.close()
                    s78=[]
                    for x in ggg78:
                        if x not in s78:
                            s78.append(x)
                    kk78=len(s78)
                    Vissim.Net.Detectors.ItemByKey(41).SetAttValue ('VehicleNumber',kk78)
                    arrivalrate78=round(Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(1).AttValue('preARR')+  KalmanGain* (((Vissim.Net.Detectors.ItemByKey(41).AttValue ('VehicleNumber')/(proportion_of_CAVs*ittearrival))*3600)- Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(1).AttValue('preARR')))
                    Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(1).SetAttValue ('ArrivalRate',arrivalrate78)


                if Vissim.Net.Detectors.ItemByKey(41).AttValue ('vh')==0:
                    s78=[]                    
                    kk78=len(s78)
                    Vissim.Net.Detectors.ItemByKey(41).SetAttValue ('VehicleNumber',kk78)
                    arrivalrate78=round(Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(1).AttValue('preARR')+  KalmanGain* (((Vissim.Net.Detectors.ItemByKey(41).AttValue ('VehicleNumber')/(proportion_of_CAVs*ittearrival))*3600)- Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(1).AttValue('preARR')))
                    Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(1).SetAttValue ('ArrivalRate',arrivalrate78)



                if Vissim.Net.Detectors.ItemByKey(42).AttValue ('vh')==1:
                    f97 = open("97.txt","r")                        
                    ggg97 = f97.readlines()
                    f97.close()
                    s97=[]
                    for x in ggg97:
                        if x not in s97:
                            s97.append(x)
                    kk97=len(s97)
                    Vissim.Net.Detectors.ItemByKey(42).SetAttValue ('VehicleNumber',kk97)
                    arrivalrate97=round(Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(2).AttValue('preARR')+  KalmanGain* (((Vissim.Net.Detectors.ItemByKey(42).AttValue ('VehicleNumber')/(proportion_of_CAVs*ittearrival))*3600)- Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(2).AttValue('preARR')))
                    Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(2).SetAttValue ('ArrivalRate',arrivalrate97)


                if Vissim.Net.Detectors.ItemByKey(42).AttValue ('vh')==0:
                    s97=[]                    
                    kk97=len(s97)
                    Vissim.Net.Detectors.ItemByKey(42).SetAttValue ('VehicleNumber',kk97)
                    arrivalrate97=round(Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(2).AttValue('preARR')+  KalmanGain* (((Vissim.Net.Detectors.ItemByKey(42).AttValue ('VehicleNumber')/(proportion_of_CAVs*ittearrival))*3600)- Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(2).AttValue('preARR')))
                    Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(2).SetAttValue ('ArrivalRate',arrivalrate97)




                if Vissim.Net.Detectors.ItemByKey(43).AttValue ('vh')==1:
                    f69 = open("69.txt","r")                        
                    ggg69 = f69.readlines()
                    f69.close()
                    s69=[]
                    for x in ggg69:
                        if x not in s69:
                            s69.append(x)
                    kk69=len(s69)
                    Vissim.Net.Detectors.ItemByKey(43).SetAttValue ('VehicleNumber',kk69)
                    arrivalrate69=round(Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(3).AttValue('preARR')+  KalmanGain* (((Vissim.Net.Detectors.ItemByKey(43).AttValue ('VehicleNumber')/(proportion_of_CAVs*ittearrival))*3600)- Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(3).AttValue('preARR')))
                    Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(3).SetAttValue ('ArrivalRate',arrivalrate69)


                if Vissim.Net.Detectors.ItemByKey(43).AttValue ('vh')==0:
                    s69=[]                    
                    kk69=len(s69)
                    Vissim.Net.Detectors.ItemByKey(43).SetAttValue ('VehicleNumber',kk69)
                    arrivalrate69=round(Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(3).AttValue('preARR')+  KalmanGain* (((Vissim.Net.Detectors.ItemByKey(43).AttValue ('VehicleNumber')/(proportion_of_CAVs*ittearrival))*3600)- Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(3).AttValue('preARR')))
                    Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(3).SetAttValue ('ArrivalRate',arrivalrate69)





                if Vissim.Net.Detectors.ItemByKey(44).AttValue ('vh')==1:
                    f96 = open("96.txt","r")                        
                    ggg96 = f96.readlines()
                    f96.close()
                    s96=[]
                    for x in ggg96:
                        if x not in s96:
                            s96.append(x)
                    kk96=len(s96)
                    Vissim.Net.Detectors.ItemByKey(44).SetAttValue ('VehicleNumber',kk96)
                    arrivalrate96=round(Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(4).AttValue('preARR')+  KalmanGain* (((Vissim.Net.Detectors.ItemByKey(44).AttValue ('VehicleNumber')/(proportion_of_CAVs*ittearrival))*3600)- Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(4).AttValue('preARR')))
                    Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(4).SetAttValue ('ArrivalRate',arrivalrate96)


                if Vissim.Net.Detectors.ItemByKey(44).AttValue ('vh')==0:
                    s96=[]                    
                    kk96=len(s96)
                    Vissim.Net.Detectors.ItemByKey(44).SetAttValue ('VehicleNumber',kk96)
                    arrivalrate96=round(Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(4).AttValue('preARR')+  KalmanGain* (((Vissim.Net.Detectors.ItemByKey(44).AttValue ('VehicleNumber')/(proportion_of_CAVs*ittearrival))*3600)- Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(4).AttValue('preARR')))
                    Vissim.Net.SignalControllers.ItemByKey(11).SGs.ItemByKey(4).SetAttValue ('ArrivalRate',arrivalrate96)




                if Vissim.Net.Detectors.ItemByKey(45).AttValue ('vh')==1:
                    f112 = open("112.txt","r")                        
                    ggg112 = f112.readlines()
                    f112.close()
                    s112=[]
                    for x in ggg112:
                        if x not in s112:
                            s112.append(x)
                    kk112=len(s112)
                    Vissim.Net.Detectors.ItemByKey(45).SetAttValue ('VehicleNumber',kk112)
                    arrivalrate112=round(Vissim.Net.SignalControllers.ItemByKey(12).SGs.ItemByKey(1).AttValue('preARR')+  KalmanGain* (((Vissim.Net.Detectors.ItemByKey(45).AttValue ('VehicleNumber')/(proportion_of_CAVs*ittearrival))*3600)- Vissim.Net.SignalControllers.ItemByKey(12).SGs.ItemByKey(1).AttValue('preARR')))
                    Vissim.Net.SignalControllers.ItemByKey(12).SGs.ItemByKey(1).SetAttValue ('ArrivalRate',arrivalrate112)


                if Vissim.Net.Detectors.ItemByKey(45).AttValue ('vh')==0:
                    s112=[]                    
                    kk112=len(s112)
                    Vissim.Net.Detectors.ItemByKey(45).SetAttValue ('VehicleNumber',kk112)
                    arrivalrate112=round(Vissim.Net.SignalControllers.ItemByKey(12).SGs.ItemByKey(1).AttValue('preARR')+  KalmanGain* (((Vissim.Net.Detectors.ItemByKey(45).AttValue ('VehicleNumber')/(proportion_of_CAVs*ittearrival))*3600)- Vissim.Net.SignalControllers.ItemByKey(12).SGs.ItemByKey(1).AttValue('preARR')))
                    Vissim.Net.SignalControllers.ItemByKey(12).SGs.ItemByKey(1).SetAttValue ('ArrivalRate',arrivalrate112)


                if Vissim.Net.Detectors.ItemByKey(46).AttValue ('vh')==1:
                    f95 = open("95.txt","r")                        
                    ggg95 = f95.readlines()
                    f95.close()
                    s95=[]
                    for x in ggg95:
                        if x not in s95:
                            s95.append(x)
                    kk95=len(s95)
                    Vissim.Net.Detectors.ItemByKey(46).SetAttValue ('VehicleNumber',kk95)
                    arrivalrate95=round(Vissim.Net.SignalControllers.ItemByKey(12).SGs.ItemByKey(2).AttValue('preARR')+  KalmanGain* (((Vissim.Net.Detectors.ItemByKey(46).AttValue ('VehicleNumber')/(proportion_of_CAVs*ittearrival))*3600)- Vissim.Net.SignalControllers.ItemByKey(12).SGs.ItemByKey(2).AttValue('preARR')))
                    Vissim.Net.SignalControllers.ItemByKey(12).SGs.ItemByKey(2).SetAttValue ('ArrivalRate',arrivalrate95)


                if Vissim.Net.Detectors.ItemByKey(46).AttValue ('vh')==0:
                    s95=[]                    
                    kk95=len(s95)
                    Vissim.Net.Detectors.ItemByKey(46).SetAttValue ('VehicleNumber',kk95)
                    arrivalrate95=round(Vissim.Net.SignalControllers.ItemByKey(12).SGs.ItemByKey(2).AttValue('preARR')+  KalmanGain* (((Vissim.Net.Detectors.ItemByKey(46).AttValue ('VehicleNumber')/(proportion_of_CAVs*ittearrival))*3600)- Vissim.Net.SignalControllers.ItemByKey(12).SGs.ItemByKey(2).AttValue('preARR')))
                    Vissim.Net.SignalControllers.ItemByKey(12).SGs.ItemByKey(2).SetAttValue ('ArrivalRate',arrivalrate95)


                if Vissim.Net.Detectors.ItemByKey(47).AttValue ('vh')==1:
                    f85 = open("85.txt","r")                        
                    ggg85 = f85.readlines()
                    f85.close()
                    s85=[]
                    for x in ggg85:
                        if x not in s85:
                            s85.append(x)
                    kk85=len(s85)
                    Vissim.Net.Detectors.ItemByKey(47).SetAttValue ('VehicleNumber',kk85)
                    arrivalrate85=round(Vissim.Net.SignalControllers.ItemByKey(12).SGs.ItemByKey(3).AttValue('preARR')+  KalmanGain* (((Vissim.Net.Detectors.ItemByKey(47).AttValue ('VehicleNumber')/(proportion_of_CAVs*ittearrival))*3600)- Vissim.Net.SignalControllers.ItemByKey(12).SGs.ItemByKey(3).AttValue('preARR')))
                    Vissim.Net.SignalControllers.ItemByKey(12).SGs.ItemByKey(3).SetAttValue ('ArrivalRate',arrivalrate85)


                if Vissim.Net.Detectors.ItemByKey(47).AttValue ('vh')==0:
                    s85=[]                    
                    kk85=len(s85)
                    Vissim.Net.Detectors.ItemByKey(47).SetAttValue ('VehicleNumber',kk85)
                    arrivalrate85=round(Vissim.Net.SignalControllers.ItemByKey(12).SGs.ItemByKey(3).AttValue('preARR')+  KalmanGain* (((Vissim.Net.Detectors.ItemByKey(47).AttValue ('VehicleNumber')/(proportion_of_CAVs*ittearrival))*3600)- Vissim.Net.SignalControllers.ItemByKey(12).SGs.ItemByKey(3).AttValue('preARR')))
                    Vissim.Net.SignalControllers.ItemByKey(12).SGs.ItemByKey(3).SetAttValue ('ArrivalRate',arrivalrate85)


                if Vissim.Net.Detectors.ItemByKey(48).AttValue ('vh')==1:
                    f101 = open("101.txt","r")                        
                    ggg101 = f101.readlines()
                    f101.close()
                    s101=[]
                    for x in ggg101:
                        if x not in s101:
                            s101.append(x)
                    kk101=len(s101)
                    Vissim.Net.Detectors.ItemByKey(48).SetAttValue ('VehicleNumber',kk101)
                    arrivalrate101=round(Vissim.Net.SignalControllers.ItemByKey(12).SGs.ItemByKey(4).AttValue('preARR')+  KalmanGain* (((Vissim.Net.Detectors.ItemByKey(48).AttValue ('VehicleNumber')/(proportion_of_CAVs*ittearrival))*3600)- Vissim.Net.SignalControllers.ItemByKey(12).SGs.ItemByKey(4).AttValue('preARR')))
                    Vissim.Net.SignalControllers.ItemByKey(12).SGs.ItemByKey(4).SetAttValue ('ArrivalRate',arrivalrate101)


                if Vissim.Net.Detectors.ItemByKey(48).AttValue ('vh')==0:
                    s101=[]                    
                    kk101=len(s101)
                    Vissim.Net.Detectors.ItemByKey(48).SetAttValue ('VehicleNumber',kk101)
                    arrivalrate101=round(Vissim.Net.SignalControllers.ItemByKey(12).SGs.ItemByKey(4).AttValue('preARR')+  KalmanGain* (((Vissim.Net.Detectors.ItemByKey(48).AttValue ('VehicleNumber')/(proportion_of_CAVs*ittearrival))*3600)- Vissim.Net.SignalControllers.ItemByKey(12).SGs.ItemByKey(4).AttValue('preARR')))
                    Vissim.Net.SignalControllers.ItemByKey(12).SGs.ItemByKey(4).SetAttValue ('ArrivalRate',arrivalrate101)


                if Vissim.Net.Detectors.ItemByKey(49).AttValue ('vh')==1:
                    f113 = open("113.txt","r")                        
                    ggg113 = f113.readlines()
                    f113.close()
                    s113=[]
                    for x in ggg113:
                        if x not in s113:
                            s113.append(x)
                    kk113=len(s113)
                    Vissim.Net.Detectors.ItemByKey(49).SetAttValue ('VehicleNumber',kk113)
                    arrivalrate113=round(Vissim.Net.SignalControllers.ItemByKey(13).SGs.ItemByKey(1).AttValue('preARR')+  KalmanGain* (((Vissim.Net.Detectors.ItemByKey(49).AttValue ('VehicleNumber')/(proportion_of_CAVs*ittearrival))*3600)- Vissim.Net.SignalControllers.ItemByKey(13).SGs.ItemByKey(1).AttValue('preARR')))
                    Vissim.Net.SignalControllers.ItemByKey(13).SGs.ItemByKey(1).SetAttValue ('ArrivalRate',arrivalrate113)


                if Vissim.Net.Detectors.ItemByKey(49).AttValue ('vh')==0:
                    s113=[]                    
                    kk113=len(s113)
                    Vissim.Net.Detectors.ItemByKey(49).SetAttValue ('VehicleNumber',kk113)
                    arrivalrate113=round(Vissim.Net.SignalControllers.ItemByKey(13).SGs.ItemByKey(1).AttValue('preARR')+  KalmanGain* (((Vissim.Net.Detectors.ItemByKey(49).AttValue ('VehicleNumber')/(proportion_of_CAVs*ittearrival))*3600)- Vissim.Net.SignalControllers.ItemByKey(13).SGs.ItemByKey(1).AttValue('preARR')))
                    Vissim.Net.SignalControllers.ItemByKey(13).SGs.ItemByKey(1).SetAttValue ('ArrivalRate',arrivalrate113)



                if Vissim.Net.Detectors.ItemByKey(50).AttValue ('vh')==1:
                    f106 = open("106.txt","r")                        
                    ggg106 = f106.readlines()
                    f106.close()
                    s106=[]
                    for x in ggg106:
                        if x not in s106:
                            s106.append(x)
                    kk106=len(s106)
                    Vissim.Net.Detectors.ItemByKey(50).SetAttValue ('VehicleNumber',kk106)
                    arrivalrate106=round(Vissim.Net.SignalControllers.ItemByKey(13).SGs.ItemByKey(2).AttValue('preARR')+  KalmanGain* (((Vissim.Net.Detectors.ItemByKey(50).AttValue ('VehicleNumber')/(proportion_of_CAVs*ittearrival))*3600)- Vissim.Net.SignalControllers.ItemByKey(13).SGs.ItemByKey(2).AttValue('preARR')))
                    Vissim.Net.SignalControllers.ItemByKey(13).SGs.ItemByKey(2).SetAttValue ('ArrivalRate',arrivalrate106)


                if Vissim.Net.Detectors.ItemByKey(50).AttValue ('vh')==0:
                    s106=[]                    
                    kk106=len(s106)
                    Vissim.Net.Detectors.ItemByKey(50).SetAttValue ('VehicleNumber',kk106)
                    arrivalrate106=round(Vissim.Net.SignalControllers.ItemByKey(13).SGs.ItemByKey(2).AttValue('preARR')+  KalmanGain* (((Vissim.Net.Detectors.ItemByKey(50).AttValue ('VehicleNumber')/(proportion_of_CAVs*ittearrival))*3600)- Vissim.Net.SignalControllers.ItemByKey(13).SGs.ItemByKey(2).AttValue('preARR')))
                    Vissim.Net.SignalControllers.ItemByKey(13).SGs.ItemByKey(2).SetAttValue ('ArrivalRate',arrivalrate106)


                if Vissim.Net.Detectors.ItemByKey(51).AttValue ('vh')==1:
                    f84 = open("84.txt","r")                        
                    ggg84 = f84.readlines()
                    f84.close()
                    s84=[]
                    for x in ggg84:
                        if x not in s84:
                            s84.append(x)
                    kk84=len(s84)
                    Vissim.Net.Detectors.ItemByKey(51).SetAttValue ('VehicleNumber',kk84)
                    arrivalrate84=round(Vissim.Net.SignalControllers.ItemByKey(13).SGs.ItemByKey(3).AttValue('preARR')+  KalmanGain* (((Vissim.Net.Detectors.ItemByKey(51).AttValue ('VehicleNumber')/(proportion_of_CAVs*ittearrival))*3600)- Vissim.Net.SignalControllers.ItemByKey(13).SGs.ItemByKey(3).AttValue('preARR')))
                    Vissim.Net.SignalControllers.ItemByKey(13).SGs.ItemByKey(3).SetAttValue ('ArrivalRate',arrivalrate84)


                if Vissim.Net.Detectors.ItemByKey(51).AttValue ('vh')==0:
                    s84=[]                    
                    kk84=len(s84)
                    Vissim.Net.Detectors.ItemByKey(51).SetAttValue ('VehicleNumber',kk84)
                    arrivalrate84=round(Vissim.Net.SignalControllers.ItemByKey(13).SGs.ItemByKey(3).AttValue('preARR')+  KalmanGain* (((Vissim.Net.Detectors.ItemByKey(51).AttValue ('VehicleNumber')/(proportion_of_CAVs*ittearrival))*3600)- Vissim.Net.SignalControllers.ItemByKey(13).SGs.ItemByKey(3).AttValue('preARR')))
                    Vissim.Net.SignalControllers.ItemByKey(13).SGs.ItemByKey(3).SetAttValue ('ArrivalRate',arrivalrate84)


                if Vissim.Net.Detectors.ItemByKey(52).AttValue ('vh')==1:
                    f94 = open("94.txt","r")                        
                    ggg94 = f94.readlines()
                    f94.close()
                    s94=[]
                    for x in ggg94:
                        if x not in s94:
                            s94.append(x)
                    kk94=len(s94)
                    Vissim.Net.Detectors.ItemByKey(52).SetAttValue ('VehicleNumber',kk94)
                    arrivalrate94=round(Vissim.Net.SignalControllers.ItemByKey(13).SGs.ItemByKey(4).AttValue('preARR')+  KalmanGain* (((Vissim.Net.Detectors.ItemByKey(52).AttValue ('VehicleNumber')/(proportion_of_CAVs*ittearrival))*3600)- Vissim.Net.SignalControllers.ItemByKey(13).SGs.ItemByKey(4).AttValue('preARR')))
                    Vissim.Net.SignalControllers.ItemByKey(13).SGs.ItemByKey(4).SetAttValue ('ArrivalRate',arrivalrate94)


                if Vissim.Net.Detectors.ItemByKey(52).AttValue ('vh')==0:
                    s94=[]                    
                    kk94=len(s94)
                    Vissim.Net.Detectors.ItemByKey(52).SetAttValue ('VehicleNumber',kk94)
                    arrivalrate94=round(Vissim.Net.SignalControllers.ItemByKey(13).SGs.ItemByKey(4).AttValue('preARR')+  KalmanGain* (((Vissim.Net.Detectors.ItemByKey(52).AttValue ('VehicleNumber')/(proportion_of_CAVs*ittearrival))*3600)- Vissim.Net.SignalControllers.ItemByKey(13).SGs.ItemByKey(4).AttValue('preARR')))
                    Vissim.Net.SignalControllers.ItemByKey(13).SGs.ItemByKey(4).SetAttValue ('ArrivalRate',arrivalrate94)


































