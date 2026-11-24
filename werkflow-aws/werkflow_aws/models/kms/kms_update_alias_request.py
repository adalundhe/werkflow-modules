from __future__ import annotations
from pydantic import BaseModel, StrictStr


class KMSUpdateAliasRequest(BaseModel):
    AliasName: StrictStr
    TargetKeyId: StrictStr
