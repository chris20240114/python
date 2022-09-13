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