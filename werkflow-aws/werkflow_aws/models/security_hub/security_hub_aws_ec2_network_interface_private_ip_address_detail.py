from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SecurityHubAwsEc2NetworkInterfacePrivateIpAddressDetail(BaseModel):
    PrivateIpAddress: StrictStr | None = None
    PrivateDnsName: StrictStr | None = None
