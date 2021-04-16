#!/usr/bin/env python3

# text_in_filler.py
#
# One of several simple Urwid examples.
# Shows how to use a Filler object to enclose a Text object.

import urwid

palette = [
    ('title', 'dark red', ''),
    ('bold', 'white,bold', '')]

# Create a Text object from two strings and formatting tag.
body_text = urwid.Text ([
	u"Body text is here.\n\n",
	('title', u"Press Ctrl-C to exit") ],
	align='center'
)

# Must wrap the "flow" object in a "box" object.
body_filled = urwid.Filler (body_text)

loop = urwid.MainLoop(body_filled, palette)
loop.run()

