from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SecurityHubAwsRdsDbClusterOptionGroupMembership(BaseModel):
    DbClusterOptionGroupName: StrictStr | None = None
    Status: StrictStr | None = None
