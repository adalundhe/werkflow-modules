from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class SecurityHubAwsEc2LaunchTemplateDataNetworkInterfaceSetPrivateIpAddressesDetails(BaseModel):
    Primary: StrictBool | None = None
    PrivateIpAddress: StrictStr | None = None
