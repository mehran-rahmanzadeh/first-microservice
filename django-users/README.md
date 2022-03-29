## Users Service (Python/Django)

### User API Endpoints

- /api/v1/users/ GET
- /api/v1/users/ POST
- /api/v1/users/change_password/ PATCH
- /api/v1/users/edit/ PATCH

### Auth API Endpoints

- /api/v1/token/ POST
- /api/v1/token/refresh/ POST
- /api/v1/token/verify/ POST

### gRPC Services

- AuthController/VerifyToken


### Start Django Server

```sh
$ python manage.py makemigrations
$ python manage.py migrate
$ python manage.py runserver
```

### Start gRPC Server

```sh
$ python manage.py run_grpc
```