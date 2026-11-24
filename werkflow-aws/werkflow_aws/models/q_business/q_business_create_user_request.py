from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .q_business_user_alias import QBusinessUserAlias


class QBusinessCreateUserRequest(BaseModel):
    applicationId: StrictStr
    userId: StrictStr
    userAliases: list[QBusinessUserAlias] | None = None
    clientToken: StrictStr | None = None
