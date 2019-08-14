from Xlib import X
from Xlib.display import Display
from Xlib.keysymdef import xf86
from subprocess import run


actions = {
    xf86.XK_XF86_AudioPlay: ['playerctl', 'play-pause'],
    xf86.XK_XF86_AudioStop: ['playerctl', 'stop'],
    xf86.XK_XF86_AudioNext: ['playerctl', 'next'],
    xf86.XK_XF86_AudioPrev: ['playerctl', 'previous']
}


# int XGrabKeyboard(display, grab_window, owner_events, pointer_mode, keyboard_mode, time)
#       Display *display;
#       Window grab_window;
#       Bool owner_events;
#       int pointer_mode, keyboard_mode;
#       Time time;


# XGrabKey(display, keycode, modifiers, grab_window, owner_events, pointer_mode, 
#              keyboard_mode)
#       Display *display;
#       int keycode;
#       unsigned int modifiers;
#       Window grab_window;
#       Bool owner_events;
#       int pointer_mode, keyboard_mode;

# Arguments
# display	Specifies the connection to the X server.
# keycode	Specifies the KeyCode or AnyKey.
# modifiers	Specifies the set of keymasks or AnyModifier. The mask is the bitwise inclusive OR of the valid keymask bits.
# grab_window	Specifies the grab window.
# owner_events	Specifies a Boolean value that indicates whether the keyboard events are to be reported as usual.
# pointer_mode	Specifies further processing of pointer events. You can pass GrabModeSync or GrabModeAsync.
# keyboard_mode	Specifies further processing of keyboard events. You can pass GrabModeSync or GrabModeAsync.

def bind_actions(dpy, window, action_dct):
    for keysym in action_dct:
        keycode = dpy.keysym_to_keycode(keysym)
        window.grab_key(keycode, X.AnyModifier, False, X.GrabModeAsync, X.GrabModeAsync)        

        
def process(dpy, actions, evt):
    if evt.type == X.KeyRelease:
        keycode = evt.detail
        mod = evt.state
        keysym = dpy.keycode_to_keysym(keycode, mod)
        if keysym in actions:
            do_action(actions[keysym])
        else:
            print('Keysym:', keysym, 'modifier', mod)


def do_action(action):
    run(action)


def setup() -> Display:
    dpy = Display()
    s = dpy.screen()
    root = s.root
    bind_actions(dpy, root, actions)
    return dpy


def loop(dpy: Display, actions: dict):
    try:
        for _ in range(5):
            evt = dpy.next_event()
            process(dpy, actions, evt)
    finally:
        dpy.close()


def main(argv):
    dpy = setup()
    loop(dpy)
    return 0


if __name__ == '__main__':
    from sys import exit, argv
    exit(main(argv))
