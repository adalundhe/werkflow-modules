from __future__ import annotations
from pydantic import BaseModel, StrictStr


class RedshiftCreateEndpointAccessRequest(BaseModel):
    EndpointName: StrictStr
    SubnetGroupName: StrictStr
    ClusterIdentifier: StrictStr | None = None
    ResourceOwner: StrictStr | None = None
    VpcSecurityGroupIds: list[StrictStr] | None = None
