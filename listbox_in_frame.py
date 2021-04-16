#!/usr/bin/env python3

# text_in_filler.py
#
# One of several simple Urwid examples.
# Very simple ListBox example.

import urwid
import urwid.curses_display

# A really basic palette of markup.
palette = [
    ('titlebar', 'dark red', ''),
    ('bold', 'white,bold', '')
]

# Header text + blank line for spacing.
text_header = urwid.Text (('titlebar', "Ctrl-C to exit\n"))

body_text1 = urwid.Text (u"Body text is in this part over here.")
body_text2 = urwid.Text (u"We need an extra line for this example.")
body_text3 = urwid.Text (('bold', u"And another line in bold just be sure."))

# A frame's body must be a box object.
# We'll use the ListBox object here to combine the Text objects
body_listbox = urwid.ListBox(
	urwid.SimpleListWalker(
		[body_text1, body_text2, body_text3]
	)
)

# Create a Screen object that uses the OS's ncurses instead of Urwid's
# default of using the Python based raw_display.

screen = urwid.curses_display.Screen()

# Setup the object to display on screen
layout = urwid.Frame(body_listbox, header=text_header)

# Create the event loop, specifying the ncurses based screen we created earlier.
loop = urwid.MainLoop (
	layout,
	palette,
	screen=screen
)

loop.run()

