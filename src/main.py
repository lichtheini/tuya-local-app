"""
@source https://github.com/kaustubhgupta/KivyMLApp/tree/master/Basic%20Auth%20App
"""

from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.properties import ObjectProperty


#import tinytuya
#from tinytuya.Contrib import SocketDevice

import os



kv = """
Screen:
    in_class: text
    MDLabel:
        text: 'Basic Authentication App'
        font_style: 'H2'
        pos_hint: {'center_x': 0.6, 'center_y': 0.8}
    MDTextField:
        id: text
        hint_text: 'Enter you password'
        helper_text: 'Forgot your password?'
        helper_text_mode: "on_focus" 
        pos_hint: {'center_x': 0.5, 'center_y': 0.4}
        size_hint_x: None
        width: 300
        icon_right: "account-search"
        required: True
        
    MDRectangleFlatButton:
        text: 'Submit'
        pos_hint: {'center_x': 0.5, 'center_y': 0.3}
        on_press:
            app.auth()

    MDRectangleFlatButton:
        id: powerstate
        text: 'activate'
        pos_hint: {'center_x': 0.5, 'center_y': 0.2}
        on_press:
            app.setup()
            
    MDLabel:
        text: ''
        id: show
        pos_hint: {'center_x': 0.5, 'center_y': 0.1}
"""


class Main(MDApp):
    in_class = ObjectProperty(None)

    def build(self):
        return Builder.load_string(kv)

    def auth(self):
        if self.root.in_class.text == 'root':
            label = self.root.ids.show
            label.text = "Sucess"
        else:
            label = self.root.ids.show
            label.text = "Fail"

    def setup(self):
        label = self.root.ids.show
        label.text = "loading tinytuya"
        import tinytuya

        label.text = "create device"
#        d = SocketDevice("bf6823916bed4f2286tyne", "192.168.178.34", "dcacc24203cb84d0")
#        d.set_version(3.4)
        
#        label.text = "update status"
#        d.status()

#        label.text = "Status: " + str(d.get_state()['on'])

    def on_start(self):
        from kivy import platform
        if platform == "android":
            label = self.root.ids.show
            label.text = "detected android"
            from android.permissions import request_permissions, Permission
            request_permissions([Permission.WRITE_EXTERNAL_STORAGE, Permission.READ_EXTERNAL_STORAGE])
            label.text = "permission requested"




Main().run()
