
from solid import *
from solid.utils import *
import os, sys
import math



def hexdraw(insize,outsize):
        """Given a tip-to-tip size of inner and outer hexagons in lightweighting pattern(insize and outsize respectively)
        generates .DXF file of skateboard and returns name of .DXF
        """
        #sets path out for generated DXF files to be in static
        os.chdir('static')
        #sets path out for generated OpenScad file to temp.scad in static
        out_dir = os.getcwd()
        file_out = os.path.join(out_dir, 'temp.scad')
        core = import_('Core.dxf') #Import core
        flatflat = outsize*math.sqrt(3)/2.0 # outsize is tip to tip distance of outer hexagon, outsize * sqrt3/2 = flat to flat distance
        #Draw and subtract one grid of hexagons
        for i in range(-10,10):
                #go left then draw another column
                leftdist=outsize*1.5*i+outsize*.75
                #Draw a column of hexagons
                for i in range(-10,10):
                        Hexagon2 = left(leftdist)(forward((flatflat*i+flatflat/2))(circle(insize/2)))
                        Hexagon2.add_param('$fn',6) # make hexagonal
                        core = difference()(core, Hexagon2)
        #Draw and subtract half offset grid to make lightweighting pattern
        for i in range(-10,10):
                #go left
                leftdist=outsize*1.5*i
                #Draw a column of hexagons
                for i in range(-10,10):
                        Hexagon1 = left(leftdist)(forward(flatflat*i)(circle(insize/2)))
                        Hexagon1.add_param('$fn',6) # make hexagonal
                        core = difference()(core, Hexagon1)
        #combine lightweighted core, board outer profile, and truck attachment points to make skateboard
        outside= import_('Outside.dxf')
        trucks= import_('Trucks.dxf')
        basic_geometry = core + outside + trucks
        SEGMENTS = 400 #Resolution setting for OpenScad
        scad_render_to_file(basic_geometry, file_out, file_header='$fn = %s;'%SEGMENTS)
        filenum = 0 #default start file number
        filename = "board" + str(filenum) + ".dxf" #default file name
        #figure out what to name generated file based on existing files (takes lowest available number)
        while os.path.isfile(filename):
                filenum += 1
                filename = "board" + str(filenum) + ".dxf"
        #export dxf
        os.system('openscad -o ' + filename+ ' temp.scad')
        return filename

