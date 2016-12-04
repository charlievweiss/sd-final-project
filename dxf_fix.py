import ezdxf
dwg = ezdxf.readfile("Board_Core.dxf")


def flatten(c):
  (x,y,z) = c
  return (x*z/abs(z), y, 0)


def mirror(a):
  a = 180-a
  if a < 0:
    a = a+360
  return a


for e in dwg.entities:
  if e.dxftype()=="CIRCLE":
    e.dxf.center = flatten(e.dxf.center)
  elif e.dxftype()=="ARC":
    (x,y,z) = e.dxf.center
    if z < 0:
      start_angle = e.dxf.start_angle
      end_angle = e.dxf.end_angle
      e.dxf.start_angle = mirror(end_angle)
      e.dxf.end_angle = mirror(start_angle)
    e.dxf.center = flatten(e.dxf.center)


dwg.saveas("core_output.dxf")
