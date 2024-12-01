from flet import * 
from share.db.auth import *

def RegisterView(page:Page, myPyrebase:PyrebaseWrapper):
    title = "Register"

    def handle_sign_up(e):
        try:
            myPyrebase.register_user(name.value, username.value, email_input.value, password_input.value)
            name.value, username.value, email_input.value, password_input.value = '', '', '', ''
            page.go('/')
        except:
            handle_sign_in_error()

    def handle_sign_in_error():
        page.snack_bar = SnackBar(
            content=Text("Something's wrong. Please Try Again.", color=colors.WHITE),
            bgcolor=colors.RED
        )
        page.snack_bar.open = True
        page.update()

    banner = CircleAvatar(
        radius=55,
        content=Image(src='banner.png',border_radius=5, fit=ImageFit.COVER),
    )
    welcome_text = Text("User Registration", size=26, bottom=10, right=10, color=colors.WHITE70)
    name = TextField(label="Name", width=250,border_radius=border_radius.all(5))
    username = TextField(label="Username", width=250,border_radius=border_radius.all(5))
    email_input = TextField(label="Email", prefix_icon=icons.EMAIL,border_radius=border_radius.all(5),)
    password_input = TextField(label="Password",password=True, can_reveal_password=True,prefix_icon=icons.LOCK,
        border_radius=border_radius.all(5)) 
 
    back_to_login_button = Row(
        alignment=MainAxisAlignment.END,
        controls=[
            TextButton("I have account.", icon=icons.UNDO, icon_color=colors.RED, on_click=lambda _:page.go('/')),
        ]
    )
    sign_up_button = ElevatedButton(
        text="Sign up",
        icon=icons.SAVE,
        bgcolor=colors.BLUE_600,
        color=colors.WHITE,
        style=ButtonStyle(
            shape=RoundedRectangleBorder(radius=5),
            padding=padding.symmetric(vertical=15, horizontal=24),
        ),
        on_click=handle_sign_up,
    )
    
    myPage = Container(
            content=Column(
                [
                    banner,
                    Text(
                        "User Registration",
                        size=28,
                        weight=FontWeight.BOLD,
                        text_align=TextAlign.LEFT,
                    ),
                    name,
                    username,
                    email_input,
                    password_input,
                    Container(height=10),
                    sign_up_button,
                    Container(height=10),
                    back_to_login_button,
                ],
                
                horizontal_alignment = CrossAxisAlignment.STRETCH,
                spacing=20,
            ),
            padding=padding.all(20),   
        )
    
    return {
        "view":myPage,
        "title": title
        }
