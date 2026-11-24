from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .q_business_user_alias import QBusinessUserAlias


class QBusinessUpdateUserResponse(BaseModel):
    userAliasesAdded: list[QBusinessUserAlias] | None = None
    userAliasesUpdated: list[QBusinessUserAlias] | None = None
    userAliasesDeleted: list[QBusinessUserAlias] | None = None
    ResponseMetadata: dict[str, Any] | None = None
