from __future__ import annotations
from pydantic import BaseModel, StrictStr


class KMSDescribeKeyRequest(BaseModel):
    KeyId: StrictStr
    GrantTokens: list[StrictStr] | None = None
