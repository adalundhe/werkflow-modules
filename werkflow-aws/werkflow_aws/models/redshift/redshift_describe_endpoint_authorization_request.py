from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class RedshiftDescribeEndpointAuthorizationRequest(BaseModel):
    ClusterIdentifier: StrictStr | None = None
    Account: StrictStr | None = None
    Grantee: StrictBool | None = None
    MaxRecords: StrictInt | None = None
    Marker: StrictStr | None = None
