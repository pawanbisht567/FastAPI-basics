from random import randrange
from typing import Optional

from fastapi import Body, FastAPI, Response, status, HTTPException
from pydantic import BaseModel

app = FastAPI()

posts = [{
    "title": "First Post",
    "content": "This is the content of the first post",
    "id": 1
}, {
    "title": "Second Post",
    "content": "This is the content of the second post",
    "id": 2
}]


class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None

@app.get("/")
async def root():
    return { "posts": posts }


@app.post('/createPost')
async def create_post(payload: dict = Body(...)):
    print(payload)
    # Here you can add logic to save the post to a database or perform other actions
    return {"message": "Post created successfully", "post": payload}


@app.post('/createPostWithModel') #Schema Validation here
async def create_post(post: Post, status_code=status.HTTP_201_CREATED): #status_code=status.HTTP_201_CREATED sets the default response status code to 201 (Created)
    new_post = post.model_dump()  # Convert the Pydantic model to a dictionary
    new_post['id'] = randrange(1, 1000000)  # Generate a random ID for the new post
    posts.append(new_post)  # Add the new post to the list of posts
    # Here you can add logic to save the post to a database or perform other actions
    
    return {"message": "Post created successfully", "data": posts}


def find_post(id):
    for post in posts:
        if post['id'] == id:
            return post
    return None

def find_post_index(id):
    for index, post in enumerate(posts):
        if post['id'] == id:
            return index
    return None

@app.get('/post/{id}')
async def get_post(id: int, response: Response): #automatically converts the path parameter from string to an integer
    post = find_post(id)
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id: {id} was not found")
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return { "message": f"Post with id: {id} was not found" }
    return { "post_detail": post }

@app.delete('/post/{id}', status_code = status.HTTP_204_NO_CONTENT)
async def delete_post(id: int):
    index = find_post_index(id)
    
    if index is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id: {id} does not exist")
    posts.pop(index)
    return Response(status_code=status.HTTP_204_NO_CONTENT)

@app.put('/post/{id}')
async def update_post(id: int, updated_post: Post):
    post_index= find_post_index(id)
    if post_index is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id: {id} does not exist")
    updated_post_dict = updated_post.model_dump()
    updated_post_dict['id'] = id  # Ensure the ID remains the same
    posts[post_index] = updated_post_dict
    return { "message": "Updated Post"}