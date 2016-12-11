from numpy import *
from logRegres import *

def classsifyVector(x, w):
    prob = sigmoid(sum(x * w))
    return 1 if prob > 0.5 else 0

def colicTest():
    train = open('horseColicTraining.txt')
    test = open('horseColicTest.txt')
    trainSet = []; trainLabel = []
    for line in train.readlines():
        currLine = line.strip().split('\t')
        lineArr = []
        for i in range (21):
            lineArr.append(float(currLine[i]))
        trainSet.append(lineArr)
        trainLabel.append(float(currLine[21]))
    trainWeights = stocGradAscent01(trainSet, trainLabel, 200)
    errorCount = 0; numTestVector = 0.0
    for line in test.readlines():
        numTestVector += 1
        currLine = line.strip().split('\t')
        lineArr = []
        for i in range(21):
            lineArr.append(float(currLine[i]))
        if  int(classsifyVector(array(lineArr), trainWeights)) != int(currLine[21]):
            errorCount += 1
    errorRate = float(errorCount / numTestVector)
    print "error rate : %f " % errorRate
    return errorRate

def multiTest():
    numTest = 10; errorSum = 0.0
    for k in range(numTest):
        errorSum += colicTest()
    print "after %d iterations the average error rate is %f " % (numTest, errorSum / float(numTest))

multiTest()