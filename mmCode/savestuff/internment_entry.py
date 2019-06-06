import wx
import wx.lib.inspection

class InternmentEntryFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, wx.ID_ANY, "Internment Entry")
        panel = wx.Panel(self)

        # First we create the controls
        top_label = wx.StaticText(panel, wx.ID_ANY, "Internment")
        top_label.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.BOLD))

        cemetery_label = wx.StaticText(panel, wx.ID_ANY, "Cemetery:")
        cemetery = wx.TextCtrl(panel, wx.ID_ANY, "")

        address_label = wx.StaticText(panel, wx.ID_ANY, "Address:")
        address = wx.TextCtrl(panel, wx.ID_ANY, "")

        csz_label = wx.StaticText(panel, wx.ID_ANY, "City, State, Zip:")
        city = wx.TextCtrl(panel, wx.ID_ANY, "", size=(150, -1))
        state = wx.TextCtrl(panel, wx.ID_ANY, "", size=(50, -1))
        zipcode = wx.TextCtrl(panel, wx.ID_ANY, "", size=(70, -1))

        gps_label = wx.StaticText(panel, wx.ID_ANY, "gps coordinates:")
        gps_long_label = wx.StaticText(panel, wx.ID_ANY, "Longitude")
        gps_lat_label = wx.StaticText(panel, wx.ID_ANY, "Lattitude")
        gps_long = wx.TextCtrl(panel, wx.ID_ANY, "")
        gps_lat = wx.TextCtrl(panel, wx.ID_ANY, "")

        location_label = wx.StaticText(panel, wx.ID_ANY, "Grave location:")
        location = wx.TextCtrl(panel, wx.ID_ANY,
            size=(280, 50), style=wx.TE_MULTILINE)

        sitepic_label = wx.StaticText(panel, wx.ID_ANY, "Grave pic:")
        sitepic = wx.TextCtrl(panel, wx.ID_ANY, "")

        stone_label = wx.StaticText(panel, wx.ID_ANY, "Gravestone pic:")
        stone = wx.TextCtrl(panel, wx.ID_ANY, "")

        death_label = wx.StaticText(panel, wx.ID_ANY, "Death date:")
        death_month = wx.TextCtrl(panel, wx.ID_ANY, "", size=(30, 20))
        death_slash = wx.StaticText(panel, wx.ID_ANY, "/")
        death_day = wx.TextCtrl(panel, wx.ID_ANY, "", size=(30, 20))
        death_slash1 = wx.StaticText(panel, wx.ID_ANY, "/")
        death_year = wx.TextCtrl(panel, wx.ID_ANY, "", size=(60, 20))
        death_button = wx.Button(panel, wx.ID_ANY, "date picker")


        save_button = wx.Button(panel, wx.ID_ANY, "Save")
        cancel_button = wx.Button(panel, wx.ID_ANY, "Cancel")

        #---------------------------------------------------
        # Now do the layout

        # main_sizer is the top level one that manages everything
        main_sizer = wx.BoxSizer(wx.VERTICAL)
        main_sizer.Add(top_label, 0, wx.ALL, 5)
        main_sizer.Add(wx.StaticLine(panel), 0,
                wx.EXPAND|wx.TOP|wx.BOTTOM, 5)



        # cemetery_sizer is the grid that holds all of the name/bio Info
        cemetery_sizer = wx.FlexGridSizer(cols=2, hgap=5, vgap=5)
        cemetery_sizer.AddGrowableCol(1)
        cemetery_sizer.Add(death_label, 0,
                wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL)
        # create a horizontal sizer for birth date and picker
        death_sizer = wx.BoxSizer(wx.HORIZONTAL)
        death_sizer.Add((30, 20), 1)
        death_sizer.Add(death_month)
        death_sizer.Add((5, 20), 1)
        death_sizer.Add(death_slash)
        death_sizer.Add((5, 20), 1)
        death_sizer.Add(death_day)
        death_sizer.Add((5, 20), 1)
        death_sizer.Add(death_slash1)
        death_sizer.Add((5, 20), 1)
        death_sizer.Add(death_year)
        death_sizer.Add((30, 20), 1)
        death_sizer.Add(death_button)
        cemetery_sizer.Add(death_sizer, 0, wx.EXPAND)

        cemetery_sizer.Add(cemetery_label, 0,
                wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL)
        cemetery_sizer.Add(cemetery, 0, wx.EXPAND)
        cemetery_sizer.Add(address_label, 0,
                wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL)
        cemetery_sizer.Add(address, 0, wx.EXPAND)

        cemetery_sizer.Add(csz_label, 0,
                wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL)

        # city, state, zip fields are in a sub-sizer
        csz_sizer = wx.BoxSizer(wx.HORIZONTAL)
        csz_sizer.Add(city, 1)
        csz_sizer.Add(state, 0, wx.LEFT|wx.RIGHT, 5)
        csz_sizer.Add(zipcode)
        cemetery_sizer.Add(csz_sizer, 0, wx.EXPAND)

        # grave location multiline
        cemetery_sizer.Add(location_label, 0,
                wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL)
        cemetery_sizer.Add(location, 0, wx.EXPAND)
        # add pics
        cemetery_sizer.Add(sitepic_label, 0,
                wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL)
        cemetery_sizer.Add(sitepic, 0, wx.EXPAND)
        cemetery_sizer.Add(stone_label, 0,
                wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL)
        cemetery_sizer.Add(stone, 0, wx.EXPAND)

        # gps coordinates
        cemetery_sizer.Add(20, 20) # skip a space left side
        # build right side container for labels
        gps_label_sizer = wx.BoxSizer(wx.HORIZONTAL)
        gps_label_sizer.Add((20, 20), 1)
        gps_label_sizer.Add(gps_lat_label)
        gps_label_sizer.Add((20, 20), 1)
        gps_label_sizer.Add(gps_long_label)
        gps_label_sizer.Add((20, 20), 1)
        # add the gps_label_sizer in
        cemetery_sizer.Add(gps_label_sizer, 0, wx.EXPAND)

        cemetery_sizer.Add(gps_label, 0,
                wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL)

        # build right side container for values
        gps_sizer = wx.BoxSizer(wx.HORIZONTAL)
        gps_sizer.Add((20, 20), 1)
        gps_sizer.Add(gps_lat)
        gps_sizer.Add((20, 20), 1)
        gps_sizer.Add(gps_long)
        gps_sizer.Add((20, 20), 1)
        # add the gps_sizer in
        cemetery_sizer.Add(gps_sizer, 0, wx.EXPAND)



        # now add the cemetery_sizer to the main_sizer
        main_sizer.Add(cemetery_sizer, 0, wx.EXPAND|wx.ALL, 10)

        # add a divider StaticLine
        main_sizer.Add(wx.StaticLine(panel), 0,
                wx.EXPAND|wx.TOP|wx.BOTTOM, 5)

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
InternmentEntryFrame().Show()
wx.lib.inspection.InspectionTool().Show()
app.MainLoop()
