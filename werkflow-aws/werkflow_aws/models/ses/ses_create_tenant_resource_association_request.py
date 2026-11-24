from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SESCreateTenantResourceAssociationRequest(BaseModel):
    TenantName: StrictStr
    ResourceArn: StrictStr
