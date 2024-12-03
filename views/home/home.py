from flet import *
from share.db.auth import *
class HomeView:
    def __init__(self,page:Page, myPyrebase:PyrebaseWrapper) -> None: 
        self.page = page 
        self.myPyrebase=myPyrebase
        self.page.bgcolor=colors.WHITE  
        self.page.bgcolor=colors.WHITE 
        self.username = Text("Welcome", size=16) 
        self.on_page_load
    
    def on_page_load(self):
           # clean_notes()
        self. username.value = "Welcome",
        if self.myPyrebase.check_token() == "Success":
            self.myPyrebase.stream_data(self.handle_stream)
            handle = self.myPyrebase.get_username()
            if handle:
                self.username.value = "Welcome, " + "@" + handle  
                self.page.update()
                
    def handle_stream(self,message):
       try:
           self.build_notes()
           self.page.update()
       except:
           pass
    def handle_add(self,e):
           #self. myPyrebase.add_note({"note": note_field.value})
           #note_field.value = ""
            self.page.update()

    def handle_logout(self,*e):
            #clean_notes()
            self.username.value = ""
            self.myPyrebase.kill_all_streams()
            self.myPyrebase.sign_out()
            self.page.go("/login")
             
    def build_page(self):
        def open_pagelet_end_drawer(e):
            pagelet.drawer.open = True
            pagelet.drawer.update()
        note_field = TextField(label="Enter note here", width=250)
        all_notes = []
        add_note_button = TextButton("Add Note", on_click=self.handle_add)
        logout_button = TextButton("Logout", on_click=self.handle_logout, style=ButtonStyle(colors.RED))
        myPage = Column([
                Row([Text("Dashboard", size=20)], alignment=MainAxisAlignment.CENTER),
                Row([self.username], alignment=MainAxisAlignment.CENTER),
                Column(all_notes, alignment="center"),
                Row([note_field], alignment=MainAxisAlignment.CENTER),
                Row([add_note_button], alignment=MainAxisAlignment.CENTER),
                Row([logout_button], alignment=MainAxisAlignment.CENTER)
                ])
        pagelet = Pagelet(
        appbar=AppBar(
            leading=IconButton(icons.MENU_ROUNDED,on_click=open_pagelet_end_drawer),
            leading_width=40,
            title=Text("AppBar Title"),
            center_title=False,
            bgcolor=colors.SURFACE_VARIANT,
            actions=[
                IconButton(icons.WB_SUNNY_OUTLINED),
                IconButton(icons.FILTER_3),
                PopupMenuButton(
                    items=[
                        PopupMenuItem(text="Item 1"),
                        PopupMenuItem(),  # divider
                        PopupMenuItem(
                            text="Checked item",
                            checked=False,
                        ),
                    ]
                ),
            ],
        ),
         drawer=NavigationDrawer(
            controls=[
                NavigationDrawerDestination(
                    icon=icons.HOME, label="Accueil",
                    icon_content=Badge(content=Icon(icons.HOME)),
                ),
                NavigationDrawerDestination(
                    icon=icons.NOTIFICATIONS, label="Notification",
                    icon_content=Badge(content=Icon(icons.NOTIFICATIONS), text="5"),
                ),
                NavigationDrawerDestination(
                    icon=icons.NOTIFICATIONS, label="Compte",
                    icon_content=Badge(content=Icon(icons.NOTIFICATIONS), text="5"),
                ),
            ],
        ),
        floating_action_button=FloatingActionButton(
            "Open", on_click=open_pagelet_end_drawer
        ),
        height=720,
        
        content=Container(height=300,bgcolor=colors.RED,content=myPage),
    )
        return pagelet
    
    def DashboardView(self):
        title = "My Dashboard"  
        note_field = TextField(label="Enter note here", width=250)
        all_notes = []
        add_note_button = TextButton("Add Note", on_click=self.handle_add)
        logout_button = TextButton("Logout", on_click=self.handle_logout, style=ButtonStyle(colors.RED))
        myPage = self.build_page()

        return {
            "view":myPage,
            "title": title,
            "load": self.on_page_load
            }