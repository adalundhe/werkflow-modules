from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class EC2VerifiedAccessEndpointRdsOptions(BaseModel):
    Protocol: StrictStr | None = None
    Port: StrictInt | None = None
    RdsDbInstanceArn: StrictStr | None = None
    RdsDbClusterArn: StrictStr | None = None
    RdsDbProxyArn: StrictStr | None = None
    RdsEndpoint: StrictStr | None = None
    SubnetIds: list[StrictStr] | None = None
