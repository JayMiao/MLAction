# -*- coding: utf-8 -*-
from numpy import *
import matplotlib.pyplot as plt

def loadData(fileName):
    numFeat = len(open(fileName).readline().split('\t')) - 1
    dataMat = []; labelMat = []
    fp = open(fileName)
    for line in fp.readlines():
        lineArr = []
        currLine = line.strip().split('\t')
        for i in range(numFeat):
            lineArr.append(float(currLine[i]))
        dataMat.append(lineArr)
        labelMat.append(float(currLine[-1]))
    return dataMat,labelMat

def standRegres(xArr, yArr):
    xMat = mat(xArr); yMat = mat(yArr).T
    xTx = xMat.T * xMat
    if linalg.det(xTx) == 0:
        print 'errrr'
        return
    ws = xTx.I * (xMat.T * yMat)
    return ws

def lwlr(testPoint, xArr, yArr, k=1.0):
    xMat = mat(xArr)
    yMat = mat(yArr).T
    m, n = shape(xMat)
    weights = mat(eye(m))
    for j in range(m):
        diffMat = testPoint - xMat[j,:]
        weights[j,j] = exp(diffMat * diffMat.T / (-2.0*k**2))
    xTx = xMat.T * (weights * xMat)
    if linalg.det(xTx) == 0:
        return
    ws = xTx.I * (xMat.T * (weights * yMat))
    return testPoint * ws

def lwlrTest(testArr, xArr, yArr, k=1.0):
    m,n = shape(testArr)
    yHat = zeros(m)
    for i in range(m):
        yHat[i] = lwlr(testArr[i], xArr, yArr, k)
    return yHat


def ridgeRegres(xMat, yMat, lam = 0.2):
    xTx = xMat.T * xMat
    denom = xTx + eye(shape(xMat)[1]) * lam
    if linalg.det(denom) == 0:
        return
    ws = denom.I * (xMat.T * yMat)
    return ws

def ridgeTest(xArr, yArr):
    xMat = mat(xArr); yMat = mat(yArr).T
    yMean = mean(yMat, axis=0)
    yMat = yMat - yMean
    xMeans = mean(xMat, axis=0)
    xVar = var(xMat, 0)
    xMat = (xMat - xMeans) / xVar
    numTestPts = 30
    wMat = zeros((numTestPts, shape(xMat)[1]))
    for i in range(numTestPts):
        ws = ridgeRegres(xMat, yMat, exp(i - 10))
        wMat[i,:] = ws.T
    return wMat

def regularize(xMat):
    inMat = xMat.copy()
    inMeans = mean(inMat,0)
    inVar = var(inMat,0)
    inMat = (inMat - inMeans) / inVar
    return inMat
def rssError(yArr, yHatArr):
    return ((yArr - yHatArr) ** 2).sum()

def stageWise(xArr, yArr, eps=0.01, numIt=100):
    xMat = mat(xArr)
    yMat = mat(yArr).T
    yMean = mean(yMat,0)
    yMat = yMat - yMean
    xMat = regularize(xMat)
    m,n = shape(xMat)
    ws = zeros((n,1)); wsTest = ws.copy(); wsMax = ws.copy()
    retMat = zeros((numIt, n))
    for i in range(numIt):
        # print ws.T
        lowwestError = inf
        for j in range(n):
            for sign in [-1,1]:
                wsTest = ws.copy()
                wsTest[j] += eps*sign
                yTest = xMat * wsTest
                rssE = rssError(yMat.A, yTest.A)
                if rssE < lowwestError:
                    lowwestError = rssE
                    wsMax = wsTest
        ws = wsMax.copy()
        retMat[i,:] = ws.T
    return retMat


# 4. ridgeRegres
# xArr, yArr = loadData('abalone.txt')
# ridgeWeights = ridgeTest(xArr, yArr)
# print ridgeWeights[0:2]
# plt.plot(ridgeWeights[0:2])
# plt.show()
# exit()

# 5. stage wise
xArr, yArr = loadData('abalone.txt')
wsMat = stageWise(xArr, yArr, 0.001, 10000)
plt.plot(wsMat)
plt.show()
# xArr, yArr = loadData('ex0.txt')
# ws = standRegres(xArr, yArr)
# xMat = mat(xArr)
# yMat = mat(yArr)
# yHat = xArr * ws

# 1. stand regress
# plt.scatter(xMat[:,1].flatten().A[0], yMat.T[:,0].flatten().A[0])
# xMat.sort(0)
# yHat = xMat * ws
# plt.plot(xMat[:,1],yHat)
# plt.show()

# 2. lwlr
# print lwlr(xArr[0], xArr, yArr, 1.0)
# print lwlr(xArr[0], xArr, yArr, 0.001)

# 3. lwlr with varies k
# yHat = lwlrTest(xArr, xArr, yArr, 0.1)
# yHat = lwlrTest(xArr, xArr, yArr, 0.01)
# yHat = lwlrTest(xArr, xArr, yArr, 0.003)
# srtInd = xMat[:,1].argsort(0)
# xSort = xMat[srtInd][:,0,:]
# plt.plot(xSort[:,1],yHat[srtInd])
# plt.scatter(xMat[:,1].flatten().A[0], yMat.T[:,0].flatten().A[0], s=2, c='red')
# plt.show()

# print corrcoef(yHat.T, yMat)