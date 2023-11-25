import os
import string
from typing import Any, List
import nltk

class ClearingText:
    def __init__(self, text: List[str]) -> None:
        self.text: List[str] = text
        
    def stopWord(self, filename: str) -> List[str]:
        result = list()

        with open(filename, "r") as file:
            for text in file.readlines():
                text = text.split()
                if len(text) > 1:
                    result.append(text[0].lower().replace("\n", ""))
                else:
                    result.append(text[0].lower().replace("\n", ""))
        
        return result

    def allStopwords(self) -> List[str]:

        os.chdir("C:/Users/dell/OneDrive/Desktop/Data Engineering Assignment/StopWords")

        result = list()

        for filename in os.listdir():
            result.extend(self.stopWord(filename))
        
        return result
    
    def filterStopwords(self) -> List[str]:
        
        result = list()
        stopwords = self.allStopwords()
        for word in self.text:
            if word not in stopwords:
                result.append(word)
        
        return result