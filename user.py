# Baisc Data Model 4 User ----------------

class User():
    def __construct__(self, username, theme, image):
        self.username = username
        self.theme = theme
        self.image = image


users = []


def get_current_user():
    return session['loggeduser']


def get_all_users():
    return users


def set_user():
    newuser = User('Rodrigo', 'Light', './data/rod_profile.png')
    users.append(newuser)
    session['loggeduser'] = newuser

