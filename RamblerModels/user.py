class User(object):
    def __init__(self, username=None, password=None, komy=None, theme=None, area=None):
        self.username = username
        self.password = password
        self.komy = komy
        self.theme = theme
        self.area = area


    @classmethod
    def Admin(cls):
        return cls(username="autotestselenium", password="creative")

    @classmethod
    def Mailparameters(clt):
        return clt(komy="safonov-ve@ya.ru", theme="test_message", area="testmessage_for_autetest")