from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class ElastiCacheAuthenticationMode(BaseModel):
    Type: Literal['password', 'no-password-required', 'iam'] | None = None
    Passwords: list[StrictStr] | None = None
