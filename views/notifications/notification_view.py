from share.db.auth import PyrebaseWrapper
from flet import *


class NotificationView:
    routeName = "/notification"
    def __init__(self,page:Page, myPyrebase:PyrebaseWrapper) -> None:
        self.page=page
        self.myPyrebase=myPyrebase
        self.page.bgcolor=colors.BLUE_200  
        self.build_page
    def build_page(self):  
        print("------------------NotificationView-------------------------") 
        
        return Container(
            content=Text(value='NotificationView'),
        )