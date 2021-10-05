from fastapi import FastAPI, Depends
# from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from routes.user import user
app = FastAPI()
# oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


app.include_router(user)

# @app.post('/token')
# async def token(form_data : OAuth2PasswordRequestForm = Depends()):
#     print(form_data)
#     return {"access_token":form_data}

# @app.get('/add-pic')
# async def profile_upload(token:str= Depends(oauth2_scheme)):
#     return{"user": "ren", "token": token}
