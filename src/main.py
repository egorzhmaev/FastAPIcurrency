from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from auth.base_config import fastapi_users, auth_backend
from auth.schemas import UserRead, UserCreate
from currency.router import router as curr_router
from auth.router import router as auth_router
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="templates")

app = FastAPI(
    title="Trading App"
)

app.mount("/log/login/static", StaticFiles(directory="static", html=True), name="static")
app.mount("/log/registration/static", StaticFiles(directory="static", html=True), name="static")
app.mount("/currency/static", StaticFiles(directory="static", html=True), name="static")

app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["auth"],
)

app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)

app.include_router(curr_router, prefix='/currency')
app.include_router(auth_router, prefix='/log')

origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "OPTIONS", "DELETE", "PATCH", "PUT"],
    allow_headers=["Content-Type", "Set-Cookie", "Access-Control-Allow-Headers", "Access-Control-Allow-Origin",
                   "Authorization"],
)

@app.get('/')
async def root():
    return {'message': 'Go to /currency/login for authentication'}