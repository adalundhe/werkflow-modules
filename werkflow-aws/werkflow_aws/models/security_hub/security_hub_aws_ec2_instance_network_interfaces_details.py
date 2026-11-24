from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SecurityHubAwsEc2InstanceNetworkInterfacesDetails(BaseModel):
    NetworkInterfaceId: StrictStr | None = None
