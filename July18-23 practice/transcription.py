with open(r"/Users/christopher/Downloads/Document36.txt", 'r') as fp:
    linecount = len(fp.readlines())

interview = open("/Users/christopher/Downloads/Document36.txt", "r")

y=0
formatted_interview = ''''''
Speaker = 'P:'
while y < linecount:
    newline=(interview.readline())
    if newline.strip() == 'I:' and Speaker == 'P:':
        Speaker = 'I:'
        formatted_interview += '''\nI: '''
    elif newline.strip() == 'I:' and Speaker == 'I:':
        Speaker = 'I:'
    elif newline.strip() == 'P:' and Speaker == 'I:':
        Speaker = 'P:'
        formatted_interview += '''\nP: '''
    elif newline.strip() == 'P:' and Speaker == 'P:':
        Speaker = 'P:'
    elif newline.strip() != 'P:' and newline.strip() != 'I:':
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