from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class MemoryDBAuthenticationMode(BaseModel):
    Type: Literal['password', 'iam'] | None = None
    Passwords: list[StrictStr] | None = None
