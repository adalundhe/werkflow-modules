from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SecurityHubAwsEc2LaunchTemplateDataNetworkInterfaceSetIpv6AddressesDetails(BaseModel):
    Ipv6Address: StrictStr | None = None
