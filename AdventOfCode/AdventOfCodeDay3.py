

file = open('input.txt')
file2 = open('input.txt')

contents = file.read().strip('\n').strip().replace('\n','')
contents2 = file2.read().strip().split('\n')[::2]
count = 0


try:
    for line in range(len(contents)):
        step_index = 1
        s = ((line + (31 * step_index)) * (step_index)) % 31
        s2 = (line * 31) + 3
        letter = contents2[line]
        editedLine = letter.strip()
        line_me = ''
        for char in range(len(editedLine)):
            if char == s:
                if editedLine.strip()[char] == '#':
                    line_me += 'O'
                    count += 1
                else:
                    line_me += 'X'
            else:
                line_me += editedLine[char]
        print(str(line) + ': ' + line_me)

except Exception as e:
    print(e)

print(count)
#print(contents)

