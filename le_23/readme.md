pip install django 
pip install bpython

cd le_23/
django-admin.py startproject bbs
(django版本:(1, 9, 7, 'final', 0))

cd bbs 
python manage.py startapp hello


//同步数据库
python manage.py makemigrations
python manage.py migrate

运行服务器
python manage.py runserver 8001

进入 bpython终端
python manage.py shell

//创建数据库
python manage.py makemigrations
python manage.py migrate

//手动创建一个管理员
python manage.py createsuperuser
