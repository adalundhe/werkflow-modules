from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ManagedGrafanaVpcConfiguration(BaseModel):
    securityGroupIds: list[StrictStr] | None = None
    subnetIds: list[StrictStr] | None = None
