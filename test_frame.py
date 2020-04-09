#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  test_frame.py
"""
Frame to visualise different icons in a theme.
"""
#
#  Copyright 2020 Dominic Davis-Foster <dominic@davis-foster.co.uk>
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#
# generated by wxGlade 0.9.3 on Tue Apr  7 11:17:23 2020
#

import sys
import wx

sys.path.append("hicolor")
sys.path.append("adwaita")
sys.path.append("humanity")
sys.path.append("suru")
sys.path.append("tango")

from wx_icons_hicolor.test import freedesktop_naming_spec_list
from wx_icons_humanity import wxHumanityIconTheme, wxHumanityDarkIconTheme
from wx_icons_suru import wxSuruIconTheme
from wx_icons_tango import wxTangoIconTheme
from wx_icons_adwaita import wxAdwaitaIconTheme

# begin wxGlade: dependencies
# end wxGlade

# begin wxGlade: extracode
# end wxGlade


class TestFrame(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: TestFrame.__init__
        kwds["style"] = kwds.get("style", 0) | wx.DEFAULT_FRAME_STYLE | wx.MAXIMIZE
        wx.Frame.__init__(self, *args, **kwds)
        self.SetSize((400, 300))
        self.bitmap = wx.StaticBitmap(self, wx.ID_ANY, wx.NullBitmap)
        self.prev_btn = wx.Button(self, wx.ID_ANY, "<<< Previous Icon")
        self.next_btn = wx.Button(self, wx.ID_ANY, "Next Icon >>>")

        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.EVT_BUTTON, self.on_previous, self.prev_btn)
        self.Bind(wx.EVT_BUTTON, self.on_next, self.next_btn)
        # end wxGlade
        
        self.icon_idx = 0
        self.load_icon()
    
    def load_icon(self):
        icon = wx.ArtProvider.GetBitmap(freedesktop_naming_spec_list[self.icon_idx], wx.ART_TOOLBAR, wx.Size(128, 128))
        self.bitmap.SetBitmap(icon)
    
    def __set_properties(self):
        # begin wxGlade: TestFrame.__set_properties
        self.SetTitle("frame")
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: TestFrame.__do_layout
        sizer_2 = wx.BoxSizer(wx.VERTICAL)
        sizer_1 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_2.Add(self.bitmap, 0, wx.ALIGN_CENTER, 0)
        sizer_1.Add(self.prev_btn, 0, wx.ALIGN_CENTER_HORIZONTAL, 0)
        sizer_1.Add(self.next_btn, 0, wx.ALIGN_CENTER_HORIZONTAL, 0)
        sizer_2.Add(sizer_1, 1, wx.ALIGN_CENTER | wx.EXPAND, 0)
        self.SetSizer(sizer_2)
        self.Layout()
        # end wxGlade

    def on_previous(self, _):  # wxGlade: TestFrame.<event_handler>
        self.icon_idx -= 1
        if self.icon_idx == -1:
            # self.icon_idx = len(all_icons) - 1
            self.icon_idx = len(freedesktop_naming_spec_list) - 1
        
        self.load_icon()
        
    def on_next(self, _):  # wxGlade: TestFrame.<event_handler>
        self.icon_idx += 1
        # if self.icon_idx > len(all_icons):
        if self.icon_idx > len(freedesktop_naming_spec_list):
            self.icon_idx = 0
        
        self.load_icon()
            
# end of class TestFrame


class IconWallApp(wx.App):
    def OnInit(self):
        # wx.ArtProvider.Push(wxTangoIconTheme())
        # wx.ArtProvider.Push(wxSuruIconTheme())
        wx.ArtProvider.Push(wxHumanityIconTheme())
        # wx.ArtProvider.Push(wxHumanityDarkIconTheme())
        # wx.ArtProvider.Push(wxAdwaitaIconTheme())
        self.frame = TestFrame(None, wx.ID_ANY, "")
        self.SetTopWindow(self.frame)
        self.frame.Show()
        return True

# end of class IconWallApp


if __name__ == "__main__":
    icon_wall_app = IconWallApp(0)
    icon_wall_app.MainLoop()