from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .user import User


class Votes(BaseModel):
    hasVoted: StrictBool | None = None
    self: StrictStr | None = None
    voters: list[User] | None = None
    votes: StrictInt | None = None
