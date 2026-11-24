from __future__ import annotations
from pydantic import BaseModel, StrictStr


class RedshiftAuthorizeClusterSecurityGroupIngressRequest(BaseModel):
    ClusterSecurityGroupName: StrictStr
    CIDRIP: StrictStr | None = None
    EC2SecurityGroupName: StrictStr | None = None
    EC2SecurityGroupOwnerId: StrictStr | None = None
