from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool


class EC2LaunchTemplatePrivateDnsNameOptionsRequest(BaseModel):
    HostnameType: Literal['ip-name', 'resource-name'] | None = None
    EnableResourceNameDnsARecord: StrictBool | None = None
    EnableResourceNameDnsAAAARecord: StrictBool | None = None
