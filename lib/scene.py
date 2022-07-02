from tkinter import Frame, BOTH

class Scene(Frame):
    def __init__(self, action_listener, container, **kwargs):
        # set up action listener
        self.action_listener = action_listener

        # save reference to container
        self.container = container

        # start scene
        super().__init__(container, **kwargs)

    def show(self):
        self.on_show()
        self.pack(expand=True, fill=BOTH)

    def hide(self):
        self.on_hide()
        self.pack_forget()

    def on_show(self):
        pass

    def on_hide(self):
        pass
