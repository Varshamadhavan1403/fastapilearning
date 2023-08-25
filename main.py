from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
import uvicorn

app = FastAPI()


class Blog(BaseModel):
    title:str
    body: str
    published: Optional[bool]

# @app.get('/')
# def index():
#     # return "hey"
#     return {"data":{"name":"varsha"}}

@app.get('/about')
def about():
    return {"data":{"about page"}}


# @app.get('/blog/{id}')
# def show(id):
#     return {"data":id}


@app.get('/blog/{id}/comments')
def comments(id):
    return {'data':{'1','2'}}


@app.get('/blog/unpublished/')
def unpublished():
    return {'data':'unpublished data'}


@app.get('/blog/{id}/')
def show(id:int):
    return {'data':id}


@app.get('/blog')
def index(limit=10, published:bool=True, sort: Optional[str]=None):
    if published:
        return {'data' : f'{limit} published blogs from the db'}
    
    else:
        return {'data' : f'{limit}  blogs from the db'}

@app.post('/blog')
def create_blog(blog:Blog):
    return {'data': f"Blog is created with title as {blog.title}"}




#for debugging

# if __name__== "__main__":
#     uvicorn.run(app, host="127.0.0.1", port=9000)