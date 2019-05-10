import rhinoscriptsyntax as rs



def add_cube_w_material(count):

    for i in xrange(count):
        for j in xrange(count):


            ### define pt, plane
            tmp_pt = rs.AddPoint(i * 2, j * 2, 0)
            tmp_pln = rs.PlaneFromPoints(tmp_pt,
            rs.PointAdd(tmp_pt, (1,0,0)), rs.PointAdd(tmp_pt, (0,1,0)))


            ### define extrude line
            line_ex = rs.AddLine((0,0,0), (0,0,1))


            ### draw rect
            tmp_crv = rs.AddRectangle(tmp_pln, 1,1)
            tmp_surf = rs.AddPlanarSrf(tmp_crv)
            tmp_box = rs.ExtrudeSurface(tmp_surf, line_ex, True)


            ### set color
            rs.AddMaterialToObject(tmp_box)

            index = rs.ObjectMaterialIndex(tmp_box)

            rs.MaterialName(index, str(i) + "_" +str(j))
            rs.MaterialColor(index,  ((255 / count) * i, 255 - ((255 / count) * j), 255 - ((255 / count) * j)))

            # name = rs.MaterialName(index)
            # print name


            ### delete
            rs.DeleteObject(tmp_pt)
            rs.DeleteObject(tmp_crv)
            rs.DeleteObject(tmp_surf)
            rs.DeleteObject(line_ex)





add_cube_w_material(5)