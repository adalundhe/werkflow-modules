from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class EC2DeleteLocalGatewayVirtualInterfaceGroupRequest(BaseModel):
    LocalGatewayVirtualInterfaceGroupId: StrictStr
    DryRun: StrictBool | None = None
