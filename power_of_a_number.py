def pownum(x,y):
    i = 1
    for f in range (y):
        i *= x
    return i

x=2
y=5
print (pownum(x,y)) #should return 32 (2**5)