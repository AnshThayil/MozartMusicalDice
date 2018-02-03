import random
import webbrowser
file = open("getmeasures.txt")
text = file.readlines()
measures = []
for i in text:
    arr = i.split()
    rand = random.randint(1,11)
    measures.append(arr[rand - 1])

file2 = open("notes.txt")
text2 = file2.readlines()
output = open("output.txt", 'w+')

output.truncate()
print(measures)
measurecount = 0
for j in measures:
    for i in text2:
        arr = i.split()
        beat = arr[1]
        if float(beat) >= ((float(j)*3) - 3) and float(beat) < (float(j)*3):
            arr[1] = str((float(beat) - ((float(j)*3) - 3)) + (measurecount*3))
            arr.append('\n')
            i = " ".join(arr)
            output.write(i)
    measurecount += 1
file.close()
file2.close()
output.close()
webbrowser.open('output.txt')
webbrowser.open('listen.html')
