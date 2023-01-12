//a c demo to use hitboxes with hitbox.h
//compile: gcc hitbox_src/test.c -lm -o bin/hitbox_test


#include <stdio.h>
#include "hitbox.h"


void main(){
	
	printf("Macro in circle:   %d\n",IN_CIRCLE(10,10,100,15,15));
	
	printf("Macro touch Circle:%d\n",TOUCH_CIRCLE(10,10,100,20,30,30));
	printf("Macro in rect:     %d\n",INRECT(25,25,20,20,30,30));
	printf("Macro Touch rect:  %d\n",TOUCH_RECT(10,10,30,30,20,20,40,40));
	
	printf("func get distance:%d\n",get_distance(10,10,30,40));
	printf("func in circle:   %d\n",in_circle(10,10,100,30,30));
	printf("func touch circle:%d\n",touch_circle(10,10,100,20,30,30));
	printf("func in rect:     %d\n",in_rect(25,25,20,20,30,30));
	printf("func in rect:     %d\n",touch_rect(10,10,30,30,20,20,40,40));
	
}
