from numpy import *
import operator
from sklearn import preprocessing
import matplotlib
import matplotlib.pyplot as plt

def createDataSet():
    group = array([[1.0,1],[1.0,1.0],[0,0],[0,0.1]])
    labels = ['A','A','B','B']
    return group,labels

# knn
def classify0(inX, dataSet, labels, k):
    dataSetSize = dataSet.shape[0]
    diffMat = tile(inX, (dataSetSize,1)) - dataSet
    sqDiffMat = diffMat**2
    sqDistances = sqDiffMat.sum(axis=1)
    distances = sqDistances**0.5
    sortedDistIndicies = distances.argsort()
    classCount={}
    for i in range(k):
        voteIlabel = labels[sortedDistIndicies[i]]
        classCount[voteIlabel] = classCount.get(voteIlabel,0) + 1
    sortedClassCount = sorted(classCount.iteritems(), key=operator.itemgetter(1), reverse=True)
    return sortedClassCount[0][0]


def file2matrix(filename):
    fr = open(filename)
    numberOfLines = len(fr.readlines())         #get the number of lines in the file
    returnMat = zeros((numberOfLines,3))        #prepare matrix to return
    classLabelVector = []                       #prepare labels return
    fr = open(filename)
    index = 0
    for line in fr.readlines():
        line = line.strip()
        listFromLine = line.split('\t')
        returnMat[index,:] = listFromLine[0:3]
        classLabelVector.append(int(listFromLine[-1]))
        index += 1
    return returnMat,classLabelVector

def autoNorm(dataSet):
    minVal = dataSet.min(0)
    maxVal = dataSet.max(0)
    ranges = maxVal - minVal
    normDataSet = zeros(shape(dataSet))
    m = dataSet.shape[0]
    test = tile(minVal,(m,1))
    norDataSet = dataSet - tile(minVal,(m,1))
    norDataSet = norDataSet/tile(ranges,(m,1))
    return norDataSet,ranges,minVal

def autoNormSklearn(dataSet):
    X_train_minmax = preprocessing.MinMaxScaler().fit_transform(dataSet)
    return X_train_minmax

def datingClassTest():
    hoRatio = 0.50      #hold out 10%
    datingDataMat,datingLabels = file2matrix('datingTestSet2.txt')       #load data setfrom file
    normMat, ranges, minVals = autoNorm(datingDataMat)
    m = normMat.shape[0]
    numTestVecs = int(m*hoRatio)
    errorCount = 0.0
    for i in range(numTestVecs):
        classifierResult = classify0(normMat[i,:],normMat[numTestVecs:m,:],datingLabels[numTestVecs:m],3)
        print "%d: the classifier came back with: %d, the real answer is: %d" % (i,classifierResult, datingLabels[i])
        if (classifierResult != datingLabels[i]): errorCount += 1.0
    print "the total error rate is: %f" % (errorCount/float(numTestVecs))
    print errorCount
# datingClassTest()
# group,labels = createDataSet()
# print classify0([0,0],group,labels,3)
# datingDataMat,datingLabels = file2matrix('datingTestSet2.txt')

#normalize
# norMat = autoNorm(datingDataMat)
# norMatSklearn = autoNormSklearn(datingDataMat)


# exit()
# fig = plt.figure()
# ax = fig.add_subplot(1,1,1)
# # print array(datingLabels)
# print datingLabels
# ax.scatter(datingDataMat[:,0], datingDataMat[:,2],15*array(datingLabels),15*array(datingLabels)) # x-axis , y-axis
# plt.show()
