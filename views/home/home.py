from flet import *
from share.db.auth import *
from views.notifications.notification_view import NotificationView
class HomeView:
    def __init__(self,page:Page, myPyrebase:PyrebaseWrapper) -> None: 
        self.page = page 
        self.myPyrebase=myPyrebase
        self.page.bgcolor=colors.WHITE  
        self.page.bgcolor=colors.WHITE 
        self.username = Text("Welcome", size=16) 
        self.index_selected = 0
        self.pages = [Text(value="Accueil", size=24, weight=FontWeight.BOLD),NotificationView(self.page,myPyrebase=myPyrebase).on_load(),Text(value="Compte", size=24, weight=FontWeight.BOLD)]
        self.on_page_load
        self.current_page = Text(value="Accueil", size=24, weight=FontWeight.BOLD)
    
    def on_page_load(self):
           # clean_notes()
        self.page.navigation_bar = NavigationBar(
        on_change=self.on_nav_change,
        selected_index=0,
            destinations=[ 
            NavigationBarDestination(icon=icons.HOME, label="Accueil"),
                
            NavigationBarDestination(
                icon_content=Badge(content=Icon(icons.MAIL), text="5"),
                label="Notification",
            ),
             NavigationBarDestination(icon=icons.SETTINGS_OUTLINED, label="Settings"), 
            ]
        )
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
             
    #ef build_page(self):
    #   def open_pagelet_end_drawer(e):
    #       pagelet.drawer.open = True
    #       pagelet.drawer.update()
    #   note_field = TextField(label="Enter note here", width=250)
    #   all_notes = []
    #   add_note_button = TextButton("Add Note", on_click=self.handle_add)
    #   logout_button = TextButton("Logout", on_click=self.handle_logout, style=ButtonStyle(colors.RED))
    #   myPage = Column([
    #           Row([Text("Dashboard", size=20)], alignment=MainAxisAlignment.CENTER),
    #           Row([self.username], alignment=MainAxisAlignment.CENTER),
    #           Column(all_notes, alignment="center"),
    #           Row([note_field], alignment=MainAxisAlignment.CENTER),
    #           Row([add_note_button], alignment=MainAxisAlignment.CENTER),
    #           Row([logout_button], alignment=MainAxisAlignment.CENTER)
    #           ])
    def on_nav_change(self,e):
        selected_index = self.page.navigation_bar.selected_index
        self.current_page.value = self.pages[selected_index].value
        self.page.update() 
          
    def DashboardView(self):
        title = "My Dashboard"  
        note_field = TextField(label="Enter note here", width=250)
        all_notes = []
        add_note_button = TextButton("Add Note", on_click=self.handle_add)
        logout_button = TextButton("Logout", on_click=self.handle_logout, style=ButtonStyle(colors.RED))
        myPage = Column(controls=[
            logout_button,
            self.current_page,
        ])

        return {
            "view":myPage,
            "title": title,
            "load": self.on_page_load
            }