'''
Prototype 1
=======================

This demonstrates the ability to enter in data
through a user interface. This UI is used for:
- manually entering data
- sending data for storage 

The focus of these factors surround a health 
application for preventative well-being. 

Created: 12/12/2017
By: KHS
'''

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

# Create both screens. Please note the root.manager.current: this is how
# you can control the ScreenManager from kv. Each screen has by default a
# property manager that gives you the instance of the ScreenManager used.
Builder.load_string("""
<MenuScreen>:
    BoxLayout:
        Button:
            text: 'Goto settings'
            on_press:
            	root.manager.transition.direction = 'left'
                root.manager.current = 'settings'
        Button:
            text: 'Quit'

<SettingsScreen>:
    BoxLayout:
        Button:
            text: 'My settings button'
        Button:
            text: 'Back to menu'
            on_press: 
            	root.manager.transition.direction = 'right'
                root.manager.current = 'menu'
""")

# Declare both screens
class MenuScreen(Screen):
    pass

class SettingsScreen(Screen):
    pass

# Create the screen manager
sm = ScreenManager()
sm.add_widget(MenuScreen(name='menu'))
sm.add_widget(SettingsScreen(name='settings'))

class TestApp(App):

    def build(self):
        return sm

if __name__ == '__main__':
    TestApp().run()




'''
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.storage.jsonstore import JsonStore
from os.path import join
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

# Create both screens. Please note the root.manager.current: this is how
# you can control the ScreenManager from kv. Each screen has by default a
# property manager that gives you the instance of the ScreenManager used.
Builder.load_string("""
<MenuScreen>:
    BoxLayout:
        Button:
            text: 'Goto settings'
            on_press: root.manager.current = 'settings'
        Button:
            text: 'Quit'

<SettingsScreen>:
    BoxLayout:
        Button:
            text: 'My settings button'
        Button:
            text: 'Back to menu'
            on_press: root.manager.current = 'menu'
""")

#This chuck of code allows for login
#Save and store information
#TODO: Get screens to switch

# Declare required screens
class MenuScreen(Screen):
    pass

class SettingsScreen(Screen):
    pass


# Create screen manager
sm = ScreenManager()
sm.add_widget(MenuScreen(name='menu'))
sm.add_widget(SettingsScreen(name='settings'))

class MyApp(App):

    def build(self):
        return sm()


if __name__ == '__main__':
    MyApp().run()
'''


'''
class AppScreen(sm):
    data_dir = App().user_data_dir
    store = JsonStore(join(data_dir, 'storage.json'))
    ...
        def login(self):
        username = self.login_username.text
        self.username = TextInput(multiline=False)
        password = self.login_password.text
        self.password = TextInput(password=True, multiline=False)
        AppScreen.store.put('credentials', username=username, password=password)
        '''

'''
#This code is supposed to be ableto retrieve the credentials
#TODO: will need to be implemented later date

try:
    store.get('credentials')['username']
except KeyError:
    username = ""
else:
    username = store.get('credentials')['username']

try:
    store.get('credentials')['password']
except KeyError:
    password = ""
else:
    password = store.get('credentials')['password']


'''

'''
#This chuck of code allows for a login screen
#This is an older idea; it does not store date
#TODO: Delete content when screen manager function works

class LoginScreen(GridLayout):

    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        self.cols = 2
        self.add_widget(Label(text='User Name'))
        self.username = TextInput(multiline=False)
        self.add_widget(self.username)
        self.add_widget(Label(text='password'))
        self.password = TextInput(password=True, multiline=False)
        self.add_widget(self.password)


class MyApp(App):

    def build(self):
        return LoginScreen()

'''