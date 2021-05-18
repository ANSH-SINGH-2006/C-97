sentence=input("sentence: ")
characterCount=0
wordCount=1

for i in sentence:
    characterCount=characterCount+1
    if(i==" "):
        wordCount=wordCount+1
        characterCount=characterCount-1
print(wordCount, characterCount)
