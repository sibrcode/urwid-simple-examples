#!/usr/bin/env python3

# gridflow_in_frame.py
#
# One of several simple Urwid examples.
# Text objects are embedded into a GridFlow object so that they will adjust their position
# based on available width of screen. The GridFlow object object must then be put in a box
# widget. Finally, we add the Fill object to a Frame, and add some Text to its header.

import urwid

# A really basic palette of markup.
palette = [
    ('titlebar', 'dark red', ''),
    ('bold', 'standout', '')
]

# Centered text for use with the Frame's header.
text_header = urwid.Text (('titlebar', "Press Ctrl-C to exit\n"), align='center')

# The Text objects we'll put in the GridFlow object.
body_text1 = urwid.Text (u"Column 1 body text here.")
body_text2 = urwid.Text (u"We need extra lines (rows) for this text block #2 because it is over 30 characters.")
body_text3 = urwid.Text (('bold', u"Block #3 with emphasis."))

# We'll combine the Text objects in a GridFlow object, which will pack
# the blocks of text as closely as possible.
# The GridFlow parameters are:
#	cells, cell_width, h_sep, v_sep, align

body_gridflow = urwid.GridFlow(
	[body_text1, body_text2, body_text3],
	30,
	4,
	1,
	'center'
)

# The frame we use later requires a box object for its body.
body_filled = urwid.Filler(
	body_gridflow,
	height='pack',
	valign='top'
)

layout = urwid.Frame(
	body_filled,
	header=text_header
)

urwid.MainLoop(layout, palette).run()
