def pathToText(filename):
    with open(filename, "r",  encoding="utf-8") as myFile:
        data = myFile.readlines()
    return data



inFileName = "in.txt"
text = pathToText(inFileName)
sents = []
for line in text:
    line = line.replace("\t", "")
    line = line.replace("\r", "")
    line = line.replace(". ", ".\n")
    line = line.replace("? ", "?\n")
    line = line.replace("! ", "!\n")
    sents.append(line)
newText = "".join(sents)
print(newText)
outFileName = inFileName.split(".")[0]+"_SentSep.txt"
file = open(outFileName, "w", encoding = "utf-8")
file.write(newText)
file.close()
