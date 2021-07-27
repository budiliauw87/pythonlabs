# -------------------------------
#  Scrapper Tool 2
#  This find embed link detail movie
#  Created By Budiliauw87
# -------------------------------
import os,csv,time,requests,numpy
from bs4 import BeautifulSoup

def getInputMaxPage():
    totalpages = int(input("Insert maximum pages number :\n"))
    return totalpages

def findCSVFile():
    listCsv = []
    for file in os.listdir():
        if file.endswith(".csv"):
            listCsv.append(file)
    return listCsv

def readDataCSV(filename):
    rowLinks = []
    try:
        with open(filename, "r") as f:
            reader = csv.reader(f)
            for i, line in enumerate(reader):
                if (i > 0):
                    rowLink = []
                    titlemovie = line[0]
                    print("find embed for movie {}".format(titlemovie))
                    rowLink.append(titlemovie)
                    page = requests.get(line[1])
                    soup = BeautifulSoup(page.content, "html.parser")
                    entities = soup.find_all("tr", class_="linkTr")
                    for entitie in entities:
                        links = entitie.find_all("td",class_="linkHiddenUrl")
                        for link in links:
                            rowLink.append(link.text)
                    rowLinks.append(rowLink)        
    except:
        print("Something wrong !!")
    finally:
        print("Saving data...")    
        fileEmbed = time.strftime("%Y%m%d%H%M%S")+"-embed.csv"
        numpy.savetxt(fileEmbed, numpy.array(rowLinks), delimiter=',',header='Judul Film, Link Embed', fmt="%s")
        print("Finish ")

if __name__ == "__main__":

    listFile = findCSVFile()
    count = 1
    for filecsv in listFile:
        print("{}. {}".format(count,filecsv))
        count = count + 1

    indexFiles = int(input("Select list file :\n"))
    selectedFile = listFile[indexFiles-1]
    readDataCSV(selectedFile)