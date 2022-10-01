f = '5\nABABC'
inp = f.strip().split("\n")
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
print(final)
f = open('whereami.out', 'w')
f.write(str(final))
f.close()

"ABCABCD"

"ABCA" 