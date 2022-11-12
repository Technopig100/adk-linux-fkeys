def GUI(self, Gtk):

    # ========================================
    #               HEADER WINDOW
    # ========================================
    
    hb = Gtk.HeaderBar()
    hb.props.show_close_button = True
    hb.props.title = "ADK-Linux Fix-keys Application"
    hb.props.subtitle = "Refreshing the Pacman keys and Datbase on ADK-Linux"
    self.set_titlebar(hb)

    # ========================================
    #               MAIN WINDOW
    # ========================================

    vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
    vbox.set_size_request(500, 100)
    self.add(vbox)

    # ========================================
    #               GLOBALS
    # ========================================

    hbox1 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
 
    # ========================================
    #               BUTTONS
    # ========================================

    btn1 = Gtk.Button(label="Refresh Pacman Keys and Datbase")
    btn1.set_size_request(550, 100)
    btn1.set_name("label")

    btn1.connect("clicked", self.on_btn1_clicked)

    hbox1.pack_start(btn1, True, True, 0)

    self.lbl_status = Gtk.Label(label="Refreshing Pacman Keys and Datbase")

    vbox.pack_start(hbox1, False, False, 0)
    vbox.pack_end(self.lbl_status, False, False, 0)
