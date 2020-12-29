# TextToSentences
Separates lines which have multiple sentences in them into separate lines, one per sentence. Works in Hebrew, UTF-8.

For example,
for an input file such as in.txt, We get an output file such as in_SentSep.txt.
This was created for a specific type of files, where the lines are already meant to be separated to sentences by "." or "\n" somehow,
but the separated lines still contain more than one sentence each.

To run, have the script and input files in the same directory. In this directory, run:
`python textToSents.py <filename>`
where <filename> is a relative path of the structure: filename.txt
Works on windows 10, python 3.6.0
Efficiancy and complexity can be improved, it was written in a time crunch
