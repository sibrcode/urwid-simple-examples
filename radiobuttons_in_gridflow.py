#!/usr/bin/env python3

# text_in_frame.py
#
# One of several simple Urwid examples.
# Embed some Text objects in a Frame object. We'll also add a Text
# object to the header, and some Text objects in a Column object,
# and add that in to Frame's footer.

import urwid

# A really basic palette of markup.
palette = [
    ('titlebar', 'dark red', ''),
    ('bold', 'standout', '')
]

text_header = urwid.Text (('titlebar', "Press Ctrl-C to exit\n"), align='center')

button_group = []

button_1 = urwid.RadioButton (button_group, u"Radio 1")
button_2 = urwid.RadioButton (button_group, u"Radio 2")
button_3 = urwid.RadioButton (button_group, u"Radio 3")

# We'll combine the RadioButton objects in a GridFlow object, which will pack
# them as closely as possible.

body_gridflow = urwid.GridFlow(
	button_group,
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



