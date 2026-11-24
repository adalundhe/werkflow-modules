from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SecurityHubAwsEc2LaunchTemplateDataNetworkInterfaceSetIpv6PrefixesDetails(BaseModel):
    Ipv6Prefix: StrictStr | None = None
