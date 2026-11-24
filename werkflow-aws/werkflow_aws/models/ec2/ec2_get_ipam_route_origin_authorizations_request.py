from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class EC2GetIpamRouteOriginAuthorizationsRequest(BaseModel):
    IpamInternetRegistryAssociationId: StrictStr
    DryRun: StrictBool | None = None
    Cidr: StrictStr | None = None
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
