from pydantic import BaseModel, computed_field

class QueryParams(BaseModel):
    """
    почему? limit понятно, это число записей, а offset - то, откуда начинать
    те с шагом в size мы берем перве 20 элементов, а на второй странице - 20*2 и начианем с 20 элемента,
    поэтому тут умножение

    page должен начинаться с 0
    """
    page: int = 0
    size: int = 100

    @computed_field
    @property
    def offset(self) -> int:
        return self.page * self.size
