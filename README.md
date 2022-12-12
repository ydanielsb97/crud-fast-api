# CRUD with FastAPI

A simple CRUD API developed with python using the FastAPI framework.

Documentation: https://documenter.getpostman.com/view/10890377/2s8YzTU36K

## Endpoints
---
<br>

Create Post:
```http
POST /posts HTTP/1.1
Host: localhost:8000
Content-Length: 63

{
    "title": "Title test",
    "content": "Test Content"
}

```
Response 201 Created
```json
{
  "data": {
    "title": "Title test",
    "content": "Test Content",
    "id": 703048
  }
}
```
<br>
<br>



Get All

```http
GET /posts HTTP/1.1
Host: localhost:8000
```
Response 200 OK
```json
{
  "data": [
    {
      "title": "Title test",
      "content": "Test Content",
      "id": 703048
    }
  ]
}
```
<br>
<br>

Get One

```http
GET /posts/703048 HTTP/1.1
Host: localhost:8000
```
Response 200 OK
```json
{
  "data": {
    "title": "Title of post 1",
    "content": "Content of post 1",
    "id": 703048
  }
}
```
<br>
<br>

Patch One

```http
PATCH /posts/703048 HTTP/1.1
Host: localhost:8000
Content-Length: 75

{
    "title": "Title of post 55",
    "content": "Content of post 55"
}
```
Response 200 OK
```json
{
  "data": {
    "title": "Title of post 55",
    "content": "Content of post 55",
    "id": 703048
  }
}
```
<br>
<br>

Delete One

```http
DELETE /posts/1 HTTP/1.1
Host: localhost:8000
```
Response 201 No Content
