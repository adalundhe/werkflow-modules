from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EC2IpamPublicAddressSecurityGroup(BaseModel):
    GroupName: StrictStr | None = None
    GroupId: StrictStr | None = None
