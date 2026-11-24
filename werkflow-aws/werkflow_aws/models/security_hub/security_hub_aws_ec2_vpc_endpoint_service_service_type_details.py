from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SecurityHubAwsEc2VpcEndpointServiceServiceTypeDetails(BaseModel):
    ServiceType: StrictStr | None = None
