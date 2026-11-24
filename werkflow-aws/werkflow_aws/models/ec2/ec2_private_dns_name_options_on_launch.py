from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class EC2PrivateDnsNameOptionsOnLaunch(BaseModel):
    HostnameType: StrictStr | None = None
    EnableResourceNameDnsARecord: StrictBool | None = None
    EnableResourceNameDnsAAAARecord: StrictBool | None = None
