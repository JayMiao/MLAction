from numpy import *
import numpy as np

def loadDataSet():
    dataMat = []; labelMat = []
    fr = open('testSet.txt')
    for line in fr.readlines():
        lineArr = line.strip().split()
        dataMat.append([1.0, float(lineArr[0]), float(lineArr[1])])
        labelMat.append(int(lineArr[2]))
    return dataMat,labelMat

def sigmoid(inX):
    return 1.0/(1+exp(-inX))

def gradAscent(dataMatIn, classLabels):
    x = mat(dataMatIn)
    y = mat(classLabels).transpose()
    m, n = shape(x)
    cycle = 5000
    alpha = 0.001
    weights = ones((n, 1))
    for i in range(cycle):
        weights = weights + alpha * x.transpose() * (y - sigmoid(x * weights))
    return weights

def stocGradAscent(dataMatIn, classLabels):
    m,n = shape(dataMatIn)
    alpha = 0.01
    weights = ones(n)
    for i in range(m):
        h = sigmoid(sum(dataMatIn[i]) * weights)
        error = classLabels[i] - h
        weights = weights + alpha * error * dataMatIn[i]
    return weights

def stocGradAscent01(dataMatIn, classLabels, numIter = 20):
    dataMatIn = array(dataMatIn)
    m, n = shape(dataMatIn)
    weights = ones(n)
    mark = 0
    for j in range(numIter):
        indexs = arange(m); random.shuffle(indexs)
        for i in indexs:
            h = sigmoid(sum(dataMatIn[i] * weights))
            error = classLabels[i] - h
            alpha = 4 / (1.0 + mark) + 0.01
            weights = weights + alpha * error * dataMatIn[i]
            mark += 1
    return weights

def stocGradAscent1(dataMatrix, classLabels, numIter=150):
    m,n = shape(dataMatrix)
    weights = ones(n)   #initialize to all ones
    for j in range(numIter):
        dataIndex = range(m)
        for i in range(m):
            alpha = 4/(1.0+j+i)+0.0001    #apha decreases with iteration, does not
            randIndex = int(random.uniform(0,len(dataIndex)))#go to 0 because of the constant
            h = sigmoid(sum(dataMatrix[randIndex]*weights))
            error = classLabels[randIndex] - h
            weights = weights + alpha * error * dataMatrix[randIndex]
            del(dataIndex[randIndex])
    return weights

def plotBestFit(weights):
    import matplotlib.pyplot as plt
    dataMat,labelMat=loadDataSet()
    dataArr = array(dataMat)
    n = shape(dataArr)[0]
    xcord1 = []; ycord1 = []
    xcord2 = []; ycord2 = []
    for i in range(n):
        if int(labelMat[i])== 1:
            xcord1.append(dataArr[i,1])
            ycord1.append(dataArr[i,2])
        else:
            xcord2.append(dataArr[i,1])
            ycord2.append(dataArr[i,2])
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.scatter(xcord1, ycord1, s=40, c='red')
    ax.scatter(xcord2, ycord2, s=30, c='green')
    x1 = arange(-3.0, 3.0, 0.1)
    # w0 * x0 + w1 * x1 + w2 * x2 = 0
    x2 = (-weights[0]-weights[1]*x1)/weights[2]
    ax.plot(x1, x2)
    plt.xlabel('X1'); plt.ylabel('X2')
    plt.show()

dataMat,labelMat = loadDataSet()
weights = stocGradAscent01(dataMat, labelMat)
print weights
plotBestFit(weights)
