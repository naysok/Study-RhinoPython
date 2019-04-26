import rhinoscriptsyntax as rs


### rs.GetInteger(msg, defalut, min, max)
tmp_num_0 = rs.GetInteger("Please Enter an Integer-A", 10, 0, 100)
tmp_num_1 = rs.GetInteger("Please Enter an Integer-B", 2)

print "Integer-A + Interger-B =", tmp_num_0 + tmp_num_1



### rs.GetString(msg, defalut)
tmp_txt = rs.GetString("Please Enter Your Name", "aaa")

print "Hello,", tmp_txt
