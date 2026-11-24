from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QBusinessDataSourceVpcConfiguration(BaseModel):
    subnetIds: list[StrictStr] | None = None
    securityGroupIds: list[StrictStr] | None = None
