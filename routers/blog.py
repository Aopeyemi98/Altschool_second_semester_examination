from fastapi import APIRouter,HTTPException
from schemas.blog import Article, Update_article,Create_aticle,Response
from uuid import UUID
from fastapi.security import OAuth2PasswordBearer
from datetime import datetime
blog_router = APIRouter()

Oauth_scheme = OAuth2PasswordBearer(tokenUrl="token")

posts: list[Article] = []


#A reusable function that loops through the list of posts
def get_post_by_id(id: str):
    for post in posts:
        if post.id == id:
            return post
    
    return None
    

#CREATE-POST ROUTE
@blog_router.post("/",status_code=201)
async def create_post(blog: Create_aticle):
    blogger = Article(id=str(UUID(int=len(posts) + 1)), **blog.dict())
    posts.append(blogger)
    
    return Response(message= f"Your post has been successfully uploaded with the unique ID: {blogger.id}", data= blogger)


#GET- ALL-POST ROUTE
@blog_router.get("/", status_code=200)
def get_all_post():
    return posts


#GET-POST-BY-ID ROUTE
@blog_router.get("/{id}", status_code=200)
def get_post_id(id: str):
    post = get_post_by_id(id)
    if post:
        return post
    
    raise HTTPException(status_code=404, detail="Post not found")
    

#UPDATE ROUTE
@blog_router.put("/{id}", status_code=200)
async def update_post(id: str, post_in: Update_article):
    post = get_post_by_id(id)
    if not post:
         raise HTTPException(status_code=404, detail="Post not found")
        
    
    post.title = post_in.title
    post.content = post_in.content
    
    return Response(message= "Your post has been successfully updated", data= post)


#DELETE-POST ROUTE
@blog_router.delete("/{id}", status_code=200)
async def delete_post(id: str):
    post = get_post_by_id(id)
    if not post:
        raise HTTPException(status_code=404,detail="Post not foumd")
    
    post_index = None
    
    for i, pt in enumerate(posts):
        if pt.id == id:
            post_index = i
            break
    posts.pop(post_index)
    
    return Response(message= f"Your post of ID; {pt.id} has been deleted successfully")
      