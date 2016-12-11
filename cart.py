from itertools import *
import pdb
def featuresplit(features):
    count = len(features)
    featureind = range(count)
    featureind.pop(0) #get value 1~(count-1)
    combiList = []
    for i in featureind:
        com = list(combinations(features, len(features[0:i])))
        combiList.extend(com)
    combiLen = len(combiList)
    featuresplitGroup = zip(combiList[0:combiLen/2], combiList[combiLen-1:combiLen/2-1:-1])
    return featuresplitGroup
if __name__ == '__main__':
    test= range(3)
    splitGroup = featuresplit(test)
    print 'splitGroup', len(splitGroup), splitGroup
    test= range(4)
    splitGroup = featuresplit(test)
    print 'splitGroup', len(splitGroup),splitGroup
    test= range(5)
    splitGroup = featuresplit(test)
    print 'splitGroup', len(splitGroup),splitGroup
    test= ['young','middle','old']
    splitGroup = featuresplit(test)
    print 'splitGroup', len(splitGroup),splitGroup