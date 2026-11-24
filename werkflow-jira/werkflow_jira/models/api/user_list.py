from __future__ import annotations
from pydantic import BaseModel, ConfigDict, Field as PydanticField, StrictInt
from .user import User


class UserList(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    end_index: StrictInt | None = PydanticField(default=None, alias='end-index')
    items: list[User] | None = None
    max_results: StrictInt | None = PydanticField(default=None, alias='max-results')
    size: StrictInt | None = None
    start_index: StrictInt | None = PydanticField(default=None, alias='start-index')
