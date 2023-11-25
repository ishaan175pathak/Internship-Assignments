import pandas
import os
from text_analysis import textAnalysis
from fetch_and_save import data

result = {"URL_ID": list(),
          "URL": list(),
          "POSITIVE SCORE": list(),
          "NEGATIVE SCORE": list(),
          "POLARITY SCORE": list(),
          "SUBJECTIVITY SCORE": list(),
          "AVG SENTENCE LENGTH": list(),
          "PERCENTAGE OF COMPLEX WORDS": list(),
          "FOG INDEX": list(),
          "AVG NUMBER OF WORDS PER SENTENCE": list(),
          "COMPLEX WORD COUNT": list(),
          "WORD COUNT": list(),
          "SYLLABLE PER WORD": list(),
          "PERSONAL PRONOUNS": list(),
          "AVG WORD LENGTH": list()}

# fetching file url id 

for _, url in data.iterrows():
    print(f"for url {url[0]}")
    result["URL_ID"].append(url[0])
    result["URL"].append(url[1])

    analysisResult = textAnalysis(f"C:/Users/dell/OneDrive/Desktop/Data Engineering Assignment/data/{str(url[0])}")
    
    for colname, val in zip(list(result.keys())[2:], analysisResult):
        result[colname].append(val)

output = pandas.DataFrame(result)

output.to_csv("C:/Users/dell/OneDrive/Desktop/Data Engineering Assignment/Output.csv", index=False)