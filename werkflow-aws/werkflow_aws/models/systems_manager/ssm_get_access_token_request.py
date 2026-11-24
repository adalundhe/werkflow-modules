from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SSMGetAccessTokenRequest(BaseModel):
    AccessRequestId: StrictStr
