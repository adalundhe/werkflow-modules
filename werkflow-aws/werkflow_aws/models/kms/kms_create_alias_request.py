from __future__ import annotations
from pydantic import BaseModel, StrictStr


class KMSCreateAliasRequest(BaseModel):
    AliasName: StrictStr
    TargetKeyId: StrictStr
