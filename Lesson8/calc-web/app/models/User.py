class User:
    userName = ''
    password = ''

    def __init__(self, userName, password) -> None:
        super().__init__()

        self.userName = userName
        self.password = password


