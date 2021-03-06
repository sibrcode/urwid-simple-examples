#!/usr/bin/env python3

# text_in_frame.py
#
# One of several simple Urwid examples.
# Embed some Text objects in a Frame object. We'll also add a Text
# object to the header, and some Text objects in a Column object,
# and add that in to Frame's footer.

import urwid

palette = [
    ('titlebar', 'dark red', ''),
    ('bold', 'white,bold', '')]

header_text = urwid.Text (('titlebar',u"Ctrl-C to cancel"),align='center')
body_text1 = urwid.Text (u"Body text is in this part over here.")
body_text2 = urwid.Text (u"Second line.")

# For the footer, we get a bit fancy and add in some columns.
footer_columns = urwid.Columns (
	[urwid.Text (u"Column 1"), urwid.Text (u"Column 2"), urwid.Text (u"Column 3")],
	dividechars=1
)

# Must wrap the "flow" object in a "box" object in order for it
# to be in the body of a Frame.
body_filled = urwid.Filler (
	body_text1,
	valign='top'
)

# We'll use a Frame object to combine header, body, and footer.
# The header & footer are expected to be flow objects.
layout= urwid.Frame (
	body_filled,
	header=header_text,
	footer=footer_columns
)

loop = urwid.MainLoop(layout, palette)
loop.run()

