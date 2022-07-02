from cgitb import text
from curses.textpad import Textbox
from actions import *
from logic.database_access import DatabaseAccess
from scene_actions import *

from database_access import *

from scene import *
from tkinter import *

class App(Scene):
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
        self.note_text_area = None

    def configure_frame(self):
        # make the app responsive
        self.columnconfigure(index=0, weight=2)
        self.columnconfigure(index=1, weight=6)
        self.columnconfigure(index=2, weight=8)
        self.columnconfigure(index=3, weight=6)
        self.columnconfigure(index=4, weight=2)
        self.columnconfigure(index=5, weight=6)
        self.columnconfigure(index=6, weight=2)
        self.rowconfigure(index=0, weight=1)
        self.rowconfigure(index=1, weight=2)
        self.rowconfigure(index=2, weight=1)
        self.rowconfigure(index=3, weight=10)
        self.rowconfigure(index=4, weight=1)
        self.rowconfigure(index=5, weight=2)
        self.rowconfigure(index=6, weight=1)

        # set background
        self.config(background="#00C2FE")
        
    def draw_widgets(self):
        # undo button
        self.undo_button = Button(
            self,
            text="UNDO",
            background="#FFFFFF",
            activebackground="#FFFFFF",
            foreground="#00C2FE",
            activeforeground="#00C2FE",
            relief=FLAT,
            padx=50,
            pady=10,
            font=("Cantarell", 24),
            command=self.undo
        )
        self.undo_button.grid(row=1, column=3, pady=10)

        # redo button
        self.redo_button = Button(
            self,
            text="REDO",
            background="#FFFFFF",
            activebackground="#FFFFFF",
            foreground="#00C2FE",
            activeforeground="#00C2FE",
            relief=FLAT,
            padx=50,
            pady=10,
            font=("Cantarell", 24),
            command=self.redo
        )
        self.redo_button.grid(row=1, column=5, pady=10)

        # clear button
        self.clear_button = Button(
            self,
            text="CLEAR",
            background="#FFFFFF",
            activebackground="#FFFFFF",
            foreground="#00C2FE",
            activeforeground="#00C2FE",
            relief=FLAT,
            padx=50,
            pady=10,
            font=("Cantarell", 24),
            command=self.clear
        )
        self.clear_button.grid(row=5, column=1, pady=10)

        # save button
        self.save_button = Button(
            self,
            text="SAVE",
            background="#FFFFFF",
            activebackground="#FFFFFF",
            foreground="#00C2FE",
            activeforeground="#00C2FE",
            relief=FLAT,
            padx=50,
            pady=10,
            font=("Cantarell", 24),
            command=self.save_text
        )
        self.save_button.grid(row=5, column=5, pady=10)

        # note text area
        self.note_text_area = Text(
            self,
            background="#FFFFFF",
            highlightbackground="#FFFFFF",
            highlightcolor="#FFFFFF",
            selectbackground="#F2F3F3",
            relief=FLAT,
            font=("Cantarell", 12),
            undo=True,
            autoseparators=True,
            maxundo=-1
        )
        self.note_text_area.grid(row=3, column=1, columnspan=5, sticky=EW)

        # create menu
        self.menu_bar = Menu(
            self,
            activebackground="#FFFFFF",
            activeforeground="#00C2FE",
            background="#00C2FE",
            foreground="#FFFFFF",
            relief=FLAT,
            font=("Cantarell", 14)
        )
        self.account_menu = Menu(
            self.menu_bar,
            tearoff=0,
            activebackground="#FFFFFF",
            activeforeground="#00C2FE",
            background="#00C2FE",
            foreground="#FFFFFF",
            relief=FLAT,
            font=("Cantarell", 14)
        )
        self.account_menu.add_command(
            label="Log Out",
            command=self.log_out_option_pressed
        )
        self.account_menu.add_command(
            label="Delete Account",
            command=self.delete_account_option_pressed
        )
        self.menu_bar.add_cascade(
            label="Account",
            menu=self.account_menu,
            underline=0
        )

    def undo(self):
        if self.note_text_area is not None:
            try:
                self.note_text_area.edit_undo()
            except:
                pass

    def redo(self):
        if self.note_text_area is not None:
            try:
                self.note_text_area.edit_redo()
            except:
                pass
    
    def clear(self):
        if self.note_text_area is not None:
            self.note_text_area.delete('1.0', END)

    def log_out_option_pressed(self):
        # call log out
        DatabaseAccess().log_out()

        # notify root window of this action
        self.action_listener.push_action(SceneActions.App, SceneActions.App.LOG_OUT_OPRION_PRESSED)

    def delete_account_option_pressed(self):
        # call delete account
        DatabaseAccess().delete_account()

        # notify root window of this action
        self.action_listener.push_action(SceneActions.App, SceneActions.App.DELETE_ACCOUNT_OPTION_PRESSED)

    def save_text(self):
        DatabaseAccess().write_text_changes(self.note_text_area.get('1.0', END))

    def on_show(self):
        self.container.config(menu=self.menu_bar)
        self.note_text_area.delete('1.0', END)
        self.note_text_area.insert('1.0', DatabaseAccess().read_plaintext())

    def on_hide(self):
        self.container.config(menu="")