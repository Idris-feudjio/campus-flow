from share.db.auth import PyrebaseWrapper
from flet import *


class SettingsView:
    def __init__(self,page:Page, myPyrebase:PyrebaseWrapper) -> None:
        self.page=page
        self.myPyrebase=myPyrebase
        self.page.bgcolor=colors.BLUE_200  
        self.on_load
        
        
    def on_load(self):  
        print("------------------SettingsView-------------------------") 
        
        return Container(
            content=Text(value='SettingsView'),
        )