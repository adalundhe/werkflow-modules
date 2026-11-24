from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class SecurityHubAwsEc2LaunchTemplateDataPrivateDnsNameOptionsDetails(BaseModel):
    EnableResourceNameDnsAAAARecord: StrictBool | None = None
    EnableResourceNameDnsARecord: StrictBool | None = None
    HostnameType: StrictStr | None = None
