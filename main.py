
from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel 



app = FastAPI()

class Post(BaseModel):
    title: str
    content: str
    published: bool=True

my_post=[{"title": "title of post 1", "content":"content of the post 1", "id":1 }, {"title": "title of post 2", "content":"content of the post 2", "id":2},{"title": "title of post 3", "content":"content of the post 3", "id":3}]

def find_index_post(id):
    for i,p in enumerate(my_post):
        if p['id'] == id:
            return i
        
        
#get method 
@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}

@app.get("/posts")
def read_root():
    return {"message": my_post}

#post method 

@app.post("/createpost")
def create_posts(payload: dict = Body(...)):
    print(payload)
    return {"new_post": f"title: {payload ['title' ]} content: {payload ['content']}"}

#delete method

@app.delete("/posts/{id}")
def delete_post(id: int):
    index= find_index_post(id)
    my_post.pop(index)
    return{'message': 'post was succesfully deleted'}
     
#update method

@app.put("/posts/{id}")
def update_post(id: int , post: Post):
    index= find_index_post(id)
    
    post_dict = post.dict()
    post_dict['id'] = id
    my_post[index] = post_dict
    return{"Data":post_dict}



