from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class Article(BaseModel):
    id: str
    title: str
    content: str
    author: str
    published: datetime = datetime.now
    
class Create_aticle(BaseModel):
    title: str
    content: str
    author: str
    published: datetime
    
class Update_article(BaseModel):
    title: str
    content: str

class Response(BaseModel):
    message: Optional[str] = None
    data: Optional[Article] = None    
    
    