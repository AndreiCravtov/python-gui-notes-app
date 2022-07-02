# include other folders in the structure
import sys

from scenes.scene_actions import SceneActions
sys.path.append("./lib/")
sys.path.append("./logic/")
sys.path.append("./scenes/")

from actions import *
from scene_actions import *

from login import *
from sign_up import *
from app import *

from tkinter import *

class Main(Tk):
    def __init__(self):
        # Create window
        self.instantiate_window()
        
        # Declare needed variables
        self.declare_variables()
            
        # Create the frame objects
        self.make_frames()

    def instantiate_window(self):
        # Start root window
        super().__init__()

        # Configure root window
        self.title("Notes")
        self.geometry('960x540')
        self.resizable(False, False)

    def declare_variables(self):
        self.action_listener = ActionListener(self.handle_action)
        
    def make_frames(self):
        # define frames
        self.login = Login(self.action_listener, self)
        self.sign_up = SignUp(self.action_listener, self)
        self.app = App(self.action_listener, self)

        # show the default frame
        self.login.show()

    def handle_action(self):
        action = self.action_listener.pop_action()

        if action.scene is SceneActions.Login: # Login scene handling
            if action.action is SceneActions.Login.LOGIN_BUTTON_PRESSED:
                self.login.hide()
                self.app.show()
            elif action.action is SceneActions.Login.SIGN_UP_LABEL_PRESSED:
                self.login.hide()
                self.sign_up.show()
            else:
                raise Exception("No such action: {}".format(action.action))
        
        elif action.scene is SceneActions.SignUp: # Signup scene handling
            if action.action is SceneActions.SignUp.SIGN_UP_BUTTON_PRESSED:
                self.sign_up.hide()
                self.app.show()
            elif action.action is SceneActions.SignUp.LOGIN_LABEL_PRESSED:
                self.sign_up.hide()
                self.login.show()
            else:
                raise Exception("No such action: {}".format(action.action))

        elif action.scene is SceneActions.App: # App scene handling
            if action.action is SceneActions.App.LOG_OUT_OPRION_PRESSED:
                self.app.hide()
                self.login.show()
            elif action.action is SceneActions.App.DELETE_ACCOUNT_OPTION_PRESSED:
                self.app.hide()
                self.login.show()
            else:
                raise Exception("No such action: {}".format(action.action))

        else:
            raise Exception("Action from a non-existent scene detected\naction: {}\nscene: {}".format(action.action, action.scene))

if __name__ == '__main__':
    Main().mainloop()
