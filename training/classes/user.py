#!/usr/bin/env python3.7
class User():
    def __init__(self, name, admin, active):
        self.admin = bool(admin)
        self.active = bool(active)
        self.user = {'name':name, 'admin':self.admin, 'active':self.active}

        if self.user['admin'] == True and self.user['active'] == True:
            self.prefix = "ACTIVE - (ADMIN) "
        elif self.user['admin'] == False and self.user['active'] == True:
            self.prefix = "ACTIVE - "
        elif self.user['admin'] == True:
            self.prefix = "(ADMIN) "
        else:
            self.prefix = ""

    def getUser(self):
        return f"{self.prefix}{self.user.get('name')}"


def main():
    #from user import User
    user1 = User('user1',1,1)
    user2 = User('user2',0,1)
    user3 = User('user3',1,0)
    user4 = User('user4',0,0)

    userlist = [user1, user2, user3, user4]

    for user in userlist:
        if user.getUser() is not None:
            print(f"{userlist.index(user)+1} {user.getUser()}")

main()
