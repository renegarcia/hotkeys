#https://github.com/python-xlib/python-xlib/blob/master/examples/xinput.py

import sys
import os


from Xlib.display import Display
from Xlib.ext import xinput
from Xlib.keysymdef import xf86


def print_hierarchy_changed_event(event):
    print('Event: ', event)
    print('<deviceid=%s time=%s flags=%s info={' % (
        event.data.deviceid,
        event.data.time,
        event.data.flags,
        ))
    #for info in event.data.info:
    #    print_info(info)
    print('}>')


def print_info(info):
    print('  <deviceid=%s attachment=%s type=%s enabled=%s flags=%s>' % (
        info.deviceid,
        info.attachment,
        info.type,
        info.enabled,
        info.flags,
        ))

def handle_key_realease(dpy, evt):
    keycode = evt.data['detail']
    mod = evt.data['mods']['base_mods']
    keysym = dpy.keycode_to_keysym(keycode, mod)
    string = dpy.lookup_string(keysym)
    print('event tyep', evt.type)
    print('key released:', string)
    print('modifieres:', mod)
    print('Raw event', evt)


def stalk(dpy, evt):
    #print(evt)
    keycode = evt.data['detail']
    mod = evt.data['mods']['base_mods']
    keysym = dpy.keycode_to_keysym(keycode, mod)
    string = dpy.lookup_string(keysym)
    if string is not None:
        print(string)
    else:
        print('Keysym:', keysym, 'modifier', mod)


def main(argv):
    display = Display()
    try:
        extension_info = display.query_extension('XInputExtension')
        xinput_major = extension_info.major_opcode

        version_info = display.xinput_query_version()
        print('Found XInput version %u.%u' % (
          version_info.major_version,
          version_info.minor_version,
        ))

        screen = display.screen()
        screen.root.xinput_select_events([
          (xinput.AllDevices, xinput.KeyReleaseMask),
        ])
 
        while True:
            event = display.next_event()
            #handle_key_realease(display, event)
            stalk(display, event)
            #print_hierarchy_changed_event(event)
            #if (
            #  event.type == display.extension_event.GenericEvent
            #  and event.extension == xinput_major
            #  and event.evtype == 11
            #):
            #    print_hierarchy_changed_event(event)

    finally:
        display.close()


if __name__ == '__main__':
    sys.exit(main(sys.argv))
