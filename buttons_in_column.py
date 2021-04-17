#!/usr/bin/env python3

# buttons_in_column.py
#
# One of several simple Urwid examples.
# Add some buttons to a Frame object, using a Pile object to stack them vertically.
#
# FYI, There are some nicer looking examples of buttons here:
#	http://urwid.org/tutorial/index.html  (under Simple Menu)
#	https://stackoverflow.com/questions/52252730/how-do-you-make-buttons-of-the-python-library-urwid-look-pretty

import urwid

# A really basic palette of markup.
palette = [
    ('titlebar', 'dark red', ''),
    ('plain', '', ''),
    ('highlight', 'black', 'dark blue'),
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

# We'll combine the Button objects in a Column object, stacking the buttons
# horizontally. Previously this was a Pile to stack vertically, but then the
# buttons would expand to the full width of the window.

body_columns = urwid.Columns (
	BUTTON_LIST,
	dividechars=8
)

# The frame we use later must have a box object for its body.
body_filled = urwid.Filler(
	body_columns,
	height='pack',
	valign='top'
)

layout = urwid.Frame(
	body_filled,
	header=text_header
)


loop = urwid.MainLoop(layout, palette)
loop.run()



