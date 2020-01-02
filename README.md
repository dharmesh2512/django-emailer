# django-emailer

1. setup virtual environment
    ```virtualenv --python "C:\Program Files\Python\Python36\python.exe" venv```
2. Activate virtual environment
    ```venv\Script\activate```
3. Install dependencies
    ```pip install -r requirements.txt```
4. Run project using django server
    ```python manage.py runserver```
5. Add mailgun credentials
    - Replace `Domain` and `API_KEY` values in `services/mailgun.py`

#### Create super user
Start terminal with virtualenv activate and execute below command to create superadmin user to access django-admin dashboard panel.
```
python manage.py createsuperuser
```

#### Start new terminal to run celery.
1. Start celery worker to run tasks
    ```celery -A django_emailer worker -l info```
2. Start celery beat for cronjob work
    ```celery -A django_emailer beat -l info```


#### Run django emailer in docker
Follow below steps to run django-emailer project using docker

1. Install redir-server
    - ```sudo apt-get install redis-server```
2. Go to Project roor direcotry and execute below commands:
    - ```docker build .```
    - ```docker-compose up``` (With this command celery and django server will start, django server will start on port 8000)
3. To create super user, open new terminal window and execute below commands:
    - ```docker container list``` - This will return list of containers, find container image name with `djangoemailer_web` and get container ID of it and apply below command to create super user.
    - ```docker exec -it <container ID> python manage.py createsuperuser```
4. Open url `localhost:8000/admin` in browser, you will get admin screen and login with super user credentials.