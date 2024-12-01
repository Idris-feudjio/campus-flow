from flet import  *
from views.home.home_view import *   
from share.route.routes import * 
from share.constants.colors import *
from share.constants.size import *
 
def main(page: Page):
    page.title = "CampusNews" 
    page.window.width = 360
    page.window.height = 650
    page.horizontal_alignment = CrossAxisAlignment.CENTER
    page.scroll = ScrollMode.ADAPTIVE
    page.bgcolor=colors.WHITE
    page.theme_mode = ThemeMode.LIGHT
    page.vertical_alignment = MainAxisAlignment.CENTER
    
    page.window_title_bar_hidden = False
    page.window_frameless = False
    page.window_title_bar_buttons_hidden = False
    #page.bgcolor = colors.TRANSPARENT
    #page.window_bgcolor = colors.TRANSPARENT
    
    
    print(teacher1.to_json())
    
    myPyrebase = PyrebaseWrapper(page)
    myRouter = Router(page, myPyrebase)

    page.on_route_change = myRouter.route_change

    page.add(
        myRouter.body
    ) 

if __name__ == "__main__":
    app(target=main, assets_dir='assets')
