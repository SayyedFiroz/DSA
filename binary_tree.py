# Develop fast memory structure to manage profile info(username,user,email) and show allow insert,update,find,list

"""class User:
    def __init__(self,username,user,email):
        self.username=username
        self.user=user
        self.email=email

    def __repr__(self):
        return f"Username(username='{self.username}',user={self.user},email={self.email})"
    def __str__(self):
        return self.__repr__()

class Userdatabase:
    def __init__(self):
        self.users=[]

    def insert(self,user):
        i=0
        while i<len(self.users):
            if self.users[i].username>user.username:
                break
            i+=1
        self.users.insert(i,user)

    def find(self,username):
        for user in self.users:
            if user.username==username:
                return user
    def update(self,user):
        target=self.find(user.username)
        target.name.target.email=user.name,user.email

    def list_all(self):
        return self.users

raza=User('raza','khan raza','raza@123')

database=Userdatabase()
database.insert(raza)
database.list_all()

akash1=User('akash','akash mehta','akash@123')
mohd=User('mohd','mohd rahim','rahim@123')
jona=User('jona','jona thomas','jona@123')

usersdata=[akash1,mohd,jona]
database.insert(akash1)
print(database.list_all())"""


# simple binary tree (without any additional property) containing key
class TreeNode:
    def __init__(self,key):
        self.key=key
        self.left=None
        self.right=None

TreeNode0=TreeNode(3)
TreeNode1=TreeNode(4)
TreeNode2=TreeNode(4)

print(TreeNode0)
print(TreeNode0.key)

TreeNode0.left=TreeNode1
TreeNode1.right=TreeNode2

