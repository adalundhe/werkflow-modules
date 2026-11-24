from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SecurityHubAwsRdsDbClusterAssociatedRole(BaseModel):
    RoleArn: StrictStr | None = None
    Status: StrictStr | None = None
