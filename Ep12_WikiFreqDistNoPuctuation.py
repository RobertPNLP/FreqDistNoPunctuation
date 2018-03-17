from nltk.probability import FreqDist
from nltk.tokenize import word_tokenize
import wikipedia as wiki
import operator

def getFreqDist(wikiArtical):
    
    tokWord_summary = word_tokenize(wiki.summary(wikiArtical))
    noPunctuation_summary = list()
    Punctuation = ['.',',','"','?',';',':','}','{','(',')','!','@','#',"''",'""',
                   "``"]
    for i in range(0,len(tokWord_summary)):
        tokWord_summary[i] = tokWord_summary[i].lower()
        if tokWord_summary[i] in Punctuation:
            pass
        else:
            noPunctuation_summary.append(tokWord_summary[i])
            
    fDist = FreqDist(noPunctuation_summary)

    # https://stackoverflow.com/questions/613183/how-do-i-sort-a-dictionary-by-value
    sorted_fDist = sorted(fDist.items(), key=operator.itemgetter(1))
    sorted_fDist.reverse() # sorted in-place
    
    return(sorted_fDist)
