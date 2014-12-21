#!/usr/bin/env python

# toolbar_issue00.py - illustrates a problem with the radiance e19 theme
#                       Disabling and then re-enabling a 
#                       toolbar item breaks it's functionality
#
# python-efl version 1.10  tested under Bodhi linux 3.0rc unstable

# Copyright 2014 ylee@bodhilinux.com
#
# This work is free. You can redistribute it and/or modify it under the
# terms of the Do What The Fuck You Want To Public License, Version 2,
# as published by Sam Hocevar. See http://www.wtfpl.net/ for more details.


from efl.evas import EVAS_HINT_EXPAND, EVAS_HINT_FILL
from efl import elementary
from efl.elementary.box import Box
from efl.elementary.button import Button
from efl.elementary.label import Label
from efl.elementary.panel import Panel, ELM_PANEL_ORIENT_TOP
from efl.elementary.popup import Popup
from efl.elementary.toolbar import Toolbar, ELM_OBJECT_SELECT_MODE_DEFAULT
from efl.elementary.window import StandardWindow

EXPAND_BOTH = EVAS_HINT_EXPAND, EVAS_HINT_EXPAND
EXPAND_HORIZ = EVAS_HINT_EXPAND, 0.0
FILL_BOTH = EVAS_HINT_FILL, EVAS_HINT_FILL


class Interface(object):

    def __init__(self):
        self.win = StandardWindow("test", "Toolbar_issue",
            size=(600, 400))
        self.win.callback_delete_request_add(lambda x: elementary.exit())

        box0 = Box(self.win)
        #, size_hint_weight=EXPAND_HORIZ, size_hint_align=FILL_BOTH)
        self.win.resize_object_add(box0)
        box0.show()

        tb = Toolbar(self.win, homogeneous=True,
                size_hint_weight=EXPAND_HORIZ, size_hint_align=(EVAS_HINT_FILL, 0.0),
                select_mode=ELM_OBJECT_SELECT_MODE_DEFAULT)
        self.menuItem = tb.item_append("document-save", "Save", self.popup)
        tb.show()
        box0.pack_end(tb)

        lb = Label(self.win) 
        lb.text_set("<br>This is a test program to illustrate a problem <br>"
                    "with the Radiance e19 theme.<br><br>"
                    "Disabling a toolbar item and then re-enabling it does not<br>"
                    "re-enable the toolbar item's <i>callback function</i>.<br><br>"
                    "To test this first click <b>Save</b> when this program is opened<br>"
                    "This opens a popup as expected. Dismiss popup.<br><br>"
                    "Now click the <b>Toggle</b> button to disable <b>Save</b> Toolbar Item<br>"
                    "After this the <b>Save</b> button is disabled and 'looks different'<br><br>"
                    "Click the <b>Toggle</b> button again to enable <b>Save</b><br>"
                    "After this clicking <b>Save</b> does nothing even tho it 'looks' enabled<br><br>"
                    )
        lb.show()
        box0.pack_end(lb)

        testButton = Button(self.win, text="Toogle")
        testButton.callback_clicked_add(self.disable)
        testButton.show()
        box0.pack_end(testButton)

        self.win.show()

    def popup(self, tb, it):
        msg = Popup(self.win, size_hint_weight=EXPAND_BOTH, text="Save Clicked")
        msg.callback_block_clicked_add(self.closePopup)
        msg.show()
        it.selected_set(False)

    def closePopup(self, obj):
        obj.delete()

    def disable(self, obj):
        self.menuItem.disabled_set(not self.menuItem.disabled)


if __name__ == "__main__":

    elementary.init()
    GUI = Interface()
    elementary.run()
