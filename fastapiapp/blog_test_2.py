from fastapi import FastAPI, Form
from pydantic import BaseModel, Field
import datetime
from fastapi.middleware.cors import CORSMiddleware

blogs = [
  {
    'id': 1,
    'title': 'Title 111',
    'content': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.',
    'author': 'Frank Bao',
    'date': 'Aug 14th, 2020',
    'image': 'blog1.jpg'
  },
  {
    'id': 2,
    'title': 'Title 2',
    'content': 'This is blog content for title 2',
    'author': 'Frank Bao',
    'date': 'Aug 15th, 2020',
    'image': 'blog2.jpg'
  },
  {
    'id': 3,
    'title': 'Title 3',
    'content': 'This is blog content for title 3',
    'author': 'Frank Bao',
    'date': 'Aug 16th, 2020',
    'image': 'blog3.jpg'
  },
  {
    'id': 4,
    'title': 'Title 4',
    'content': 'This is blog content for title 4',
    'author': 'Frank Bao',
    'date': 'Aug 17th, 2020',
    'image': 'blog4.jpg'
  }
]

class Blog(BaseModel):
  id: int
  title: str
  content: str
  image: str
  author: str
  date: str

class BlogEntry(BaseModel):
  title: str = Field(..., example="title")
  content: str = Field(..., example="content")
  image: str = Field(..., example="blog1.jpg")    

app = FastAPI()
origins = [
  "http://localhost:8080/"
]
app.add_middleware(
  CORSMiddleware,
  allow_origins=origins,
  allow_credentials=True,
  allow_methods=["*"],
  allow_headers=["*"]
)
@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/blogs")
async def get_blogs():
  return blogs;

@app.post("/addblog", response_model=Blog)
async def addblog(title: str=Form(...), content: str=Form(...), image: str=Form(...)):
  new_id = max(blog["id"] for blog in blogs) + 1
  date = str(datetime.datetime.now())
  blog = {
    'id': new_id,
    'title': title,
    'content': content,
    'author': 'Frank Bao',
    'date': date,
    'image': image 
  }
  blogs.append(blog)
  mblog = Blog(id=new_id, title=title, content=content, author='Frank Bao', date=date, image=image)
  return mblog