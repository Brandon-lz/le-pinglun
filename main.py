from fastapi import FastAPI,Body
import crud
import db
from typing import List,Dict

app = FastAPI(on_startup=db.create_all())


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/comments",description="获取所有评论")
async def list_comments():
    res:List[dict] = await crud.list_comments()
    return {"data":res}


@app.get("/comment/{user}",description="获取某个用户的评论")
async def get_comment(user):
    return {"data": await crud.get_comment_by_remark_name(user)}



@app.post("/comment",description="添加一条评论")
async def create_comment(remark_name:str=Body(description="用户昵称"),content:str=Body(default='',description="评论内容")):
    await crud.create_comment(remark_name,content)
    return 'ok'


@app.delete("/comment/{remark_name}",description="删除某个用户的所有评论")
async def delete_comment(remark_name:str):
    await crud.delete_comment(remark_name)
    return 'ok'

@app.delete("/comment-by-id/{id}",description="删除评论")
async def delete_comment(id:str):
    await crud.delete_comment_by_id(id)
    return 'ok'




if __name__ == '__main__':
    import uvicorn
    uvicorn.run("main:app",host="0.0.0.0",port=8868,reload=False)