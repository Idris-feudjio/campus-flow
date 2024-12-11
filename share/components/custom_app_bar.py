from views.share.constants.size import *
def shrink(e):
         pass
class CustomAppBar(UserControl):
    def __init__(self):
        super().__init__() 
        self.container = Row(
            alignment=MainAxisAlignment.SPACE_BETWEEN,
            controls=[
                Container(on_click=lambda e:shrink(e),content=Icon(icons.MENU)),
                Row(
                    controls=[
                        Icon(icons.SEARCH),
                        Icon(icons.NOTIFICATIONS_OUTLINED)

                    ]
                )


            ]
        )
    def build(self):
          return self.container