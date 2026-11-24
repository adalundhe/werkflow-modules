from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .q_business_user_alias import QBusinessUserAlias


class QBusinessUpdateUserRequest(BaseModel):
    applicationId: StrictStr
    userId: StrictStr
    userAliasesToUpdate: list[QBusinessUserAlias] | None = None
    userAliasesToDelete: list[QBusinessUserAlias] | None = None
