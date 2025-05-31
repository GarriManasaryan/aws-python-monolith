from fastapi import APIRouter, Depends, Query

from application.UserService import UserService
from application.repos.user_repo import UserQueryParams, UserRepo
from port.adapters.backoffice.models.user import UserBackofficeModel, UserCreationRequestBody
from port.adapters.persistence.pg_user import PGUser

router = APIRouter(tags=["User"])

def get_user_repo() -> UserRepo:
    return PGUser()

def get_user_service(repo: UserRepo = Depends(get_user_repo)) -> UserService:
    return UserService(repo=repo)

def get_query_params(
    page: int = Query(0),
    size: int = Query(100),
    name: str | None = Query(None),
) -> UserQueryParams:
    return UserQueryParams(page=page, size=size, name=name)

@router.get("/users", response_model=list[UserBackofficeModel])
def get_users(
        params: UserQueryParams = Depends(get_query_params),
        service: UserService = Depends(get_user_service)
):
    return service.query(params)

@router.post("/users")
def create_user(
        user_data: UserCreationRequestBody,
        service: UserService = Depends(get_user_service)
):
    service.save(user_data)
