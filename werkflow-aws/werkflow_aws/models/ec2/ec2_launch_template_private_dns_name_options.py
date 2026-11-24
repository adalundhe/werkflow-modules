from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class EC2LaunchTemplatePrivateDnsNameOptions(BaseModel):
    HostnameType: StrictStr | None = None
    EnableResourceNameDnsARecord: StrictBool | None = None
    EnableResourceNameDnsAAAARecord: StrictBool | None = None
