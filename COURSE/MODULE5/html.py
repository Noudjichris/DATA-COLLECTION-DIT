import json
from msilib.schema import Class
#from .utils import Utils
from bs4 import BeautifulSoup
import csv

BASE_URL = 'COURSE/DATABASES/data-zIybdmYZoV4QSwgZkFtaB.html'


class HtmlFactory(object):
    @classmethod
    def openFile(cls):
        with open(BASE_URL) as file:
            data = file.read()
            data = BeautifulSoup(
                data,
                'html.parser')
            file.close()
        return data
        
    @classmethod
    def getRows(cls,data):
        rows = data.find('table').find('tbody').find_all('tr')
        return rows

    def getHeader(cls,data):
        rows = data.find('table').find('thead').find_all('tr')
        lists = []
        for row in rows:
            datas = row.find_all('th')
            list = [
            datas[0].getText(),
            datas[1].getText(),
            datas[2].getText(),
            datas[3].getText(),
            datas[4].getText(),
            datas[5].getText(),
            ]            
            lists.append(list)
        return lists

    @classmethod
    def getList(cls, rows):
        lists = []
        for row in rows:
            datas = row.find_all('td')
            list = [
            datas[0].getText(),
            datas[1].getText(),
            datas[2].getText(),
            datas[3].getText(),
            datas[4].getText(),
            datas[5].getText(),
            ]            
            lists.append(list)
        return lists
    
class CsvFactory(object):
   
    def convertToCsv(cls,header, lists):
        with open('hr_record.csv','w') as f:
            write=csv.writer(f)
            write.writerows(header)
            write.writerows(lists)   

class JsonFactory(object):
   
    @classmethod
    def getListDictionnary(cls,header, lists):
        dictionnary = []
        for list in lists:
            dict = {
                "Name":list[0],
                "Phone":list[1],
                "Email":list[2],
                "LatLon":list[3],
                "Salary":list[4],
                "Age":list[5],
            }
            dictionnary.append(dict)
        return dictionnary
    
    @classmethod
    def convertToJson(cls,dictionnary):
        with open('hr_json.json', 'w') as f:
            json.dump(dictionnary,f,indent=4)   


if __name__=='__main__':
    htmlFactory = HtmlFactory()
    data =htmlFactory.openFile()
    rows = htmlFactory.getRows(data)
    header = htmlFactory.getHeader(data)
    lists = htmlFactory.getList(rows)
   
    cvsFactory = CsvFactory()
    cvsFactory.convertToCsv(header,lists)

    jsonFactory=JsonFactory()
    dictionnary= jsonFactory.getListDictionnary(header,lists)
    #print(dictionnary)
    jsonFactory.convertToJson(dictionnary)
