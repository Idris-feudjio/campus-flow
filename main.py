from flet import  *
from views.home.home_view import *


def main(page: Page):
    page.title = "CampusFlow" 
    page.window.width = 360
    page.window.height = 720
    page.horizontal_alignment = CrossAxisAlignment.CENTER
    page.scroll = ScrollMode.ADAPTIVE
    page.bgcolor=colors.BLUE
    # create app control and add it to the page
    page.add(HomeView())


app(target=main)


#def main(page: ft.Page):
#    page.add(ft.SafeArea(ft.Text("Hello, Flet!")))
#
#
#ft.app(main)
#