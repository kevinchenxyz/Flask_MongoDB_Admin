Flask_MongoDB_Admin
===================

myself try to do Flask-login+mongodb admin list.

password use Md5


Install mongodb :
--------------------

http://docs.mongodb.org/manual/installation/

it runing in Localhost so mongodb link 127.0.0.1


require
------------------
run "pip install -r requirements.txt "
to install requirements。

Insert "admin" user in mongo:
------------------------------------

the dir " User_Add_in_mongo/" use pymongo to insert admin data to database。

db name is "users" (you can change to what you want)。
then just run "addjson.py" to insert userd。


useing
--------

run "python run.py"

open web to "127.0.0.1:5050"

account: admin
pwd: admin

remember to change your password


