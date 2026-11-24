from __future__ import annotations
from pydantic import BaseModel, StrictStr


class RedshiftModifyEndpointAccessRequest(BaseModel):
    EndpointName: StrictStr
    VpcSecurityGroupIds: list[StrictStr] | None = None
