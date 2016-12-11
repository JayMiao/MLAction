# -*- coding: utf-8 -*-
from numpy import *

def loadExData():
    return [[0, 0, 0, 2, 2],
            [0, 0, 0, 3, 3],
            [0, 0, 0, 1, 1],
            [1, 1, 1, 0, 0],
            [2, 2, 2, 0, 0],
            [5, 5, 5, 0, 0],
            [1, 1, 1, 0, 0]]


def loadExData2():
    return [[0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 5],
            [0, 0, 0, 3, 0, 4, 0, 0, 0, 0, 3],
            [0, 0, 0, 0, 4, 0, 0, 1, 0, 4, 0],
            [3, 3, 4, 0, 0, 0, 0, 2, 2, 0, 0],
            [5, 4, 5, 0, 0, 0, 0, 5, 5, 0, 0],
            [0, 0, 0, 0, 5, 0, 1, 0, 0, 5, 0],
            [4, 3, 4, 0, 0, 0, 0, 5, 5, 0, 1],
            [0, 0, 0, 4, 0, 4, 0, 0, 0, 0, 4],
            [0, 0, 0, 2, 0, 2, 5, 0, 0, 1, 2],
            [0, 0, 0, 0, 5, 0, 0, 0, 0, 4, 0],
            [1, 0, 0, 0, 0, 0, 0, 1, 2, 0, 0]]

# 1. loadExData
# data = loadExData()
# U,sigma,VT = linalg.svd(data)
# print sigma
# print VT


# 2.
def ecludSim(inA, inB):
    return 1.0 / (1.0 + linalg.norm(inA - inB))

def pearsSim(inA, inB):
    if len(A) < 3.0:
        return 1.0
    return 0.5 + 0.5 * corrcoef(inA, inB, rowvar=0)[0][1]

def cosSim(inA, inB):
    # print inA;shape(inB)
    num = float(inA.T * inB)
    denom = linalg.norm(inA) * linalg.norm(inB)
    return 0.5 + 0.5 * (num/denom)

def standEst(dataMat, user, simMeas, item):
    m,n = shape(dataMat)
    simTotal = 0.0; rateSimTotal = 0.0
    for j in range(n):
        userRating = dataMat[user,j]
        if userRating == 0: continue
        overLap = nonzero(logical_and(dataMat[:,item].A>0,dataMat[:,j].A>0))[0]
        if len(overLap) == 0: similarity = 0
        else: similarity = simMeas(dataMat[overLap, item], dataMat[overLap, j])

        simTotal += similarity
        rateSimTotal += similarity * userRating

    if simTotal == 0: return
    else: return rateSimTotal / simTotal


# svd奇异值分解
def svdEst(dataMat, user, simMeas, item):
    m,n = shape(dataMat)
    simTotal = 0.0; ratSimTotal = 0.0
    U, sigma, VT = linalg.svd(dataMat)
    Sig4 = mat(eye(4) * sigma[:4])
    xformedItems = dataMat.T * U[:,:4] * Sig4.I #减少行还是列
    for j in range(n):
        userRating = dataMat[user,j]
        if userRating == 0 or j == item: continue

        similarity = simMeas(xformedItems[item,:].T,xformedItems[j,:].T)
        simTotal += similarity
        ratSimTotal += userRating * similarity
    if ratSimTotal == 0: return 0
    else: return ratSimTotal / simTotal

def recommend(dataMat, user, N = 3, simMeas = cosSim, estMethod=svdEst):
    unratedItems = nonzero(dataMat[user,:].A == 0)[1]
    if len(unratedItems) == 0: return 'you rated everything'
    itemScores = []
    for item in unratedItems:
        estimateScore = estMethod(dataMat, user, simMeas, item)
        itemScores.append((item, estimateScore))
    return sorted(itemScores, key=lambda jj:jj[1], reverse=True)[:N]




# myMat = mat(loadExData())
# A = myMat[:,0]
# meanA = mean(A, axis=0)
# B = myMat[:,4]
# meanB = mean(B, axis=0)
#
# print cosSim(A,B)
# print cosSim(A-meanA,B-meanB)
# print pearsSim(A,B)
# print pearsSim(A-meanA,B-meanB)

myMat = mat(loadExData())
myMat[0,1]=myMat[0,0]=myMat[1,0]=myMat[2,0]=4
myMat[3,3] = 2
print recommend(myMat, 2)
