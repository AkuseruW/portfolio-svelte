from typing import Annotated
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from api.dependencies.users_dependencies import authenticate_user
from fastapi.responses import JSONResponse, RedirectResponse
from api.config.database import get_db
from api.config.schemas import SignInRequest
import uuid

router = APIRouter(prefix="/api", tags=["auth"])
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


@router.post("/login")
async def login(form_data: SignInRequest, db: Session = Depends(get_db)):
    user = authenticate_user(form_data.email, form_data.password, db)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    token = str(uuid.uuid4())
    response = JSONResponse(content={"message": "Login successful"})
    response.set_cookie(key="auth_token", value=token, secure=True, httponly=True)

    return response
