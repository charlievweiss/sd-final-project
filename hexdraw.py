
from solid import *
from solid.utils import *
import os, sys
import math



def hexdraw(insize,outsize):
        """Given a tip-to-tip size of inner and outer hexagons(insize and outsize respectively)
        generates .DXF file of skateboard and returns path to .DXF
        """
        SEGMENTS = 400 #Resolution setting for OpenScad
        flatflat = outsize*math.sqrt(3)/2.0 # outsize is tip to tip distance of outer hexagon, outsize * sqrt3/2 = flat to flat distance
        print flatflat
        #sets path out for generated OpenScad file to temp.scad in current directory
        os.chdir('static')
        out_dir = os.getcwd()
        file_out = os.path.join(out_dir, 'temp.scad')
        core = import_('Core.dxf') #Import core 
        #Draw one grid of hexagons
        for i in range(-10,10):
                #go right then draw another column
                leftdist=outsize*1.5*i+outsize*.75
                for i in range(-10,10):
                        Hexagon2 = left(leftdist)(forward((flatflat*i+flatflat/2))(circle(insize/2)))
                        Hexagon2.add_param('$fn',6) # make hexagonal
                        core = difference()(core, Hexagon2)
        #Draw half offset grid to make hexmesh
        for i in range(-10,10):
                #go right then draw another column
                leftdist=outsize*1.5*i
                for i in range(-10,10):
                        Hexagon1 = left(leftdist)(forward(flatflat*i)(circle(insize/2)))
                        Hexagon1.add_param('$fn',6) # make hexagonal
                        core = difference()(core, Hexagon1)
        outside= import_('Outside.dxf')
        trucks= import_('Trucks.dxf')
        basic_geometry = core + outside + trucks
        scad_render_to_file(basic_geometry, file_out, file_header='$fn = %s;'%SEGMENTS)
        filenum = 0
        filename = "board" + str(filenum) + ".dxf"
        #figure out what to name generated file
        while os.path.isfile(filename):
                filenum += 1
                filename = "board" + str(filenum) + ".dxf"
        commandlinearg = 'openscad -o ' + filename+ ' temp.scad'
        os.system(commandlinearg)
        return filename

hexdraw(20,30)
