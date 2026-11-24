from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SecurityHubAwsEc2LaunchTemplateDataNetworkInterfaceSetIpv4PrefixesDetails(BaseModel):
    Ipv4Prefix: StrictStr | None = None
