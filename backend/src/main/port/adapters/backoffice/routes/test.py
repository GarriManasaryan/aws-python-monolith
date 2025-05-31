from fastapi import APIRouter, Depends, Query

from application.UserService import UserService
from application.repos.user_repo import UserQueryParams
from port.adapters.backoffice.models.user import UserBackofficeModel, UserCreationRequestBody
from port.adapters.persistence.pg_user import PGUser

router = APIRouter(tags=["Test"])

users = UserService(repo=PGUser())

def get_query_params(
    page: int = Query(0),
    size: int = Query(100),
    name: str | None = Query(None),
) -> UserQueryParams:
    return UserQueryParams(page=page, size=size, name=name)

@router.get("/tests", response_model=list[UserBackofficeModel])
def get_users(params: UserQueryParams = Depends(get_query_params)):
    return users.query(params)

@router.post("/tests")
def create_user(user_data: UserCreationRequestBody):
    users.save(user_data)
