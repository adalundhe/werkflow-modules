from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class EC2ModifyVerifiedAccessEndpointRdsOptions(BaseModel):
    SubnetIds: list[StrictStr] | None = None
    Port: StrictInt | None = None
    RdsEndpoint: StrictStr | None = None
