$fn = 400;

difference() {
	color(c = [0.8500000000, 0.7000000000, 0.4500000000], $fn = 6) {
		circle(r = 90);
	}
	color(c = [0.8500000000, 0.7000000000, 0.4500000000], $fn = 6) {
		circle(r = 60);
	}
}
/***********************************************
******      SolidPython code:      *************
************************************************
 
ó
¡z@Xc           @   s   d  Z  d   Z d S(   s=   
SolidpythonProgram that draws a hexagon of given dimensions
c         B   sg  d d l  Td d l Td d  l } d d  l } d } e e  e d   } | j d d  e e  e d   } | j d d  e   | |  } e	 | j
  d k r¶ | j
 d n | j } | j j | d	  }	 | }
 e |
 |	 d
 d | d } d } d e |  d } x4 | j j |  rG| d 7} d e |  d } qWd | d } | j |  | S(   Niÿÿÿÿ(   t   *i  iZ   s   $fni   i<   i   s	   temp.scadt   file_headers	   $fn = %s;t   boardi    s   .dxfs   openscad -o s
    temp.scad(   t   solidt   solid.utilst   ost   syst   colort   Pinet   circlet	   add_paramt
   differencet   lent   argvt   curdirt   patht   joint   scad_render_to_filet   strt   isfilet   system(   t   insizet   outsizeR   R   t   SEGMENTSt   Hexagon1t   Hexagon2t   difft   out_dirt   file_outt   basic_geometryt   export_namet   filenumt   filenamet   commandlinearg(    (    s'   /home/arpan/sd-final-project/hexdraw.pyt   hexdraw   s,    

+
N(   t   __doc__R"   (    (    (    s'   /home/arpan/sd-final-project/hexdraw.pyt   <module>   s    
 
***********************************************/
                            
