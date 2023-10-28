from fastapi import APIRouter, Depends, HTTPException
from schemas.user import User, create_user, Response
from typing import Annotated

from uuid import UUID


user_router = APIRouter()

users: dict[str, User] = {}

    


@user_router.post("/", status_code=201)
async def register_a_user(user_in: create_user):
    user = User(id=str(UUID(int=len(users) + 1)), **user_in.dict())
    users[user.id] = user
    
    return Response(message= f"Your profile has been successfully registered with the unique ID: {user.id}", data= user)


@user_router.get("/",status_code=200)
def get_all_users():
    return users

@user_router.get("/{id}",status_code=200)
async def get_user_by_id(id: UUID):
    user = users.get(str(id))
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    return user

@user_router.put("/{id}",status_code=200)
async def update_user(id: UUID, user_in: create_user):
    user = users.get(str(id))
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    user['firstName'] = user_in.firstName
    user['lastName'] = user_in.lastName
    user['email'] = user_in.email
    user['username'] = user_in.username
    user['password'] = user_in.password
    
    return Response(message= "Your data has been updated successfully", data= user)
 
@user_router.delete("/{id}", status_code=200)
async def delete_book(id: UUID):
    user = users.get(str(id))
    if not user:
        raise HTTPException(status_code=404, detail="Book not found")
    
    del users[user.id]
    
    return Response(message= "Your data has been deleted successfully")
    

