from models.user import Anounce
from share.constants.size import *
from flet import *


class AnounceCard:
    def __init__(self,anounce:Anounce) -> None:  
        self.anounce = anounce
       # self.on_load()
        
        
    def on_load(self):  
        print("------------------AnounceCard-------------------------") 
        
        return Card(
        content=Container(
            content=Column( 
                [
                    ListTile(
                        leading=CircleAvatar(bgcolor=colors.BLUE_300,radius=35,content=CircleAvatar(radius=30,content=Image(src='banner.png',border_radius=5, fit=ImageFit.COVER),)),
                        title=Text(self.anounce.teacher.full_name(),size=fontsize15,weight=FontWeight.BOLD),
                        subtitle=Text(
                            "Music by Julie Gable. Lyrics by Sidney Stein.",size=fontsize10,weight=FontWeight.BOLD
                        ),
                    ),
                    Row(
                        [TextButton("Buy tickets"), TextButton("Listen")],
                        alignment=MainAxisAlignment.END,
                    ),
                ],
            ),
            width=400,
            padding=10,
        )
    )