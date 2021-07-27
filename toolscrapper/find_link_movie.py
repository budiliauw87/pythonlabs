# -------------------------------
#  Scrapper Tool 1
#  This find url detail movie
#  Created By Budiliauw87
# -------------------------------
import os,csv,time,requests,numpy
from bs4 import BeautifulSoup

def getInputMaxPage():
    totalpages = int(input("Insert maximum pages number :\n"))
    return totalpages

def findListMovie(maxPage):
        tempData = []
        URL = "https://losmovies.life"
        count = 0
        while(count <= maxPage):
            if(count > 1):
              URL = "https://losmovies.life/?page="+str(count)
            try:
                # Scrapping using BeautifulSoup
                print ("Processing on url : ", URL)
                page = requests.get(URL)
                soup = BeautifulSoup(page.content, "html.parser")
                results = soup.find_all("div", class_="showEntity")
                for result in results:
                    title_elemen = result.find("h4",class_="showRowText").text
                    image_elemen = result.find("div", class_="showRowImage")
                    link_elemen = "https://losmovies.life"+image_elemen.find("a")['href']
                    rowslist = [title_elemen,link_elemen]
                    tempData.append(rowslist)
            except:
                print("Something else went wrong")
            finally:
                count = count + 1

        # save all data to csv
        print("Saving data...")    
        filename = time.strftime("%Y%m%d%H%M%S")+"-data.csv"
        numpy.savetxt(filename, numpy.array(tempData), delimiter=',', header="Judul Film,Detail Link", fmt="%s")    
        print("Processing all page done")    

if __name__ == "__main__":
    maximumPage = getInputMaxPage()
    if(maximumPage > 0):
        findListMovie(maximumPage)
    else:
        print("Please input correct value")