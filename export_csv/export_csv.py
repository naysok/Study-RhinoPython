import csv



### set data
list = []
for i in xrange(10):
    sub_list = []
    for j in xrange(10):
        # sub_list.append(str(i) + "," + str(j))
        sub_list.append(i * j)
    list.append(sub_list)


### export csv
path = "C://Users//yoshioca//Documents//Study-RhinoPython//export_csv//"
name = "export_csv.csv"
filename = path + name

with open(filename, 'w') as f:
    writer = csv.writer(f)
    writer.writerows(list)




### result

"""
"0,0","0,1","0,2","0,3","0,4","0,5","0,6","0,7","0,8","0,9"
"1,0","1,1","1,2","1,3","1,4","1,5","1,6","1,7","1,8","1,9"
"2,0","2,1","2,2","2,3","2,4","2,5","2,6","2,7","2,8","2,9"
"3,0","3,1","3,2","3,3","3,4","3,5","3,6","3,7","3,8","3,9"
"4,0","4,1","4,2","4,3","4,4","4,5","4,6","4,7","4,8","4,9"
"5,0","5,1","5,2","5,3","5,4","5,5","5,6","5,7","5,8","5,9"
"6,0","6,1","6,2","6,3","6,4","6,5","6,6","6,7","6,8","6,9"
"7,0","7,1","7,2","7,3","7,4","7,5","7,6","7,7","7,8","7,9"
"8,0","8,1","8,2","8,3","8,4","8,5","8,6","8,7","8,8","8,9"
"9,0","9,1","9,2","9,3","9,4","9,5","9,6","9,7","9,8","9,9"

0,0,0,0,0,0,0,0,0,0
0,1,2,3,4,5,6,7,8,9
0,2,4,6,8,10,12,14,16,18
0,3,6,9,12,15,18,21,24,27
0,4,8,12,16,20,24,28,32,36
0,5,10,15,20,25,30,35,40,45
0,6,12,18,24,30,36,42,48,54
0,7,14,21,28,35,42,49,56,63
0,8,16,24,32,40,48,56,64,72
0,9,18,27,36,45,54,63,72,81
"""