# urwid-simple-examples
Easy to understand examples of how to use the Urwid module in Python

Although the repository for Urwid at https://github.com/urwid/urwid/tree/master/examples contains over a dozen examples, plus more in the Tutorial section, I found they were often too complex for me to easily understand how different objects fit together. In particular, Urwid is fairly particular about flow and box objects are combined.

These are simplified illustrations of a few typical Urwid programming patterns.

---

## buttons_in_column.py

Displays three buttons in a Columns object, with handler to highlight the last "clicked" button.

## gridflow_in_frame.py

Displays Text objects that have been added to GridFlow object, which will dynamically arrange the position of the text blocks based on available space. Adjust your terminal window size to see the behavior. 

## listbox_in_frame.py

Adds Text objects to a basic ListBox object, which is itself in a Frame. Also shows using the OS's ncurses terminal interface instead Urwid's default of raw_display.

## radiobuttons_in_gridflow.py

RadioButton objects are added to a GridFlow object.

## text_in_filler.py

This is the simplest example. Just some Text objects inside of a Filler object.

## text_in_frame.py

Shows Text objects centered on the screen using a Filled object.
