from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictStr


class EC2ModifyVpcEndpointPayerResponsibilityRequest(BaseModel):
    VpcEndpointId: StrictStr
    PayerResponsibility: Literal['vpc-endpoint-account', 'resource-gateway-account', 'vpc-endpoint-service-account']
    Scope: Literal['vpc-endpoint-charges', 'resource-gateway-charges']
    DryRun: StrictBool | None = None
    ServiceId: StrictStr | None = None
