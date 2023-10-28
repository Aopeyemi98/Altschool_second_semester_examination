from pydantic import BaseModel
from typing import Optional


class User(BaseModel):
    id: str
    firstName: str
    lastName: str
    email: str
    username: str
    password: str
   
class create_user(BaseModel):
    firstName: str
    lastName: str
    email: str
    username: str
    password: str
    
class Response(BaseModel):
    message: Optional[str] = None
    data: Optional[User] = None
                                        