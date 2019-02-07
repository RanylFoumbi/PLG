
import os
import json
from .BingSearch import BingSearch

class FileManager():

    def WriteInFile(self,data,enterUrl,LastpageNbr):
        os.chdir(r'C:\Users\euseb\Desktop\DEV\Projet Django\PLG\Generation_2_lead\example\cache')
        if self.verifyIfFileExist(self,enterUrl):
            fdata = []
            try:
                with open("{}.json".format(enterUrl), 'r') as outfile:
                    fdata = json.load(outfile)
                    del fdata[-1]

                with open("{}.json".format(enterUrl), 'w') as outfile:
                    fdata.append(data)
                    fdata.append({"LastpageNbr": LastpageNbr})
                    json.dump(fdata, outfile)
            except FileNotFoundError:
                pass

        else:
            try:
                with open("{}.json".format(enterUrl), 'w') as outfile:
                    data.append({"LastpageNbr": LastpageNbr})
                    json.dump(data, outfile)
            except FileNotFoundError:
                pass


    def GetLastPageNumber(self, enterUrl):
        os.chdir(r'C:\Users\euseb\Desktop\DEV\Projet Django\PLG\Generation_2_lead\example\cache')
        try:

            with open("{}.json".format(enterUrl), "r") as printer:
                fdata = json.load(printer)
                lastNumber = fdata[-1]['LastpageNbr']

        except FileNotFoundError:
            return None
        return lastNumber

    def verifyIfFileExist(self,enterUrl):

        os.chdir(r'C:\Users\euseb\Desktop\DEV\Projet Django\PLG\Generation_2_lead\example\cache')
        try:
            if os.path.isfile("{}.json".format(enterUrl)):
                return True
            else:
                return False
        except FileNotFoundError:
            pass

    def getFiveFirstEmail(self,enterUrl):
        fiveFirstEmail =[]
        os.chdir(r'C:\Users\euseb\Desktop\DEV\Projet Django\PLG\Generation_2_lead\example\cache')
        try:
            with open("{}.json".format(enterUrl), "r") as printer:
                fdata = json.load(printer)
                fiveFirstEmail = fdata[slice(0,5,1)]

        except FileNotFoundError:
            pass

        return fiveFirstEmail