from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SecurityHubAwsRedshiftClusterClusterNode(BaseModel):
    NodeRole: StrictStr | None = None
    PrivateIpAddress: StrictStr | None = None
    PublicIpAddress: StrictStr | None = None
