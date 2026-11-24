from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SESDeleteTenantResourceAssociationRequest(BaseModel):
    TenantName: StrictStr
    ResourceArn: StrictStr
