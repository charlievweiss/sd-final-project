"""
SolidpythonProgram that draws a hexagon of given dimensions
"""
from solid import *
from solid.utils import *
import os, sys
import math



def hexdraw(insize,outsize):
        SEGMENTS = 400
        #outsize is tip to tip distance of outer hexagon
        flatflat = outsize*math.sqrt(3)/2.0 #outsize * sqrt3/2 = flat to flat distance
        out_dir = sys.argv[1] if len(sys.argv) > 1 else os.curdir
        file_out = os.path.join(out_dir, 'temp.scad')
        #basic_geometry = import_('Core_Export_New.dxf')
        basic_geometry = circle(3000)
        for i in range(0,30):
                #go right then draw another column
                leftdist =flatflat*i*.75
                for i in range(0,30):
                        Hexagon1 = left(leftdist)(forward(outsize*i*.5)(circle(insize)))
                        Hexagon1.add_param('$fn',6) # make hexagonal
                        basic_geometry = difference()(basic_geometry, Hexagon1)
        scad_render_to_file(basic_geometry, file_out, file_header='$fn = %s;'%SEGMENTS)
        export_name = "board"
        filenum = 0
        filename = "board" + str(filenum) + ".dxf"
        #figure out what to name generated file
        while os.path.isfile(filename):
                filenum += 1
                filename = "board" + str(filenum) + ".dxf"
        commandlinearg = 'openscad -o ' + filename+ ' temp.scad'
        os.system(commandlinearg)
        return filename

hexdraw(20,50)
