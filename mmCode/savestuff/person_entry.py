import wx
import wx.lib.inspection



class PersonEntryFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, wx.ID_ANY, "Person Entry")
        panel = wx.Panel(self)

        # First we create the controls
        top_label = wx.StaticText(panel, wx.ID_ANY, "Person Information")
        top_label.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.BOLD))

        gender_label = wx.StaticText(panel, wx.ID_ANY, "Gender:")
        gender_radio_M = wx.RadioButton(panel, wx.ID_ANY, label="Male", name="M")
        gender_radio_F = wx.RadioButton(panel, wx.ID_ANY, label="Female", name="F")

        fname_label = wx.StaticText(panel, wx.ID_ANY, "First name:")
        fname = wx.TextCtrl(panel, wx.ID_ANY, "")

        mname_label = wx.StaticText(panel, wx.ID_ANY, "middle name:")
        mname = wx.TextCtrl(panel, wx.ID_ANY, "")

        lname_label = wx.StaticText(panel, wx.ID_ANY, "last name:")
        lname = wx.TextCtrl(panel, wx.ID_ANY, "")

        suffix_label = wx.StaticText(panel, wx.ID_ANY, "name suffix:")
        suffix = wx.TextCtrl(panel, wx.ID_ANY, "")

        nickname_label = wx.StaticText(panel, wx.ID_ANY, "Nickname:")
        nickname = wx.TextCtrl(panel, wx.ID_ANY, "")

        description_label = wx.StaticText(panel, wx.ID_ANY, "Description:")
        description = wx.TextCtrl(panel, wx.ID_ANY,
            size=(280, 50), style=wx.TE_MULTILINE)

        notes_label = wx.StaticText(panel, wx.ID_ANY, "Notes:")
        notes = wx.TextCtrl(panel, wx.ID_ANY,
            size=(280, 50), style=wx.TE_MULTILINE)

        bio_label = wx.StaticText(panel, wx.ID_ANY, "Bio:")
        bio = wx.TextCtrl(panel, wx.ID_ANY,
            size=(280, 50), style=wx.TE_MULTILINE)

        thumb_label = wx.StaticText(panel, wx.ID_ANY, "Thumbnail:")
        thumb = wx.TextCtrl(panel, wx.ID_ANY, "")

        favpic_label = wx.StaticText(panel, wx.ID_ANY, "Favorite pic:")
        favpic = wx.TextCtrl(panel, wx.ID_ANY, "")

        other_label = wx.StaticText(panel, wx.ID_ANY, "Other pics:")
        other = wx.TextCtrl(panel, wx.ID_ANY, "")

        birth_label = wx.StaticText(panel, wx.ID_ANY, "Birth date:")
        birth_month = wx.TextCtrl(panel, wx.ID_ANY, "", size=(30, 20))
        birth_slash = wx.StaticText(panel, wx.ID_ANY, "/")
        birth_day = wx.TextCtrl(panel, wx.ID_ANY, "", size=(30, 20))
        birth_slash1 = wx.StaticText(panel, wx.ID_ANY, "/")
        birth_year = wx.TextCtrl(panel, wx.ID_ANY, "", size=(60, 20))
        birth_button = wx.Button(panel, wx.ID_ANY, "date picker")


        save_button = wx.Button(panel, wx.ID_ANY, "Save")
        cancel_button = wx.Button(panel, wx.ID_ANY, "Cancel")

        #---------------------------------------------------
        # Now do the layout

        # main_sizer is the top level one that manages everything
        main_sizer = wx.BoxSizer(wx.VERTICAL)
        main_sizer.Add(top_label, 0, wx.ALL, 5)
        main_sizer.Add(wx.StaticLine(panel), 0,
                wx.EXPAND|wx.TOP|wx.BOTTOM, 5)



        # name_sizer is the grid that holds all of the name/bio Info
        name_sizer = wx.FlexGridSizer(cols=2, hgap=5, vgap=5)
        name_sizer.AddGrowableCol(1)
        name_sizer.Add(gender_label, 0,
                wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL)

        # gender is in a sub-sizer
        gender_sizer = wx.BoxSizer(wx.HORIZONTAL)
        gender_sizer.Add((20, 20), 1)
        gender_sizer.Add(gender_radio_F)
        gender_sizer.Add((20, 20), 1)
        gender_sizer.Add(gender_radio_M)
        gender_sizer.Add((20, 20), 1)
        name_sizer.Add(gender_sizer, 0, wx.EXPAND)

        name_sizer.Add(fname_label, 0,
                wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL)
        name_sizer.Add(fname, 0, wx.EXPAND)
        name_sizer.Add(mname_label, 0,
                wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL)
        name_sizer.Add(mname, 0, wx.EXPAND)
        name_sizer.Add(lname_label, 0,
                wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL)
        name_sizer.Add(lname, 0, wx.EXPAND)
        name_sizer.Add(suffix_label, 0,
                wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL)
        name_sizer.Add(suffix, 0, wx.EXPAND)
        name_sizer.Add(nickname_label, 0,
                wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL)
        name_sizer.Add(nickname, 0, wx.EXPAND)
        name_sizer.Add(description_label, 0,
                wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL)
        name_sizer.Add(description, 0, wx.EXPAND)
        name_sizer.Add(notes_label, 0,
                wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL)
        name_sizer.Add(notes, 0, wx.EXPAND)
        name_sizer.Add(bio_label, 0,
                wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL)
        name_sizer.Add(bio, 0, wx.EXPAND)
        name_sizer.Add(thumb_label, 0,
                wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL)
        name_sizer.Add(thumb, 0, wx.EXPAND)
        name_sizer.Add(favpic_label, 0,
                wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL)
        name_sizer.Add(favpic, 0, wx.EXPAND)
        name_sizer.Add(other_label, 0,
                wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL)
        name_sizer.Add(other, 0, wx.EXPAND)
        name_sizer.Add(birth_label, 0,
                wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL)
        # create a horizontal sizer for birth date and picker
        birth_sizer = wx.BoxSizer(wx.HORIZONTAL)
        birth_sizer.Add((30, 20), 1)
        birth_sizer.Add(birth_month)
        birth_sizer.Add((5, 20), 1)
        birth_sizer.Add(birth_slash)
        birth_sizer.Add((5, 20), 1)
        birth_sizer.Add(birth_day)
        birth_sizer.Add((5, 20), 1)
        birth_sizer.Add(birth_slash1)
        birth_sizer.Add((5, 20), 1)
        birth_sizer.Add(birth_year)
        birth_sizer.Add((30, 20), 1)
        birth_sizer.Add(birth_button)
        name_sizer.Add(birth_sizer, 0, wx.EXPAND)

        # now add the name_sizer to the main_sizer
        main_sizer.Add(name_sizer, 0, wx.EXPAND|wx.ALL, 5)

        # the button_sizer will put them in a row with spaces
        button_sizer = wx.BoxSizer(wx.HORIZONTAL)
        button_sizer.Add((20, 20), 1)
        button_sizer.Add(save_button)
        button_sizer.Add((20, 20), 1)
        button_sizer.Add(cancel_button)
        button_sizer.Add((20, 20), 1)

        # now add the button_sizer to the main_sizer
        main_sizer.Add(button_sizer, 0, wx.EXPAND|wx.BOTTOM, 10)

        # Finally, tell the panel to use the sizer for layout
        panel.SetSizer(main_sizer)

        # Give the frame a sizer # too
        frame_sizer = wx.BoxSizer()
        frame_sizer.Add(panel, 1, wx.EXPAND)
        self.SetSizer(frame_sizer)

        # Fit the frame to the needs of the sizer. The frame will
        # automatically resize the panel as needed. Also prevent the
        # frame from getting smaller than this size.
        self.Fit()
        self.SetMinSize(self.GetSize())


app = wx.App()
PersonEntryFrame().Show()
wx.lib.inspection.InspectionTool().Show()
app.MainLoop()
