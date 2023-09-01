from fastapi import status, HTTPException
from .. import schemas, models, database
from sqlalchemy.orm import Session
from typing import List

 
def get_all(db:Session):
    blogs=db.query(models.Blog).all()
    return blogs

def create(request: schemas.Blog, db:Session ):
    new_blog = models.Blog(title=request.title, body=request.body, user_id=1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return request

def update(id:int,request: schemas.Blog, db:Session):
    blog = db.query(models.Blog).filter(models.Blog==id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=
                            f"Blog with id {id} does not exist")
    blog.update(request)
    db.commit()
    return 'updated'



def show(id:int,db:Session):
    blog = db.query(models.Blog).filter(models.Blog.id==id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Blog with id {id} doesn't exist")

    return blog


def destroy(id:int, db:Session):
    blog = db.query(models.Blog).filter(models.Blog.id==id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                             detail=f"Blog with id {id} doesn't exist")
    blog.delete(synchronize_session=False)
    db.commit()
    return 'done'