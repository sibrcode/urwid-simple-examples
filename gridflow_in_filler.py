#!/usr/bin/env python3

# gridflow_in_filler.py
#
# One of several simple Urwid examples.
# Show a mix of buttons and text objects in a GridFlow based window.

import urwid
import urwid.curses_display

PALETTE = [
    ('normal', '', ''),
    ('bold', 'bold', ''),
    ('blue', 'bold', 'dark cyan'),
    ('highlight', 'white', 'dark blue'),
]

class PlainButton (urwid.Button):
	# Override the defaults.
	button_left = urwid.Text('')
	button_right = urwid.Text('')

	def set_text(self, label):
		"""set_text is invoked by Button.set_label"""
		self.__super.set_text(label)
		# Trick to  hide cursor.
		self._cursor_position = len(label) + 1

class TextItem (urwid.Text):
	
	def selectable(self):
		return False


class BoxButton(urwid.WidgetWrap):
	
	def __init__(self, label, on_click):
		label_widget = urwid.Text(label, align='center')
		self.widget = urwid.LineBox(label_widget)
		self.hidden_button = urwid.Button('hidden button', on_click)
		super(BoxButton, self).__init__(self.widget)

	def selectable(self):
		return True

	def keypress(self, *args, **kwargs):
		return self.hidden_button.keypress(*args, **kwargs)

	def mouse_event(self, *args, **kwargs):
		return self.hidden_button.mouse_event(*args, **kwargs)


def box_button(*args, **kwargs):
    b = BoxButton(*args, **kwargs)
    b = urwid.AttrMap(b, '', 'highlight')
    #b = urwid.Padding(b, left=4, right=4)
    return b

footer = urwid.Text ('')
onclick = lambda w: footer.set_text('clicked: %r' % w)


a = urwid.AttrMap (TextItem (u"Text A"), '', 'highlight')
b = urwid.AttrMap (PlainButton (u"Button B", on_press=onclick), '', 'highlight')
c = urwid.AttrMap (PlainButton (u"Button C", on_press=onclick), '', 'highlight')


# Create a Screen object that uses the OS's ncurses instead of Urwid's
# default of using the Python based raw_display.
screen = urwid.curses_display.Screen()

# Add the Text and Button objects to a new GridFlow object.
grid = urwid.GridFlow([a,b,c, footer], cell_width=36, h_sep=2, v_sep=1, align='left')
grid.focus_position = 1 # Select first button by default

fill = urwid.Filler(grid, 'top')

loop = urwid.MainLoop(fill,PALETTE,screen=screen)

loop.run()
