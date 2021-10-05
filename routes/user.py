from fastapi import APIRouter
from config.db import conn
from models.user import users
from schemas.user import User


user = APIRouter()

@user.get('/')
def fetch_users():
    return conn.execute(users.select()).fetchall()

@user.post('/create/')
def create_users(user:User):
    return conn.execute(users.insert().values(
            name=user.name,
            username=user.username,
            password=user.password)
    )


@user.put('/update/{id}')
def update_users(id: int, user: User):
    return conn.execute(
        users.update().values(
            name=user.name,
            username=user.username,
            password=user.password)
        .where(users.c.id == id))


@user.delete('/remove/{id}')
def delete_users(id: int):
    return conn.execute(users.delete().where(users.c.id == id))
