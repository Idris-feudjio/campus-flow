from flet import *
from share.db.auth import *

def IndexView(page:Page, myPyrebase:PyrebaseWrapper):
    title = "Flet + Pyrebase"

    def on_load():
        if myPyrebase.check_token():
            page.go('/dashboard')
        else:
            page.go('/auth')

    def handle_sign_in_error():
        page.snack_bar = SnackBar(
            content=Text("Incorrect Info. Please Try Again.", color=colors.WHITE),
            bgcolor=colors.RED
        )
        page.snack_bar.open = True
        page.update()

    def handle_sign_in(e):
        try:
            myPyrebase.sign_in(email.value, password.value)
            password.value = ""
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

    banner = Image(src='banner.png', width=250, border_radius=5, fit=ImageFit.COVER)
    welcome_text = Text("Welcome", size=26, bottom=10, right=10, color=colors.WHITE70)
    email = TextField(label="Email", width=250)
    password = TextField(label="Password", width=250, password=True)

    sign_in_button = TextButton("Sign In", on_click=handle_sign_in)
    register_button = TextButton("Register", on_click=handle_register)

    google_button = Container(Image(src="btn_google_dark.png", width=250), on_click=handle_google, on_hover=handle_google_hover)
    show = ""
    myPage = Column(
        [
            Container(
                Stack(
                [
                    banner,
                    welcome_text
                    ]
            ), alignment=alignment.center
            ),
            Row(
                [email],
                alignment=MainAxisAlignment.CENTER
                ),
            Row(
                [password],
                alignment=MainAxisAlignment.CENTER
                ),
            Row(
                [register_button, sign_in_button],
            alignment=MainAxisAlignment.CENTER),
        ]
            )
    
    return {
        "view":myPage,
        "title": title,
        "load": on_load
        }