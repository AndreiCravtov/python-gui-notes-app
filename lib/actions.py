class Action:
    def __init__(self, scene, action):
        self.scene = scene
        self.action = action

class ActionListener():
    def __init__(self, handle_action):
        self._current_action = None
        self._handle_action = handle_action

    def push_action(self, scene, action):
        """Sets or replaces current action"""
        self._current_action = Action(scene, action)
        self._handle_action()

    def pop_action(self):
        """Returns current action and removes it from memory"""
        return_action = self._current_action
        self._current_action = None
        return return_action