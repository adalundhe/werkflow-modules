from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class EC2ValidateSecurityGroupQuotasForInterfaceRequest(BaseModel):
    SecurityGroupIds: list[StrictStr]
    DryRun: StrictBool | None = None
