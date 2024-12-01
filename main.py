from flet import  *
from views.home.home_view import *  
from share.db.db_config import firebaseConfig
import pyrebase


def main(page: Page):
    page.title = "CampusNews" 
    page.window.width = 360
    page.window.height = 720
    page.horizontal_alignment = CrossAxisAlignment.CENTER
    page.scroll = ScrollMode.ADAPTIVE
    page.bgcolor=colors.BLUE
    # create app control and add it to the page
    
    
    firebase = pyrebase.initialize_app(firebaseConfig)
    auth = firebase.auth()
    page.add(HomeView())


app(target=main)


#def main(page: ft.Page):
#    page.add(ft.SafeArea(ft.Text("Hello, Flet!")))
#
#
#ft.app(main)
#