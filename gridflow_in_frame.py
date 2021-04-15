import urwid

# A really basic palette of markup.
palette = [
    ('titlebar', 'dark red', ''),
    ('bold', 'standout', '')
]

text_header = urwid.Text (('titlebar', "Press Ctrl-C to exit\n"), align='center')

body_text1 = urwid.Text (u"Column 1 body text here.")
body_text2 = urwid.Text (u"We need extra lines (rows) for this text block #2 because it is over 30 characters.")
body_text3 = urwid.Text (('bold', u"Block #3 with emphasis."))

#width = int((loop.screen.get_cols_rows()[0] - 2) / 3)

# We'll combine the Text objects in a GridFlow object, which will pack
# the blocks of text as closely as possible.

body_gridflow = urwid.GridFlow(
	[body_text1, body_text2, body_text3],
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

urwid.MainLoop(layout, palette).run()
