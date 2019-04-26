import rhinoscriptsyntax as rs


### GetPoint
tmp_point = rs.GetPoint("Point", (0,0,0))

### Gei width, height
tmp_width = rs.GetReal("Width", 2, 0,10)
tmp_height = rs.GetReal("Height", 3)


### (1) copy, move, define plane, del pt
### Bake
tmp_point_c0 = rs.CopyObject(tmp_point)
tmp_point_c1 = rs.CopyObject(tmp_point)
tmp_plane = rs.PlaneFromPoints(tmp_point, rs.MoveObject(tmp_point_c0, (1,0,0)), rs.MoveObject(tmp_point_c1, (0,1,0)))
tmp_point_x = rs.MoveObject(tmp_point_c0, (1,0,0))
tmp_point_y = rs.MoveObject(tmp_point_c1, (0,1,0))
tmp_plane = rs.PlaneFromPoints(tmp_point, tmp_point_x, tmp_point_y)
rs.DeleteObject(tmp_point_x)
rs.DeleteObject(tmp_point_y)



### (2) pointadd
### OK
#tmp_point_x = rs.PointAdd(tmp_point, (1,0,0))
#tmp_point_y = rs.PointAdd(tmp_point, (0,1,0))
#tmp_plane = rs.PlaneFromPoints(tmp_point, tmp_point_x, tmp_point_y)


tmp_rect = rs.AddRectangle(tmp_plane, tmp_width, tmp_height)