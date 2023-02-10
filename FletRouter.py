
from one import One
from Exchange import Exchange
from YDown import YDown
from Translator import Prekladac
from Wiki import Wikipe

class Router:

    def __init__(self, page, ft):  #Volání příslušných funkcí(stránek) podle identifikátoeu
        self.page = page
        self.ft = ft
        self.routes = {
            "/": One(page),
            "/exchange": Exchange(page),
            "/Ydown": YDown(page),
            "/Translate": Prekladac(page),
            "/Wiki": Wikipe(page)
        }
        self.body = ft.Container(content=self.routes['/'])

    def route_change(self, route):
        self.body.content = self.routes[route.route]
        self.body.update()