from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class EC2DeleteVpcEndpointServiceConfigurationsRequest(BaseModel):
    ServiceIds: list[StrictStr]
    DryRun: StrictBool | None = None
