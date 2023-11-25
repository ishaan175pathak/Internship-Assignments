import requests
from bs4 import BeautifulSoup
import os
import pandas

os.system("cls")

def fetchAndSave(url: str, url_id: float, path = ".\data"):
    try:
        response = requests.get(url=url)
        soup = BeautifulSoup(response.content, "html.parser")

        with open(f"{path}\{url_id}", "w", encoding="utf8") as file:
            
            if soup.find("article"):
                for para in soup.find("article").find_all("p"):
                    file.write(str(para.string))
    except:
        print("URLs Ended")
        exit()
def IterTable(data: pandas.DataFrame):
    for _, url in data.iterrows():
       if url[0] and url[1]:
        fetchAndSave(url=url[1], url_id=url[0])

data = pandas.read_csv("Input.csv", encoding="utf-8")
data.dropna(inplace=True)

if __name__ == "__main__":
    IterTable(data)