
#read file
with open(filename) as f:
    lines = [x for x in f.readlines()]
    f.close()
