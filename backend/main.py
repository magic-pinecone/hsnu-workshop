from datetime import datetime

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field

from comment_storage import list_comments, save_comment

# TODO: 1-1. 建立 FastAPI 應用程式

# TODO: 1-2. 設定 CORS，允許前端網頁存取 API

# TODO: 1-3. 實作你的第一個 API /api/magic


# 定義 POST API 的 Request Body 結構與驗證條件
class CommentModel(BaseModel):
    # TODO: 2. 使用 Pydantic 定義 request body 的欄位與驗證條件。
    #
    # 提示:
    #   - 字串欄位使用 str
    #   - 時間欄位使用 datetime
    #   - Field(..., max_length=N) 可以限制字串長度
    #   - 請確保欄位名稱與需求一致，否則可能會導致問題
    #
    # 欄位需求:
    #   article_name: string，最多 50 字
    #   user_name: string，最多 50 字
    #   comment: string，最多 500 字
    #   time: datetime
    ____: ____ = Field(..., max_length=____, description="留言文章名稱")
    ____: ____ = Field(..., max_length=____, description="留言使用者名稱")
    ____: ____ = Field(..., max_length=____, description="留言內容")
    ____: ____ = Field(..., description="留言時間")


# NOTE: 別忘了去 comment_storage.py 裡面設定你的留言資料庫名稱


# TODO: 3. 實作 POST /
@app.____(____)
def create_comment(data: CommentModel):
    # TODO:
    # 1. 將 data 轉成一筆留言資料
    # 2. 將留言存到後端
    # 3. 成功時回傳 {"status": "succeed"}
    #
    # 可以使用準備好的 helper: save_comment()
    raise HTTPException(
        status_code=501,
        detail="TODO: implement POST /",
    )


# TODO: 4. 實作 GET /{article_name}/comment
@app.____(____)
def get_comments(article_name: str):
    # TODO:
    # 1. 使用 article_name 找出這篇文章的所有留言
    #
    # 可以使用準備好的 helper: list_comments()
    raise HTTPException(
        status_code=501,
        detail="TODO: implement GET /{article_name}/comment",
    )
