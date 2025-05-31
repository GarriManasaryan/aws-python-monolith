from abc import ABC, abstractmethod

from application.repos.query_params import QueryParams
from port.adapters.backoffice.models.user import UserCreationRequestBody, UserBackofficeModel

class UserQueryParams(QueryParams):
    name: str | None

class UserRepo(ABC):

    @abstractmethod
    def save(self, user: UserCreationRequestBody) -> None:
        pass

    @abstractmethod
    def query(self, params: UserQueryParams) -> list[UserBackofficeModel]:
        pass