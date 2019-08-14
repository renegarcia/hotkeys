#include <X11/Xlib.h>
#include <X11/keysym.h>
#include <stdio.h>

//https://stackoverflow.com/questions/30994628/why-does-xgrabkey-return-badrequest

int main() {
    Display *d = XOpenDisplay(0);
    Window root = DefaultRootWindow(d);
    int keycode = XKeysymToKeycode(d, XK_BackSpace);

/* XGrabKey(display, keycode, modifiers, grab_window, owner_events, pointer_mode,  */
/*              keyboard_mode) */
/*       Display *display; */
/*       int keycode; */
/*       unsigned int modifiers; */
/*       Window grab_window; */
/*       Bool owner_events; */
/*       int pointer_mode, keyboard_mode; */

/* Arguments */
/* display	Specifies the connection to the X server. */
/* keycode	Specifies the KeyCode or AnyKey. */
/* modifiers	Specifies the set of keymasks or AnyModifier. The mask is the bitwise inclusive OR of the valid keymask bits. */
/* grab_window	Specifies the grab window. */
/* owner_events	Specifies a Boolean value that indicates whether the keyboard events are to be reported as usual. */
/* pointer_mode	Specifies further processing of pointer events. You can pass GrabModeSync or GrabModeAsync. */
/* keyboard_mode	Specifies further processing of keyboard events. You can pass GrabModeSync or GrabModeAsync. */
    
    int rv = XGrabKey(d, keycode, AnyModifier, root, 1, GrabModeAsync, GrabModeAsync);
    printf("XGrabKey returned %d\n", rv);

    XEvent evt;
    while(1) {
        XNextEvent(d, &evt);
        printf("Got event %d\n", evt.type);
    }
}
