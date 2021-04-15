import urwid

# A really basic palette of markup.
palette = [
    ('titlebar', 'dark red', ''),
    ('bold', 'white,bold', '')
]

text_header = urwid.Text (('titlebar', "header text here"))

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

layout = urwid.Frame(body_listbox, header=text_header)

urwid.MainLoop(layout, palette).run()

