import typing


class ObjetoMedicion:
    type = [['TP','FP'],['TN','FN']]

    def __init__(self, realValue, measuredValue):
        self.realValue = realValue
        self.measuredValue = measuredValue

    def accuracyPrediction(self):
        return self.realValue==self.measuredValue


class MatrizConfusion:
    def __init__(self,tN,fN,fP,tP):
        self.tN = tN
        self.fN = fN
        self.fP = fP
        self.tP = tP
    
    def accuracy(self):
        return (self.tP + self.tN) / (self.tP +self.tN + self.fP + self.fN)

    def precision(self):
        return self.tP / (self.fN + self.tP) 

    def listValues(self):
        print('The accuracy outcome is ', self.accuracy())
        print('The precision outcome is ', self.precision())
