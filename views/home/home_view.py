#from views.share.components.custom_app_bar import *
from flet import *
from controllers.dummy_data import * 
from share.constants.size import *

is_drawer = True
def shrink_drawer(e):
    page_2.controls[0].width = 170
    page_2.controls[0].scale = transform.Scale(0.7,alignment=alignment.center_right)
    is_drawer = False
    page_2.update()
def restore_drawer(e):
    page_2.controls[0].width = 360
    page_2.controls[0].scale = transform.Scale(1,alignment=alignment.center_right)
    is_drawer = True
    page_2.update()

 
page_1 = Container( 
        expand=True, 
        border_radius=25,  
        content=Column(
            controls=[
                Container(
                    on_click=lambda e:restore_drawer(e), 
                    content=CircleAvatar(
                        radius = padding25, 
                        bgcolor = colors.WHITE,
                        content=CircleAvatar(
                            bgcolor = colors.TRANSPARENT,
                            radius = 23, 
                            content=Icon(icons.NAVIGATE_NEXT,size=20),
                        ),
                    ),
                )
            ]
        )
)
custom_app_bar = Row(
            alignment=MainAxisAlignment.SPACE_BETWEEN,
            controls=[
                Container(on_click=lambda e:shrink_drawer(e), content=Icon(icons.MENU)),
                Row(
                    controls=[
                        Icon(icons.SEARCH),
                        Icon(icons.NOTIFICATIONS_OUTLINED)

                    ]
                )


            ]
        )
page_2 = Row(alignment=MainAxisAlignment.END,
    controls=[
        Container(expand=True, 
                  border_radius=10,
                  
                bgcolor=colors.AMBER,
                  
                  height = 850,
                  animate=animation.Animation(600,AnimationCurve.DECELERATE),padding=padding.only(top=padding30,left=padding20,right=padding20,bottom=padding5),
                content= Column(
                     controls=[ 
                         custom_app_bar,
                         Container( height=10 ),
                        Text(f"Hi Welcome {anounce1.channel.class_name}",text_align=TextAlign.LEFT,style=TextStyle(size=fontsize25,weight=FontWeight.BOLD))
                     ]
                 ),
                 animate_scale= animation.Animation(400,curve="decelerate")
                
                )
    ]
)
class HomeView(UserControl):
    def __init__(self):
        super().__init__() 
        self.container = Container(
            expand=True,  

            content=Stack(controls=[
                page_1,
                page_2
            ])
        )
    def build(self):
        return self.container
    