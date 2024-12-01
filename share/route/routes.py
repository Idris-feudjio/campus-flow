from flet import * 
from share.db.auth import PyrebaseWrapper
from views.splash_screen.splash_screen import *
from views.authentication.register.register import *
from views.home.home import *


class Router:

    def __init__(self, page:Page, myPyrebase:PyrebaseWrapper):
        self.page = page
        self.routes = {
            "/": IndexView(page, myPyrebase),
            "/dashboard": DashboardView(page, myPyrebase),
            "/register": RegisterView(page, myPyrebase)
        }
        self.body = Container(content=self.routes['/']["view"])

    def route_change(self, route):
        self.body.content = self.routes[route.route].get("view")
        self.page.title = self.routes[route.route].get("title")
        if self.routes[route.route].get("load"):
            self.routes[route.route].get("load")()
        self.page.update()