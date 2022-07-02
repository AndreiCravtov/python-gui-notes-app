from aenum import Enum, auto

class SceneActions(Enum):
    class Login(Enum):
        LOGIN_BUTTON_PRESSED = auto()
        SIGN_UP_LABEL_PRESSED = auto()

    class SignUp(Enum):
        SIGN_UP_BUTTON_PRESSED = auto()
        LOGIN_LABEL_PRESSED = auto()

    class App(Enum):
        LOG_OUT_OPRION_PRESSED = auto()
        DELETE_ACCOUNT_OPTION_PRESSED = auto()