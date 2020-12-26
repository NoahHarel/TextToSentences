# TextToSentences
Separates lines which have multiple sentences in them into separate lines, one per sentence. Works in Hebrew, UTF-8.

For example,
for an input file such as in.txt:

היי מה נשמע? רציתי לראות אם יש פה הפרדה למשפטים. אשמח לראות את השורות האלה כשלוש שורות נפרדות.
והנה עוד שורה בלי נקודה
נקודה, נקודה!  נקודה.

We get an output file such as in_SentSep.txt:

היי מה נשמע?
רציתי לראות אם יש פה הפרדה למשפטים.
אשמח לראות את השורות האלה כשלוש שורות נפרדות.
והנה עוד שורה בלי נקודה
נקודה, נקודה!
 נקודה.
 
 This was created for a specific type of files, where the lines are already meant to be separated to sentences by "." or "\n" somehow,
 but the separated lines still contain more than one sentence each.
