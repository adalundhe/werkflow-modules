from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SESDeleteTenantRequest(BaseModel):
    TenantName: StrictStr
