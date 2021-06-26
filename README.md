### Teste - Backend Cíngulo 

1.  Intall project:

    ```sh
    git clone https://github.com/jgmartinss/teste-cingulo.git teste-cingulo-joao
    ```

2.  Install requirements:

    ```sh
    pip install -r requirements.txt
    ```

3.  Configure database:

    Create database 'cingulo'

    ```python
    # settings.py

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'cingulo', 
            'USER': 'postgres', 
            'PASSWORD': '', # change password
            'HOST': '127.0.0.1', 
            'PORT': '5432',
        }   
    }

    ```

4.  Run the project:

    ```shell
    $ python manage.py makemigrations
    $ python manage.py migrate
    $ python manage.py shell -c "from django.contrib.auth import get_user_model; CustomUser = get_user_model();  CustomUser.objects.create_superuser('admin', 'admin@email.com', 'admin')" # create user
    $ python manage.py get_user_activities --ref_year 2021 # populate database
    $ python manage.py drf_create_token admin # create token
    $ python manage.py runserver
    
    ```

5.  Run endpoints:

    ```sh

    $ curl http://127.0.0.1:8000/api/user-activiti/2 -H 'Authorization: Token 9acab09d64bd049b59baefc111a962ce92e43972'

    Response:

        [
            {
                "id_user": 2,
                "ref_year": 2021,
                "data": {
                    "2021-01-01": 1,
                    "2021-01-02": 0,
                    "2021-01-03": 0,
                    "2021-01-04": 1,
                    "2021-01-05": 0,
                    "2021-01-06": 0,
                    "2021-01-07": 0,
                    "2021-01-08": 0,
                    "2021-01-09": 1,
                    "2021-01-10": 1,
                    "2021-01-11": 1,
                    "2021-01-12": 1,
                    "2021-01-13": 1,
                    "2021-01-14": 1
                    ...
                }
            }
        ]

    $ curl http://127.0.0.1:8000/api/users-activities-by-date/2021-11-08 -H 'Authorization: Token 9acab09d64bd049b59baefc111a962ce92e43972'

    Response:

        {
            'total': 19
        }

    $ curl http://127.0.0.1:8000/api/users-activities-by-month/2021/11 -H 'Authorization: Token 9acab09d64bd049b59baefc111a962ce92e43972'

    Response:

        {
            "2021-11-01": 21,
            "2021-11-02": 20,
            "2021-11-03": 24,
            "2021-11-04": 18
            ...
        }
    
    ```
