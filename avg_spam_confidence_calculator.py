# Input file name with spam values
fname = input("Enter file name: ")
fh = open(fname)
s = 0.0000000000000000
c = 0
for line in fh:
    s = s + float(line)
    c = c + 1
print("Average spam confidence: " + str(s/float(c)))
