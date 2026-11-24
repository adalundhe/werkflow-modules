from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictStr


class EC2ModifyPrivateDnsNameOptionsRequest(BaseModel):
    InstanceId: StrictStr
    DryRun: StrictBool | None = None
    PrivateDnsHostnameType: Literal['ip-name', 'resource-name'] | None = None
    EnableResourceNameDnsARecord: StrictBool | None = None
    EnableResourceNameDnsAAAARecord: StrictBool | None = None
