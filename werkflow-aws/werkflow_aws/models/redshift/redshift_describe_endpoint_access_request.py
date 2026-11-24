from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class RedshiftDescribeEndpointAccessRequest(BaseModel):
    ClusterIdentifier: StrictStr | None = None
    ResourceOwner: StrictStr | None = None
    EndpointName: StrictStr | None = None
    VpcId: StrictStr | None = None
    MaxRecords: StrictInt | None = None
    Marker: StrictStr | None = None
