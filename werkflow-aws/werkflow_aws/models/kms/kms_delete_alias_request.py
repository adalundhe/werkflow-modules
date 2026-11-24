from __future__ import annotations
from pydantic import BaseModel, StrictStr


class KMSDeleteAliasRequest(BaseModel):
    AliasName: StrictStr
