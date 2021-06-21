# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import math
import numpy as np
def count(Text):
    for char in '-.,\n!':
        Text=Text.replace(char,' ')
    # split returns a list of words delimited by sequences of whitespace (including tabs, newlines, etc, like re's \s) 
    word_list = Text.split()

    return len(word_list)

def timeStepSecond(setskip,slide):
    setskip = int(setskip)
    minute = 0
    second = int(setskip)
    timeStamp = np.empty(slide+1,dtype=object)
    timeStamp[0] = "00:00:00,000"
    #timeFormat = "00:00:00.000"
    for i in range (1,slide+1):
        
        if (second < 10):
            if (minute < 10):
                timeStamp[i] = "00:0" + str(minute) + ":0" + str(second) + ",000"
            else:
                timeStamp[i] = "00:" + str(minute) + ":0" + str(second) + ",000"
        else:
            if (minute < 10):
                timeStamp[i] = "00:0" + str(minute) + ":" + str(second) + ",000"
            else:
                timeStamp[i] = "00:" + str(minute) + ":" + str(second) + ",000"

            
        second += setskip
        if (second >= 60):
            minute += 1
            second -= 60

    return timeStamp

def textInEachSlide(text,slide,numberOfWordInOneLine,wordcount):
    sentenceTEMP = ""
    textArray = text.split()
    sentence = np.empty(slide,dtype=object)
    start = 0
    finish = (numberOfWordInOneLine * 2)
    SandF = np.zeros(slide+1)
    Temp = 0
    for i in range(1,slide+1):
        Temp += (numberOfWordInOneLine * 2)
        if(Temp > wordcount):
            SandF[i] = wordcount
        else:
            SandF[i] = Temp
        
        
    # print(SandF)
    
    
    
    
    
    for x in range(0,slide):
        count = 0
        if(x!=0):
            start=int(SandF[x])
            finish=int(SandF[x+1])
            
        sentenceTEMP = ""
        for i in range(start,finish):
            count += 1
            if (count == numberOfWordInOneLine):
                sentenceTEMP += textArray[i] + "\n"
            else:
                sentenceTEMP += textArray[i] + " "
        sentence[x] = sentenceTEMP
    return sentence

    

    
def main():
    # Variable
    Subtitle = ""
    SequenceNum = 0
    
    
    
    Text = input("INPUT YOUR TEXT: ")
    wordCount = count(Text)
    timeSkip = input("How many second do you want each one to be? ")
    wordEachLine = input("How many word for each line? ")
    slide = math.ceil((wordCount/int(wordEachLine))/2) #wordcount/10 and then /2 
    timeStampArray = timeStepSecond(timeSkip, slide)
    sentence = textInEachSlide(Text, slide, int(wordEachLine),wordCount)
    
    #INTERFACE
    
    print("=====================================================================")
    print("The word count is: ", wordCount)
    print("The amount of slide is: ", slide)
    print("Time skip: ", timeSkip )
    print("=====================================================================")
    
    # for i in range (0,slide+1):
    #     print(timeStampArray[i])
    # for i in range (0,slide):
    #     print(sentence[i])
    
    for i in range(0,slide):
    
        Subtitle += (str(i+1) + "\n" + timeStampArray[i] + " --> " + timeStampArray[i+1] +"\n" + sentence[i] + "\n\n")
    
    print(Subtitle)

main()

    