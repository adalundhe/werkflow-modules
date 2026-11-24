from __future__ import annotations
from pydantic import BaseModel, StrictStr


class IAMDeleteAccountAliasRequest(BaseModel):
    AccountAlias: StrictStr
