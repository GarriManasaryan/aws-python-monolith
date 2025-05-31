from application.common.decorators import transactional
from application.common.id_generator import generate_id
from application.repos.user_repo import UserRepo, UserQueryParams
from port.adapters.backoffice.models.user import UserCreationRequestBody, UserBackofficeModel
from port.adapters.persistence.pg_executer import all_entities, update, get_cursor, select


class PGUser(UserRepo):

    def save(self, user: UserCreationRequestBody) -> None:
        cursor = get_cursor()

        values = (generate_id(three_letter_domain="usr"), user.name)
        sql_template = (
            """
                insert into aw_user
                (id, name)
                values
                (%s, %s)
            """
        )
        update(cursor=cursor, sql_template=sql_template, values=values)

    def query(self, param: UserQueryParams) -> list[UserBackofficeModel]:
        cursor = get_cursor()
        sql = """
        select * from aw_user
        where (name ilike %s or %s is null)
        limit %s offset %s
        """
        values = (
            f"%{param.name}%" if param.name else None,
            param.name,
            param.size,
            param.offset
        )
        return select(cursor=cursor, sql_template=sql, entity=UserBackofficeModel, values=values)
