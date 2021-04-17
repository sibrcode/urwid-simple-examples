#!/usr/bin/env python3

# buttons_in_gridflow.py
#
# One of several simple Urwid examples.
# Add some buttons to a Frame object, using a Pile object to stack them vertically.

import urwid

# A really basic palette of markup.
palette = [
    ('titlebar', 'dark red', ''),
    ('bold', 'standout', '')
]

text_header = urwid.Text (('titlebar', "Press Ctrl-C to exit\n"), align='center')

def click_handler (button):
	 """Clear any highlighting on previous button (we don't know which),
	 and add highlight to the button just clicked."""
	
	for btn in BUTTON_LIST:
		if btn == button:
			btn.set_label (('bold', btn.get_label()))
		else:
			btn.set_label (btn.get_label())

# A global that will be referenced by click_handler.
BUTTON_LIST = [
	urwid.Button (u"Button 1", click_handler),
	urwid.Button (u"Button 2", click_handler),
	urwid.Button (u"Button 3", click_handler)
]


# We'll combine the RadioButton objects in a GridFlow object, which will pack
# them as closely as possible.

body_gridflow = urwid.GridFlow(
	BUTTON_LIST,
	30,
	4,
	1,
	'center'
)

# The frame we use later must have a box object for its body.
body_filled = urwid.Filler(
	body_gridflow,
	height='pack',
	valign='top'
)

layout = urwid.Frame(
	body_filled,
	header=text_header
)


loop = urwid.MainLoop(layout, palette)
loop.run()



