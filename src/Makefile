#Examples of how to grab keys in the X server

include config.mk

main: main.c
	gcc -Wall main.c -o xreadkeys -lX11

readkeys: xreadkeys.c
	gcc -Wall xreadkeys.c -o xreadkeys2 -lX11


example: example-stack.c
	gcc -Wall example-stack.c -o example-stack -lX11


install:
	cp ${MAIN} ${PREFIX}/bin/xhotkeys
	chmod 755 ${PREFIX}/bin/xhotkeys


.PHONY: install

