#!/bin/bash 

cd ../bin
if [ -f "libhitbox.so" ]; 
then
rm "libhitbox.so"
fi

gcc -fPIC -g -c ../src/hitbox.c -o hitbox.o
gcc -shared hitbox.o -o libhitbox.so

