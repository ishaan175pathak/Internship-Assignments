import re
import nltk
from typing import List
from cleaning import ClearingText
import string

class DerivedVariables:
    def __init__(self, filepath) -> None:
        self.positive_dictionary = list()
        self.negative_dictionary = list()
        self.positiveScore = 0
        self.negativeScore = 0
        self.path = filepath
        self.polarity = 0
        self.subjectivity = 0
        self.totalWords = 0
        self.text = str()
        self.lookUp()
        self.calculatePositiveScore()
        self.calculateNegativeScore()
        self.polarityScore()
        self.subjectivityScore()

    def lookUp(self):
        with open("C:/Users/dell/OneDrive/Desktop/Data Engineering Assignment/MasterDictionary/positive-words.txt", "r") as file:
            for text in file.readlines():
                self.positive_dictionary.append(text.replace("\n", ""))

        with open("C:/Users/dell/OneDrive/Desktop/Data Engineering Assignment/MasterDictionary/negative-words.txt", "r") as file:
            for text in file.readlines():
                self.negative_dictionary.append(text.replace("\n", ""))
        try:
            with open(self.path, "r", encoding="utf-8") as file:
                for words in file.readlines():
                    word = words.replace("\n", "")
                    self.text += f" {word}"
        except:
            print("File not found")

        self.text = " ".join(re.split(f"[. | ,]",self.text))

        entireText = nltk.tokenize.word_tokenize(self.text)

        self.text = ClearingText(entireText).filterStopwords()

        self.totalWords = len(self.text) 

    def calculatePositiveScore(self):
        
        for words in self.text:
            if words in self.positive_dictionary:
                self.positiveScore += 1

    def calculateNegativeScore(self) -> int:
        
        for words in self.text:
            if words in self.negative_dictionary:
                self.negativeScore += 1


    def polarityScore(self):
        self.polarity = (self.positiveScore - self.negativeScore) / ((self.positiveScore + self.negativeScore) + 0.000001)

    def subjectivityScore(self):
        self.subjectivity = ((self.positiveScore + self.negativeScore)) / ((self.totalWords) + 0.000001)

    def __str__(self) -> str:
        return f" {self.positiveScore} , {self.negativeScore}, {self.polarity}, {self.subjectivity} "

class ReadabilityAnalysis:
    def __init__(self, filepath: str) -> None:
        self.filepath = filepath
        self.numberOfWords: int = 0
        self.entireText: str = str()
        self.numberOfComplexWord: int = 0
        self.fogIndexVariable: int = 0

        self.readFile()

    def readFile(self):
        try:
            with open(self.filepath, "r", encoding="utf8") as file:
                for words in file.readlines():
                    self.entireText += f" {words}"
        except:
            print("File not found")
    def averageSentanceLength(self):
        self.numberOfWords = nltk.tokenize.word_tokenize(re.sub("[.|,]", "", self.entireText)).__len__()

        numberOfSentences = self.entireText.split(".").__len__()

        return self.numberOfWords / numberOfSentences
    
    def percentageOfComplexWords(self):
        temp = re.sub("[.|,]", "", self.entireText)
        complexWords = 0
        for word in temp.split():
            word = word.lower()
            count = 0
            vowels = "aeiouy"
            if word[0] in vowels:
                count += 1
            for index in range(1, len(word)):
                if word[index] in vowels and word[index - 1] not in vowels:
                    count += 1
            if word.endswith("e"):
                count -= 1
            if count == 0:
                count += 1
            
            if count > 2: 
                complexWords += count
        try:
            self.numberOfComplexWord = complexWords / temp.split().__len__()
        except ZeroDivisionError: 
            self.numberOfComplexWord = complexWords / 1

        return self.numberOfComplexWord

    def fogIndex(self):
        return 0.4 * (self.averageSentanceLength() + self.percentageOfComplexWords())

    def wordCount(self):
        textList: List[str] = nltk.tokenize.word_tokenize(self.entireText)
        result: int = 0

        for word in textList:
            if (word not in string.punctuation) and (word not in nltk.corpus.stopwords.words("english")):
                result += 1

        return result

    def syllablesCount(self):
        temp = re.sub("[.|,]", "", self.entireText)
        complexWords = 0
        
        for word in temp.split():
            word = word.lower()
            count = 0
            vowels = "aeiouy"
            
            if word[0] in vowels:
                count += 1
            
            for index in range(1, len(word)):
                if word[index] in vowels and word[index - 1] not in vowels:
                    count += 1
            
            if len(word) > 1 and list(word)[-2] == "e":
                count -= 1

            if count == 0:
                count += 1
            
            if count > 2: 
                complexWords += count

        return complexWords

    def personalPronouns(self):
        temp: str = "".join([word for word in self.entireText if word not in string.punctuation])

        cleanedText: str = re.sub(r'\b(I|we|ours|my|mine|(?-i:us))\b', "", temp)        
        
        return len(temp) - len(cleanedText)

    def averageWordLength(self):
        totalCharacter: int = 0
        totalWord: int = 0

        temp = [word for word in nltk.tokenize.word_tokenize(re.sub(r"[.|,|:(|)]", "",self.entireText)) if word not in string.punctuation]
        for word in temp: 
            totalCharacter += len(word)
            totalWord += 1

        try:
            return totalCharacter / totalWord
        except: 
            return totalCharacter / 1
        
        

def textAnalysis(filepath: str):
    sentimentAnalysis = DerivedVariables(filepath=filepath)
    secondaryAnalysis = ReadabilityAnalysis(filepath=filepath)

    result = [sentimentAnalysis.positiveScore, sentimentAnalysis.negativeScore, sentimentAnalysis.polarity, sentimentAnalysis.subjectivity, \
              secondaryAnalysis.averageSentanceLength(), secondaryAnalysis.percentageOfComplexWords(), secondaryAnalysis.fogIndex(), secondaryAnalysis.averageSentanceLength(), \
              secondaryAnalysis.numberOfComplexWord, secondaryAnalysis.wordCount(), secondaryAnalysis.syllablesCount(), secondaryAnalysis.personalPronouns(), \
              secondaryAnalysis.averageWordLength()]
    
    return result