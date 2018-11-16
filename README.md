# pythonDjango
/* Cài đặt django */
	- pip install django
/* Tạo project */
	- django-admin startproject nameproject (tên project)
/* Đến thư mục project */
	- cd nameproject
/* Tạo app */
	- python manage.py startapp nameapp (tên app)
/*vào thư mục settings.py của nameproject cài đặt tên app vào*/
	- INSTALLED_APPS = [
		'news',
		'django.contrib.admin',
		'django.contrib.auth',
		'django.contrib.contenttypes',
		'django.contrib.sessions',
		'django.contrib.messages',
		'django.contrib.staticfiles',
	]
/* Tạo các đường dẫn urls , cấu hình định tuyến*/
/* run server */
	- Python manage.py runserver
