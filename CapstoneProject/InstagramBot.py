from instapy import InstaPy
from instapy import smart_run

def run_instagram_bot (username,password):
    session = InstaPy (username = "user name",password = "password")

with smart_run (session):
    session.like_by_tags ("model", amount =10)

session.login ()

session.end()




