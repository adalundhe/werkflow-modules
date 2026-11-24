from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DataZoneDisassociateEnvironmentRoleRequest(BaseModel):
    domainIdentifier: StrictStr
    environmentIdentifier: StrictStr
    environmentRoleArn: StrictStr
