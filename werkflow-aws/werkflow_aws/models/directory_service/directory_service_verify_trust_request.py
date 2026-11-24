from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DirectoryServiceVerifyTrustRequest(BaseModel):
    TrustId: StrictStr
