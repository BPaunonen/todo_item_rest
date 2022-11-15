# REST API Demo

## Local dev setup

```sh
source REST/bin/activate
```

Start in debug mode with:

```sh
flask --app app --debug run
```

## Available Routes

`GET /todos` - list all TODO items

`GET /todos/1` - get TODO item with id 1

`POST /todos` - create a new TODO item

`PUT /todos/1` - Update TODO item with id 1

`DELETE /todos/1` - Delete TODO item with id 1
