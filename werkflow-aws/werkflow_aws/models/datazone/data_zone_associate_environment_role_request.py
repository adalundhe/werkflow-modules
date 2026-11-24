from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DataZoneAssociateEnvironmentRoleRequest(BaseModel):
    domainIdentifier: StrictStr
    environmentIdentifier: StrictStr
    environmentRoleArn: StrictStr
