from flet import *
from share.db.auth import *
from views.dashboard.dashboard_view import DashBoardView

class SplashScreen:
    
    def __init__(self,page:Page, myPyrebase:PyrebaseWrapper) -> None:
        self.page=page
        self.myPyrebase=myPyrebase
        self.page.bgcolor=colors.BLUE_200  
        self.page.navigation_bar = None
        self.on_load()
        
    def on_load(self):  
        if self.myPyrebase.check_token():
                self.page.go(DashBoardView.routeName)    
                self.page.update()
                print(f'------GO TO {self.page.route.upper()}-----------')
        else:
                self.page.go('/login')  
                print(f'------GO TO {self.page.route.upper()}-----------')
                self.page.update()
        self.page.navigation_bar = None
        self.page.update()
                
    def build_view(self): 
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