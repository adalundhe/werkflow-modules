from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DataSyncPrivateLinkConfig(BaseModel):
    VpcEndpointId: StrictStr | None = None
    PrivateLinkEndpoint: StrictStr | None = None
    SubnetArns: list[StrictStr] | None = None
    SecurityGroupArns: list[StrictStr] | None = None
