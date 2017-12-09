from kivy.uix.screenmanager import Screen
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

class Home(Screen):
    def __init__(self, **kwargs):
        super(Home, self).__init__(**kwargs)

        self.load_widgets()

    def load_widgets(self, *args):
        main_grid = MainGrid()
        self.add_widget(main_grid)

class Settings(Screen):
    pass

class CoinGrid(GridLayout):
    def __init__(self, name, price, **kwargs):
        super(CoinGrid, self).__init__(**kwargs)

        self.cols = 2
        self.rows = 1

        self.name = name
        self.price = price
        self.load_widgets()

    def load_widgets(self, *args):
        coin_name = Label(text=self.name)
        coin_price = Label(text=self.price)
        toys = [coin_name, coin_price]
        [self.add_widget(toy) for toy in toys]


class MainGrid(GridLayout):
    def __init__(self, **kwargs):
        super(MainGrid, self).__init__(**kwargs)

        self.cols = 1
        self.load_widgets()

    def load_widgets(self, *args):
        btc_grid = CoinGrid(name='btc', price='90000')
        eth_grid = CoinGrid(name='eth', price='400')
        grids = [btc_grid, eth_grid]
        [self.add_widget(grid) for grid in grids]
