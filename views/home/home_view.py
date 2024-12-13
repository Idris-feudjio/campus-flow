from share.db.auth import PyrebaseWrapper
from controllers.dummy_data import *
from flet import *

from views.home.components.announce_card import AnounceCard


class HomeView:
    def __init__(self,page:Page, myPyrebase:PyrebaseWrapper) -> None:
        self.page=page
        self.myPyrebase=myPyrebase
        self.page.bgcolor=colors.BLUE_200 
        self.anchor = SearchBar( 
                  expand=True,
                  height=35,
                  divider_color=colors.BLUE_100, 
                  bar_hint_text='Search anounce',
                  view_hint_text="Choose anounce in the suggestion",
                  on_change=self.handler_change,
                  on_submit=self.handle_submit,
                  on_tap=self.handle_tap, 
              )
         
        self.build_page
    
    def close_anchor(self,e):
        text = f'{e.control.data}'
        print(f'Closing view {text}')
        self.anchor.close_view()
        
    def handler_change(self,e):
        print (f'handle_change e.data {e.data}')
    def handle_submit(self,e):
        print (f'handle_submit e.data {e.data}')
    def handle_tap(self,e):
        print (f'handle_tap e.data {e.data}')
        self.anchor.open_view()
        
    def build_page(self):  
        print("------------------HomeView-------------------------") 
        list_v = ListView(expand=1,spacing=10,padding=20,auto_scroll=True,divider_thickness=1)
        search_item = []
        for anounce in get_anounce_list():  
            card = AnounceCard(anounce).on_load()
            list_v.controls.append(card)
        
        return Container(
            content=Column(controls=[
            Row(controls= [
              IconButton(icons.MENU_ROUNDED,on_click=()),  
              self.anchor,
              IconButton(icons.SEARCH,on_click=lambda _:self.anchor.open_view()), 
            ]),
            list_v
            
        ]),
        )