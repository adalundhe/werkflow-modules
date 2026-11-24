from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SecurityHubAwsRdsDbSubnetGroupSubnetAvailabilityZone(BaseModel):
    Name: StrictStr | None = None
