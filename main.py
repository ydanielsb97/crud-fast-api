from fastapi import FastAPI, Response, status, HTTPException
from pydantic import BaseModel
from random import randrange

app = FastAPI()

class Post(BaseModel):
    title: str
    content: str

my_posts = [
    {"title": "Title of post 1", "content": "Content of post 1", "id": 1},
    {"title": "Title of post 2", "content": "Content of post 2", "id": 2},
    ]

def get_one_post(id: int):
    return next(
       (item for item in my_posts if item['id'] == id),
       None
    )

def get_index_post(id: int):
    post = get_one_post(id)
    if not post:
        return None
    return my_posts.index(post)

def raise_not_found(message: str):
    raise HTTPException(status.HTTP_404_NOT_FOUND, message)

@app.get("/")
def root(): return {"message": "Hello World"}

@app.get("/posts")
def get_posts():
    return {"data": my_posts}

@app.get("/posts/{id}")
def get_post(id: int):
    
    post = get_one_post(id)    
    
    if not post:
        raise_not_found(f"Post with id {id} was not found")
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {"message": f"Post with id {id} was not found"}
    return {"data": post}

@app.post("/posts", status_code=status.HTTP_201_CREATED)
def create_post(post: Post):
    post_dict = post.dict()
    post_dict['id'] = randrange(0, 1000000)
    
    my_posts.append(post_dict)
    return {"data": post_dict}

@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int):
    post = get_one_post(id)
    if not post:
        raise_not_found(f"Post with id {id} was not found")
    
    try:    
        my_posts.remove(post)
    except ValueError:
        return raise_not_found(f"Post with id {id} was not found")
    
    return None

@app.put("/posts/{id}")
def update_post(id: int, post: Post):
    
    post_index = get_index_post(id)
    print(post_index)
    if post_index == None:
        raise_not_found(f"Post with id {id} was not found")
    
    my_posts[post_index].update(post.dict())
    
    return {"data": my_posts[post_index]}