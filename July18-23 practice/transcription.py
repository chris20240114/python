with open(r"./Document36.txt", 'r') as fp:
    linecount = len(fp.readlines())

interview = open("./Document36.txt", "r")

y=0
formatted_interview = ''''''
Speaker = 'P:'
def isSpeaker(speaker1, speaker2):
    return newline.strip() == speaker1 and Speaker == speaker2
#use function when there's a repeating pattern
while y < linecount:
    newline=(interview.readline())
    if isSpeaker('I:', 'P:'):
        Speaker = 'I:'
        formatted_interview += '''\nI: '''
    elif isSpeaker('I:', 'I:'):
        Speaker = 'I:'
    elif isSpeaker('P:', 'I:'):
        Speaker = 'P:'
        formatted_interview += '''\nP: '''
    elif isSpeaker('P:', 'P:'):
        Speaker = 'P:'
    else:
        formatted_interview += newline.strip() + ''' '''
    y+=1
print(formatted_interview)

#Input:
''' 
 Speaker 2 

Interview statement 1.

 Speaker 2 

Interview statement 2.

 Speaker 2 

Interview statement 3.
'''
#Output:

''' 
Speaker 2: Interview statement 1. Interview statement 2. Interview statement 3.
'''