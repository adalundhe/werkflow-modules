from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .q_business_user_alias import QBusinessUserAlias


class QBusinessGetUserResponse(BaseModel):
    userAliases: list[QBusinessUserAlias] | None = None
    ResponseMetadata: dict[str, Any] | None = None
