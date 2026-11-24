from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .user_details import UserDetails


class Watchers(BaseModel):
    isWatching: StrictBool | None = None
    self: StrictStr | None = None
    watchCount: StrictInt | None = None
    watchers: list[UserDetails] | None = None
