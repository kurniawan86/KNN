from read_data import ReadData

class Filter:
    datasetOri = None
    objData = ReadData()

    def __init__(self):
        self.datasetOri = self.objData.readExcel()

    def filteringA(self):
        pass

    def filteringB(self):
        pass