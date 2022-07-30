with open(r"/Users/christopher/Downloads/Document36.txt", 'r') as fp:
    linecount = len(fp.readlines())

interview = open("/Users/christopher/Downloads/Document36.txt", "r")

y=0
formatted_interview = [ ]
Speaker = ''
isTrue = False
while y < 1:
    newline=(interview.readline())
    if newline.strip() == "Audio file":
        Speaker = 'I:'
        formatted_interview.append('I: ')
        isTrue = True
    y+=1
print(newline)
print(formatted_interview)
print(isTrue)
print(len(newline))