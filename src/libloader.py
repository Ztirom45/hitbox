#IMPORTEND: this program use a shared obeject file (.so), witch is only avaleble on linux, so that this program only works on linux

#if the program doesn't work:
#make sure that use the right path
#try to recompile the shared obeject file (.so) using compile.sh

from ctypes import *
  
# load the library
path = "/home/usr/Dokumente/Projekte/Hitboxlib/bin/libhitbox.so"
hitbox = cdll.LoadLibrary(path)

hitbox.get_distance.argtype = (c_int,c_int,c_int,c_int)
hitbox.get_distance.restype = c_int

hitbox.in_circle.argtype = (c_int,c_int,c_int,c_int,c_int)
hitbox.in_circle.restype = c_bool

hitbox.touch_circle.argtype = (c_int,c_int,c_int,c_int,c_int,c_int)
hitbox.touch_circle.restype = c_bool

hitbox.in_rect.argtype = (c_int,c_int,c_int,c_int,c_int,c_int)
hitbox.in_rect.restype = c_bool

hitbox.touch_rect.argtype = (c_int,c_int,c_int,c_int,c_int,c_int,c_int,c_int)
hitbox.touch_rect.restype = c_bool
 
if __name__ == "__main__":

	print(hitbox.get_distance(0,10,10,10)) 

	print(hitbox.in_circle(15,10,10,10,10)) 
	print(hitbox.in_circle(0,0,10,10,1))
	
	print(hitbox.touch_circle(0,0,10,10,10,10)) 
	print(hitbox.touch_circle(0,0,1,10,10,1))

	print(hitbox.in_rect(10,10,9,9,15,15)) 
	print(hitbox.in_rect(0,10,10,10,20,20))
	
	print(hitbox.touch_rect(0,0,10,10, 9,9,15,15)) 
	print(hitbox.touch_rect(0,0,10,10,10,10,20,20))



