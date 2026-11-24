from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class EC2DeleteLocalGatewayVirtualInterfaceRequest(BaseModel):
    LocalGatewayVirtualInterfaceId: StrictStr
    DryRun: StrictBool | None = None
