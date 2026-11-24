from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class EC2CreateVerifiedAccessEndpointRdsOptions(BaseModel):
    Protocol: Literal['http', 'https', 'tcp'] | None = None
    Port: StrictInt | None = None
    RdsDbInstanceArn: StrictStr | None = None
    RdsDbClusterArn: StrictStr | None = None
    RdsDbProxyArn: StrictStr | None = None
    RdsEndpoint: StrictStr | None = None
    SubnetIds: list[StrictStr] | None = None
