import kivy
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang.builder import Builder
from kivy.uix.widget import Widget


class MainWindow(Screen):
    numbs = []

    def take_input(self, num):
        num = float(num)
        self.numbs.append(num)

    def sum(self):
        som = 0
        for num in self.numbs:
            som += num
        return som

    def product(self):
        product = 1
        for num in self.numbs:
            product = product * num
        return product


class WindowManager(ScreenManager):
    pass


kv = Builder.load_file("my.kv")


class MyMainApp(App):
    def build(self):
        return MainWindow()


if __name__ == "__main__":
    MyMainApp().run()
