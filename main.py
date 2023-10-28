from fastapi import FastAPI
from routers.blog import blog_router, posts
from routers.user import user_router

app = FastAPI()

app.include_router(user_router, prefix= "/user", tags=['User'])
app.include_router(blog_router, prefix="/blog", tags=['Blogs'])



@app.get("/Home", status_code=200)
def read_post():
    return posts

  
@app.get("/About")
def about_page():
    return "This is the about page"

@app.get("/Contact")
def contact():
    return "This is the contact page"