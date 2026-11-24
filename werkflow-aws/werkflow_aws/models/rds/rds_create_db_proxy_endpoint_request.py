from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .rds_tag_model import RDSTagModel


class RDSCreateDBProxyEndpointRequest(BaseModel):
    DBProxyName: StrictStr
    DBProxyEndpointName: StrictStr
    VpcSubnetIds: list[StrictStr]
    VpcSecurityGroupIds: list[StrictStr] | None = None
    TargetRole: Literal['READ_WRITE', 'READ_ONLY'] | None = None
    Tags: list[RDSTagModel] | None = None
    EndpointNetworkType: Literal['IPV4', 'IPV6', 'DUAL'] | None = None
