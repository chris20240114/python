from os import remove
import re
'''
f = open("whereami.in")
inp = f.read().strip().split("\n")
n = int(inp[0])
mailboxes = inp[1]

final = 0
for i in range(1, n+1):
  taken = set()
  valid = True
  for j in range(0, n - i + 1):
    curr = mailboxes[j:j+i]
    if curr in taken:
      valid = False
      break
    taken.add(curr)
  if valid:
    final = i
    break

f = open('whereami.out', 'w')
f.write(str(final))
f.close()
'''


'''
from distutils.filelist import findall
from gettext import find
from mailbox import Mailbox
import re

N = int(input())
s = input().strip()
for k in range(1, N + 1):
    # i is the start position of the string
        for i in range(N - k + 1):
            # sub1 is the substring of the string
            sub1 = s[i:i + k]
            # once the character is shown twice, the second time the find will return an index of the substring where it starts
            location = 0
            for j in range(2):
                location = s[location:].find(sub1)
                # if location is -1, the substring only appears 1 once or never appears
                if location == -1:
                    # continue the start position 'i'
                    break
                location += 1
            else:
                # after 2 searching, substring appears, so we need to break this loop and increase the searching length 'k'
                break
        else:
            # if all the substring with length 'k' is unique, 'k' is the answer.
            print(k)
            break
else:
        # if all the substring appears only once, the length N is the answer.
        print(N)
'''
'''

def Where(N, MailBoxSequence):
    for i in range(0, N):
        substring = MailBoxSequence[i:i+1]
        Matching = MailBoxSequence.findall(substring)
        if len(Matching) == 1:
            break
        elif len(Matching) > 1:
            for i in range(0, N):
                substring = MailBoxSequence[i:i+2]
                Matching = MailBoxSequence.findall(substring)
                if len(Matching) == 1:
                    break
    return 15

String1 = re.compile(r'\w{5}')
Substring1 = String1.findall('ABCDABCDEF')
print(String1.findall('ABCDABCDEF'))

'''


'''
create a substring of the mailboxes. In a for loop, do a re.match() function, and then remove the 
matching sequence from the substring. Check again with the re.match() function, and if there's still an occurance, add
the next mailbox into the substring.
'''

def Where(N, MailBoxSequence):
    testing_substring = ""
    unique_value = 0
    for i in range(0, N):
        temp = MailBoxSequence
        testing_substring += MailBoxSequence[i]
        x= re.search(testing_substring, temp).span()
        while re.search(testing_substring, temp) != None:
            y= re.findall(testing_substring, temp)
            print(y[i])
        print(temp[x[0]:x[1]])
        temp = temp[i+1:len(temp)]
        x= re.search(testing_substring, temp)
        if x == None:
            unique_value = i+1
            return unique_value
        elif x != None:
            continue
    return unique_value

print(Where(9, 'ABABCABCD'))