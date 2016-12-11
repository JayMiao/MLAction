from numpy import *
from time import sleep

def loadDataSet(fileName):
    dataMat = []; labelMat = []
    fp = open(fileName)
    for line in fp.readlines():
        lineArr = line.strip().split('\t')
        dataMat.append([float(lineArr[0]), float(lineArr[1])])
        labelMat.append(float(lineArr[2]))
    return dataMat,labelMat

def selectJrand(i, m):
    j = i
    while (j == i):
        j = int(random.uniform(0, m))
    return j

def clipAlpha(aj, H, L):
    if aj > H:
        aj = H
    if aj < L:
        aj = L
    return aj


def smoSimple(dataMatIn, classLabels, C, toler, maxIter):
    dataMatIn = mat(dataMatIn); classLabels = mat(classLabels).transpose()
    b = 0; m,n = shape(dataMatIn)
    alphas = mat(zeros((m,1)))
    iter = 0
    while (iter < maxIter):
        alphaPairsChanged = 0
        for i in range(m):
            fXi = float(multiply(alphas,classLabels).T*(dataMatIn*dataMatIn[i,:].T)) + b
            Ei = fXi - float(classLabels[i])#if checks if an example violates KKT conditions
            if ((classLabels[i] * Ei < -toler) and (alphas[i] < C)) \
                or \
                ((classLabels[i] * Ei > toler) and (alphas[i] > 0)):
                j = selectJrand(i, m)
                fXj = float(multiply(alphas,classLabels).T * (dataMatIn*dataMatIn[j,:].T)) + b
                Ej = fXj - float(classLabels[j])
                alphaIold = alphas[i].copy()
                alphaJold = alphas[j].copy()
                if classLabels[i] != classLabels[j]:
                    L = max(0, alphas[j] + alphas[i] - C)
                    H = min(C, C + alphas[j] - alphas[i])
                else:
                    L = max(0, alphas[j] + alphas[i] - C)
                    H = min(C, alphas[j] + alphas[i])
                if L == H:
                    print "L = H"
                    continue
                eta = 2.0 * dataMatIn[i, :] * dataMatIn[j, :].T \
                      -dataMatIn[i, :] * dataMatIn[i, :].T \
                      -dataMatIn[j, :] * dataMatIn[j, :].T
                if eta >= 0:
                    print "eta >= 0"
                    continue
                alphas[j] -= classLabels[j] * (Ei - Ej) / eta
                alphas[j] = clipAlpha(alphas[j], H, L)
                if abs(alphas[j] - alphaJold) < 0.00001:
                    print "j not moving"
                    continue
                alphas[i] += classLabels[j] * classLabels[i] * (alphaJold - alphas[j])
                b1 = b - Ei - classLabels[i] * (alphas[i] - alphaIold) * \
                     dataMatIn[i,:] * dataMatIn[i, :].T - \
                     classLabels[j] * (alphas[j] - alphaJold) *\
                     dataMatIn[i, :] * dataMatIn[j, :].T
                b2 = b - Ej - classLabels[i] * (alphas[i] - alphaIold) * \
                     dataMatIn[i,:] * dataMatIn[j, :].T - \
                     classLabels[j] * (alphas[j] - alphaJold) * \
                     dataMatIn[j, :] * dataMatIn[j,:].T
                if (alphas[i] > 0) and (alphas[i] < C): b = b1
                elif (alphas[j] > 0) and (alphas[j] < C): b = b2
                else: b = (b1 + b2) / 2.0
                alphaPairsChanged += 1
                print "iter: %d i: %d, pairs changed %d" % (iter,i,alphaPairsChanged)
        if alphaPairsChanged == 0:
            iter += 1
        else:
            iter = 0
            print "iter number: %d " % iter
    return b,alphas

def smoSimple1(dataMatIn, classLabels, C, toler, maxIter):
    dataMatrix = mat(dataMatIn); labelMat = mat(classLabels).transpose()
    print dataMatrix
    b = 0; m,n = shape(dataMatrix)
    alphas = mat(zeros((m,1)))
    iter = 0
    while (iter < maxIter):
        alphaPairsChanged = 0
        for i in range(m):
            fXi = float(multiply(alphas,labelMat).T*(dataMatrix*dataMatrix[i,:].T)) + b
            Ei = fXi - float(labelMat[i])#if checks if an example violates KKT conditions
            if ((labelMat[i]*Ei < -toler) and (alphas[i] < C)) or ((labelMat[i]*Ei > toler) and (alphas[i] > 0)):
                j = selectJrand(i,m)
                fXj = float(multiply(alphas,labelMat).T*(dataMatrix*dataMatrix[j,:].T)) + b
                Ej = fXj - float(labelMat[j])
                alphaIold = alphas[i].copy(); alphaJold = alphas[j].copy();
                if (labelMat[i] != labelMat[j]):
                    L = max(0, alphas[j] - alphas[i])
                    H = min(C, C + alphas[j] - alphas[i])
                else:
                    L = max(0, alphas[j] + alphas[i] - C)
                    H = min(C, alphas[j] + alphas[i])
                if L==H: print "L==H"; continue
                eta = 2.0 * dataMatrix[i,:]*dataMatrix[j,:].T - dataMatrix[i,:]*dataMatrix[i,:].T - dataMatrix[j,:]*dataMatrix[j,:].T
                if eta >= 0: print "eta>=0"; continue
                alphas[j] -= labelMat[j]*(Ei - Ej)/eta
                alphas[j] = clipAlpha(alphas[j],H,L)
                if (abs(alphas[j] - alphaJold) < 0.00001): print "j not moving enough"; continue
                alphas[i] += labelMat[j]*labelMat[i]*(alphaJold - alphas[j])#update i by the same amount as j
                                                                        #the update is in the oppostie direction
                b1 = b - Ei- labelMat[i]*(alphas[i]-alphaIold)*dataMatrix[i,:]*dataMatrix[i,:].T - labelMat[j]*(alphas[j]-alphaJold)*dataMatrix[i,:]*dataMatrix[j,:].T
                b2 = b - Ej- labelMat[i]*(alphas[i]-alphaIold)*dataMatrix[i,:]*dataMatrix[j,:].T - labelMat[j]*(alphas[j]-alphaJold)*dataMatrix[j,:]*dataMatrix[j,:].T
                if (0 < alphas[i]) and (C > alphas[i]): b = b1
                elif (0 < alphas[j]) and (C > alphas[j]): b = b2
                else: b = (b1 + b2)/2.0
                alphaPairsChanged += 1
                print "iter: %d i:%d, pairs changed %d" % (iter,i,alphaPairsChanged)
        if (alphaPairsChanged == 0): iter += 1
        else: iter = 0
        print "iteration number: %d" % iter
    return b,alphas
dataArr, labelArr = loadDataSet('testSet.txt')
b, alphas = smoSimple1(dataArr, labelArr, 0.6, 0.001, 40)
print b
print alphas