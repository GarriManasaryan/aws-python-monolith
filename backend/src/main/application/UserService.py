from application.common.decorators import transactional
from application.repos.user_repo import UserRepo, UserQueryParams
from port.adapters.backoffice.models.user import UserBackofficeModel, UserCreationRequestBody


class UserService:
    def __init__(self, repo: UserRepo):
        self.repo = repo

    @transactional
    def save(self, user: UserCreationRequestBody) -> None:
        self.repo.save(user)

    @transactional
    def query(self, params: UserQueryParams) -> list[UserBackofficeModel]:
        return self.repo.query(params)

