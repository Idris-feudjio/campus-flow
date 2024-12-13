from flet import *
from share.db.auth import *
from views.home.home_view import HomeView
from views.settings.settings_view import SettingsView
from views.notifications.notification_view import NotificationView
class DashBoardView:
    routeName = "/dashboard"
    def __init__(self,page:Page, myPyrebase:PyrebaseWrapper) -> None: 
        self.page = page 
        self.myPyrebase=myPyrebase
        self.page.bgcolor=colors.WHITE  
        self.username = Text("Welcome", size=16) 
        self.index_selected = 0 
        home = HomeView(self.page,myPyrebase=myPyrebase)
        notification = NotificationView(self.page,myPyrebase=myPyrebase) 
        settings = SettingsView(self.page,myPyrebase=myPyrebase) 
        self.pages = [home.build_page(),notification.build_page(),settings.build_page()]
        self.current_page = home.build_page()
        self.on_page_load()
        
    def on_page_load(self):
           # clean_notes()
        self.page.navigation_bar = NavigationBar(
        on_change=self.on_nav_change,
        selected_index=0,
            destinations=[ 
            NavigationBarDestination(icon=icons.HOME, label="Accueil"),
            NavigationBarDestination(
                icon_content=Badge(content=Icon(icons.MAIL), text="5"),
                label="Notification"
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
             
    def on_nav_change(self,e):
        selected_index = self.page.navigation_bar.selected_index
        self.current_page.content = Container(content=self.pages[selected_index].content) 
        print(self.current_page.content)
        
        self.page.update() 
          
    def build_view(self):
        title = "My Dashboard"  
        note_field = TextField(label="Enter note here", width=250)
        all_notes = []
        add_note_button = TextButton("Add Note", on_click=self.handle_add)
        logout_button = TextButton("Logout", on_click=self.handle_logout, style=ButtonStyle(colors.RED))
        myPage = Column(controls=[
            self.current_page,
        ])

        return {
       "view":myPage,
       "title": title,
       "load": self.on_page_load
       }