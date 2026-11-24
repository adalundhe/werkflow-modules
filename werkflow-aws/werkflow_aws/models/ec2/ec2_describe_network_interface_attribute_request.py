from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictStr


class EC2DescribeNetworkInterfaceAttributeRequest(BaseModel):
    NetworkInterfaceId: StrictStr
    DryRun: StrictBool | None = None
    Attribute: Literal['description', 'groupSet', 'sourceDestCheck', 'attachment', 'associatePublicIpAddress'] | None = None
