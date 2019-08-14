#include <X11/Xlib.h>
#include <X11/keysym.h>
#include <stdio.h>
#include <stdlib.h>

int screen;
Display *dpy;
Window root;

void grabkeys(void)
{
  {
    KeyCode code;
    
    XUngrabKey(dpy, AnyKey, AnyModifier, root);
    code = XKeysymToKeycode(dpy, XK_p);
    XGrabKey(dpy, code, Mod1Mask, root, True, GrabModeAsync, GrabModeAsync);
  }
}

void setup(void)
{
  dpy = XOpenDisplay(NULL);
  XSetWindowAttributes wa;
  screen = DefaultScreen(dpy);
  root = RootWindow(dpy, screen);
  wa.event_mask = ButtonPressMask;
  XChangeWindowAttributes(dpy, root, CWEventMask|CWCursor, &wa);
  XSelectInput(dpy, root, wa.event_mask);
  grabkeys();
}

void run (void)
{
  XEvent ev;
  XSync(dpy, False);
  while (!XNextEvent(dpy, &ev)){
    printf("next event\n");
  }
}

int main()
{
 
  setup();
  /* close connection to server */
  XCloseDisplay(dpy);

  return 0;
  
}
