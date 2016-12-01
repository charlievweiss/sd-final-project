"""
SolidpythonProgram that draws a hexagon of given dimensions
"""

from solid import *
from solid.utils import *
import os, sys

SEGMENTS = 400

def hexdraw(insize,outsize):
      """given the size of an inner and outer hexagon builds scad and dxf of files
      returns filename"""
      
      Hexagon1 = color(Pine)((circle(90)))
      Hexagon1.add_param('$fn',6) # make hexagonal
      Hexagon2 = color(Pine)((circle(60)))
      Hexagon2.add_param('$fn',6) # make hexagonal
      diff = difference()(Hexagon1, Hexagon2)
      out_dir = sys.argv[1] if len(sys.argv) > 1 else os.curdir
      file_out = os.path.join( out_dir, 'temp.scad')
      basic_geometry = diff
      scad_render_to_file( basic_geometry, file_out, file_header='$fn = %s;'%SEGMENTS)
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



hexdraw(60,90)
