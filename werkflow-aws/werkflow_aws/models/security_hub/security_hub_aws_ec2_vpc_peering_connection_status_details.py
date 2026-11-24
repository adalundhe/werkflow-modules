from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SecurityHubAwsEc2VpcPeeringConnectionStatusDetails(BaseModel):
    Code: StrictStr | None = None
    Message: StrictStr | None = None
