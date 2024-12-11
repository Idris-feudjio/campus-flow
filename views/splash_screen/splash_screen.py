from flet import *
from share.db.auth import *

class SplashScreen:
    def __init__(self,page:Page, myPyrebase:PyrebaseWrapper) -> None:
        self.page=page
        self.myPyrebase=myPyrebase
        self.page.bgcolor=colors.BLUE_200  
        self.on_load()
        
    def on_load(self):  
        self.page.navigation_bar = None
        if self.myPyrebase.check_token():
                self.page.go('/dashboard')    
                print('------GO TO DASHBOARD-----------')
        else:
                print('------GO TO LOGIN-----------')
                self.page.go('/login')  
                
    def IndexView(self): 
        title = "SplashScreen"   
        banner = CircleAvatar(
            radius=100,
            content=Image(src='banner.png',border_radius=5, fit=ImageFit.COVER),
        )
    
        myPage = Container(
                content=Column( 
                    [ banner],  
                    alignment=MainAxisAlignment.CENTER,
                    horizontal_alignment = CrossAxisAlignment.CENTER
                ),
                padding=padding.only(top=200),   
            )

        return {
            "view":myPage,
            "title": title,
            "load": self.on_load
            }