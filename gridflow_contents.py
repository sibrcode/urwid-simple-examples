#!/usr/bin/env python3

# gridflow_contents.py
#
# One of several simple Urwid examples.
# Based on one of the other GridFlow examples, but in this case
# shows how you can modify the contents of a previously created
# GridFlow object.

import datetime, urwid

# A really basic palette of markup.
palette = [
    ('titlebar', 'dark red', ''),
    ('bold', 'standout', '')
]

# Centered text for use with the Frame's header.
text_header = urwid.Text (('titlebar', "Press Ctrl-C to exit\n"), align='center')

# The Text objects we'll put in the GridFlow object.
# The last object we'll replace with the current time.
body_text1 = urwid.Text (u"Column 1 body text here.")
body_text2 = urwid.Text (u"We need extra lines (rows) for this text block #2 because it is over 30 characters.")
body_text3 = urwid.Text (('bold', u""))

# We'll combine the Text objects in a GridFlow object, which will pack

GRIDFLOW = urwid.GridFlow(
	[body_text1, body_text2, body_text3],
	30,
	4,
	1,
	'center'
)

# The frame we use later requires a box object for its body.
body_filled = urwid.Filler(
	GRIDFLOW,
	height='pack',
	valign='top'
)

layout = urwid.Frame(
	body_filled,
	header=text_header
)

def handle_alarm(self, loop=None, user_data=None):
	"""Update the time text, and set alarm for one second in future."""

	global GRIDFLOW, LOOP
	
	time_string = datetime.datetime.now().strftime("%H:%M:%S")
	time_text = urwid.Text (time_string)
	cell_width = 60
	
	# Update the contents of the last cell.
	# To add it directly like this we must append the
	# width setting (eg, given width) and the cell width
	# as part of tuple of values.
	
	GRIDFLOW.contents [2] = (time_text, ('given', cell_width))
	
	# Set the alarm for the next update to call ourselves.
	alarm_handler = LOOP.set_alarm_in (
		1, handle_alarm
	)

LOOP = urwid.MainLoop(layout, palette)

# Prime the alarm used to set time.
LOOP.set_alarm_in (
	1, handle_alarm
)

LOOP.run()
