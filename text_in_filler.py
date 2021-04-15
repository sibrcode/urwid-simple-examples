import urwid

palette = [
    ('titlebar', 'dark red', ''),
    ('bold', 'white,bold', '')]

body_text = urwid.Text (u"Body text is in this part over here.")

# Must wrap the "flow" object in a "box" object.
body_filled = urwid.Filler (body_text)

urwid.MainLoop(body_filled, palette).run()

