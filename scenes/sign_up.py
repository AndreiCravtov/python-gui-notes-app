from actions import *
from scene_actions import *

from database_access import *

from scene import *
from placeholder_entry import *
from tkinter import *

class SignUp(Scene):
    def __init__(self, action_listener, container, **kwargs):
        # Create frame
        super().__init__(action_listener, container, **kwargs)
        
        # Declare variables
        self.declare_variables()

        # Configure frame
        self.configure_frame()
            
        # Draw the widgets
        self.draw_widgets()

    def declare_variables(self):
        self.username_entry = None
        self.password_entry = None

    def configure_frame(self):
        # Make the app responsive
        self.columnconfigure(index=0, weight=1)
        self.columnconfigure(index=1, weight=2)
        self.columnconfigure(index=2, weight=1)
        self.rowconfigure(index=0, weight=1)
        self.rowconfigure(index=1, weight=16)
        self.rowconfigure(index=2, weight=1)

        # set background
        self.config(background="#00C2FE")
        
    def draw_widgets(self):
        # inner frame
        self.inner_frame = Frame(self, background="#FFFFFF")
        self.inner_frame.columnconfigure(index=0, weight=1)
        self.inner_frame.columnconfigure(index=1, weight=6)
        self.inner_frame.columnconfigure(index=2, weight=1)
        self.inner_frame.rowconfigure(index=0, weight=1)
        self.inner_frame.rowconfigure(index=1, weight=3)
        self.inner_frame.rowconfigure(index=2, weight=3)
        self.inner_frame.rowconfigure(index=3, weight=3)
        self.inner_frame.rowconfigure(index=4, weight=3)
        self.inner_frame.rowconfigure(index=5, weight=1)
        self.inner_frame.rowconfigure(index=6, weight=1)
        self.inner_frame.rowconfigure(index=7, weight=1)
        self.inner_frame.grid(row=1, column=1, sticky=NS)

        # user login label
        self.user_login_label = Label(
            self.inner_frame,
            text="    User Sign Up    ",
            background="#FFFFFF",
            font=("Cantarell", 53)
        )
        self.user_login_label.grid(row=1, column=1)

        # username entry
        self.username_entry = PlaceholderEntry(
            self.inner_frame,
            placeholder="USERNAME",
            placeholder_color="#B2B3B3",
            background="#F2F3F3",
            highlightbackground="#F2F3F3",
            highlightcolor="#F2F3F3",
            relief=FLAT,
            font=("Cantarell", 24),
            width=23,
            justify=CENTER,
            validate="key",
            validatecommand=self.username_entry_typed
        )
        self.username_entry.grid(row=2, column=1)

        # password entry
        self.password_entry = PlaceholderEntry(
            self.inner_frame,
            placeholder="PASSWORD",
            placeholder_color="#B2B3B3",
            background="#F2F3F3",
            highlightbackground="#F2F3F3",
            highlightcolor="#F2F3F3",
            relief=FLAT,
            font=("Cantarell", 24),
            width=23,
            justify=CENTER,
            show="*",
            validate="key",
            validatecommand=self.password_entry_typed
        )
        self.password_entry.grid(row=3, column=1)

        # sign up button
        self.sign_up_button = Button(
            self.inner_frame,
            text="SIGN UP",
            background="#00C2FE",
            activebackground="#00C2FE",
            foreground="#FFFFFF",
            activeforeground="#FFFFFF",
            relief=FLAT,
            padx=50,
            pady=10,
            font=("Cantarell", 24),
            command=self.sign_up_button_pressed
        )
        self.sign_up_button.grid(row=4, column=1)

        # login label
        self.login_label = Label(
            self.inner_frame,
            text="Have an account? Login here!",
            cursor="hand2",
            background="#FFFFFF",
            foreground="#00C2FE",
            font=("Cantarell", 20)
        )
        self.login_label.bind("<Button-1>", lambda _: self.login_label_pressed())
        self.login_label.bind("<Enter>", lambda _: self.login_label.config(foreground="#00617f"))
        self.login_label.bind("<Leave>", lambda _: self.login_label.config(foreground="#00C2FE"))
        self.login_label.grid(row=6, column=1)

    def username_entry_typed(self):
        if self.username_entry is not None:
            self.username_entry.config(background="#F2F3F3")
        return True

    def password_entry_typed(self):
        if self.password_entry is not None:
            self.password_entry.config(background="#F2F3F3")
        return True

    def sign_up_button_pressed(self):
        # attempt account creation
        username = self.username_entry.get()
        password = self.password_entry.get()
        response = DatabaseAccess().create_account(username, password)

        # catch error return values and respond
        if response != 0:
            if response == -1:
                self.username_entry.config(background="#FFCCCC")
                return
            elif response == -2:
                self.password_entry.config(background="#FFCCCC")
                return
            else:
                return

        # notify root window of this action
        self.action_listener.push_action(SceneActions.SignUp, SceneActions.SignUp.SIGN_UP_BUTTON_PRESSED)

    def login_label_pressed(self):
        # notify root window of this action
        self.action_listener.push_action(SceneActions.SignUp, SceneActions.SignUp.LOGIN_LABEL_PRESSED)

    def on_hide(self):
        self.username_entry.delete('0', 'end')
        self.password_entry.delete('0', 'end')
        self.username_entry.event_generate('<FocusOut>')
        self.password_entry.event_generate('<FocusOut>')