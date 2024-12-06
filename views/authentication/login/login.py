from flet import *
from share.db.auth import *


def LoginForm(page:Page, myPyrebase:PyrebaseWrapper):
    title = "Login" 
    page.navigation_bar = None

    def on_loaded():
        page.navigation_bar = None
        if myPyrebase.check_token():
            page.go('/dashboard') 
              
    def handle_sign_in_error():
        page.snack_bar = SnackBar(
            content=Text("Incorrect Info. Please Try Again.", color=colors.WHITE),
            bgcolor=colors.RED
        )
        page.snack_bar.open = True
        page.update()

    def handle_sign_in(e):
        try:
            myPyrebase.sign_in(email_input.value, password_input.value)
            print(f'''
                  -----Login : {email_input.value}
                  -----Password : {password_input.value}''')
            password_input.value = ""
            page.go("/dashboard")
        except: 
            handle_sign_in_error()
            page.update()

    def handle_register(e):
        page.go('/register')
        
    def handle_google(e):
        google_button.scale = 0.9

    def handle_google_hover(e):
        pass

    banner = CircleAvatar(
        radius=55,
        content=Image(src='banner.png',border_radius=5, fit=ImageFit.COVER),
    )

    email_input = TextField(label="Email", prefix_icon=icons.EMAIL,border_radius=border_radius.all(5),)
    password_input = TextField(label="Password",password=True, can_reveal_password=True,prefix_icon=icons.LOCK,
        border_radius=border_radius.all(5)) 
    
    sign_in_button = ElevatedButton(
        text="Login",
        icon=icons.LOGIN,
        bgcolor=colors.BLUE_600,
        color=colors.WHITE,
        style=ButtonStyle(
            shape=RoundedRectangleBorder(radius=5),
            padding=padding.symmetric(vertical=15, horizontal=24),
        ),
        on_click=handle_sign_in,
    )
    go_to_register_button = Row(
        alignment=MainAxisAlignment.END,
        controls=[
            TextButton(
                text="No account yet ?",
                style=ButtonStyle(
                    shape=RoundedRectangleBorder(radius=5),
                    padding=padding.symmetric(vertical=12, horizontal=24),
                ),
                on_click=handle_register
                
            ),
        ]
    )
    
    google_button = Container(Image(src="btn_google_dark.png", width=250), on_click=handle_google, on_hover=handle_google_hover)
 
    myPage = Container(
            content=Column(
                [
                    banner,
                    Text(
                        "Bienvenue",
                        size=28,
                        weight=FontWeight.BOLD,
                        text_align=TextAlign.LEFT,
                    ),
                    Text(
                        "Veuillez vous connecter pour continuer.",
                        size=16, 
                        weight=FontWeight.BOLD,
                        color=colors.ON_SURFACE_VARIANT,
                        text_align=TextAlign.LEFT,
                    ),
                    email_input,
                    password_input,
                    Container(height=10),
                    sign_in_button,
                    Container(height=10),
                    go_to_register_button,
                ],
                
                horizontal_alignment = CrossAxisAlignment.STRETCH,
                spacing=20,
            ),
            padding=padding.all(20),   
        )
    
    return {
        "view":myPage,
        "title": title,
        "load": on_loaded
        }