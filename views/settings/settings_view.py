from share.db.auth import PyrebaseWrapper
from flet import *


class SettingsView:
    routeName = "/setting"
    def __init__(self,page:Page, myPyrebase:PyrebaseWrapper) -> None:
        self.page=page
        self.myPyrebase=myPyrebase
        self.page.bgcolor=colors.BLUE_200  
        self.build_page
        
    def handle_logout(self,*e):
            #clean_notes() 
            self.myPyrebase.kill_all_streams()
            self.myPyrebase.sign_out()
            self.page.go("/login")
            
    def build_page(self):  
        print("------------------SettingsView-------------------------") 
        
        logout_button = TextButton("Logout", on_click=self.handle_logout, style=ButtonStyle(colors.RED))
        
        return Container(
            content=Column(
                controls=[
                    Text(value='SettingsView'),
                    
            logout_button,
                ]
            ),
        )