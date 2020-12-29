#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = "Noah Harel"
__contact__ = "noaharel01@gmail.com"

"""
This script separates text to sentences, one line per sentence.
To run, have the script and input files in the same directory. In this directory, run:
python textToSents.py <filename>
where <filename> is a relative path of the structure: filename.txt
Works on windows 10, python 3.6.0
Disclaimer: this code is not the fastest or most efficient, it can be improved if given more time.
"""

import sys


# creates a list of all the patterns we want to avoid splitting, so they can be masked
def setReplacements():
    senStoppers = [". ", "? ", "! "]
    endBrackets = [")", "]", "}"]
    hebChars = [c for c in "אבגדהוזחטיכךלמםנןסעפףצץקרשת"]
    engChars = [chr(c) for c in range(ord("A"), ord("Z")+1)]+[chr(c) for c in range(ord("a"), ord("z")+1)]
    # line numbers
    rep = [str(num)+". " for num in range(10)]
    # dot dot dot
    rep.extend([".. ", "... "])
    # accidental space before a closing bracket
    rep.extend([s+b for s in senStoppers for b in endBrackets])
    # closing quotes in the end of a sentence
    rep.extend([s + "\"\n" for s in senStoppers])
    # P.S. and initials
    rep.extend(["."+ c + ". " for c in hebChars+engChars])
    # get unique tags for each of the replaceable patterns
    repNum = len(rep)
    # creates unique codes for each pattern so it can be masked and then unmasked later
    tags = (["cuteCode+"+str(i)+"unq" for i in range(repNum)])
    return rep, tags


# reads text from file
def pathToText(filename):
    with open(filename, "r",  encoding="utf-8") as myFile:
        data = myFile.readlines()
    return data


# masks all the patterns to avoid so they don't get changed
def tag(line, rep, tags, repNum):
    for i in range(repNum):
        line = line.replace(rep[i], tags[i])
    return line


# unmasks all the patterns to avoid after the splitting is done, restores the text to where it was before masking
def untag(line, rep, tags, repNum):
    for i in range(repNum):
        line = line.replace(tags[i], rep[i])
    return line

# replaces a stopping sign followed by a space with the same sign followed by a "down one line" symbol
def sep(line):
    line = line.replace(". ", ".\n")
    line = line.replace("? ", "?\n")
    line = line.replace("! ", "!\n")
    return line

# masks all the avoidable patterns, separates sentences and then unmasks the avoidable patterns back to normal
# all good sentences are appended to the lists of sentences
def separateText(text, sents, rep, tags, repNum):
    for line in text:
        line = line.replace("\t", "")
        line = line.replace("\r", "")
        line = tag(line, rep, tags, repNum)
        line = sep(line)
        line = untag(line, rep, tags, repNum)
        sents.append(line)

def outputWrite(inFileName, text):
    # adds "_SentSep" to the file name to distinguish input from output
    outFileName = inFileName.split(".")[0]+"_SentSep.txt"
    file = open(outFileName, "w", encoding = "utf-8")
    file.write(newText)
    file.close()

if __name__ == '__main__':

    inFileName = str(sys.argv[1])
    if inFileName.split(".")[1] != "txt":
        print("Error: argument must be a file path: \"file.txt\"")
        exit()
    rep, tags = setReplacements()
    repNum = len(rep)
    text = pathToText(inFileName)
    sents = []
    separateText(text, sents, rep, tags, repNum)
    newText = "".join(sents)
    outputWrite(inFileName, newText)
