from __future__ import annotations
from pydantic import BaseModel, StrictStr


class RedshiftClusterSecurityGroupMembership(BaseModel):
    ClusterSecurityGroupName: StrictStr | None = None
    Status: StrictStr | None = None
