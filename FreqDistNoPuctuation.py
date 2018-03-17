from nltk.probability import FreqDist
from nltk.tokenize import word_tokenize
import wikipedia as wiki
import operator

def topTenSortedFDist(wikiArtical):
    
    tokWord_summary = word_tokenize(wiki.summary(wikiArtical))
    noPunctuation_summary = list()
    Punctuation = ['.',',','"','?',';',':','}','{','(',')']
    for i in range(0,len(tokWord_summary)):
        if tokWord_summary[i] in Punctuation:
            pass
        else:
            noPunctuation_summary.append(tokWord_summary[i])
            
    fDist = FreqDist(noPunctuation_summary)

    # https://stackoverflow.com/questions/613183/how-do-i-sort-a-dictionary-by-value
    sorted_fDist = sorted(fDist.items(), key=operator.itemgetter(1))
   

    topTen = sorted_fDist[-10:]

    topTen.reverse() # sorted in-place
    
    return(topTen)
