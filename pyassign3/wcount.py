"""wcount.py: count words from an Internet file.

__author__ = "Sun Siyuan"
__pkuid__  = "1600012120"
__email__  = "1600012120@pku.edu.cn"
"""

import sys
from urllib.request import urlopen

def removepunc(bstring):
    nopunc=""
    for iix in bstring:
        if iix.isalpha()==True or iix==" ":
            nopunc=nopunc+iix
    return nopunc

def wcount(lines, topn=10):
    """count words from lines of text string, then sort by their counts
    in reverse order, output the topn (word count), each in one line. 
    """
    lines=removepunc(lines)
    lines=lines.lower()
    lineslst=lines.split()
    cting={}
    for i in lineslst:
        if i not in cting.keys():
            cting[i]=1
        else:
            cting[i]=cting[i]+1
    lst_tuple=list(cting.items())
    lst=sorted(lst_tuple, key=lambda lst: lst[1], reverse=True)  
    lst=lst[0:topn]
    for (a,b) in lst:
        c,d=(a,b)
        print(c," "*(12-len(c)),d,"\n")

    

if __name__ == '__main__':

    if  len(sys.argv) == 1:
        print('Usage: {} url [topn]'.format(sys.argv[0]))
        print('  url: URL of the txt file to analyze ')
        print('  topn: how many (words count) to output. If not given, will output top 10 words')
        sys.exit(1)

    try:
        topn = 10
        if len(sys.argv) == 3:
            topn = int(sys.argv[2])
    except ValueError:
        print('{} is not a valid topn int number'.format(sys.argv[2]))
        sys.exit(1)

    try:
        with urlopen(sys.argv[1]) as f:
            contents = f.read()
            lines   = contents.decode()
            wcount(lines, topn)
    except Exception as err:
        print(err)
        sys.exit(1)