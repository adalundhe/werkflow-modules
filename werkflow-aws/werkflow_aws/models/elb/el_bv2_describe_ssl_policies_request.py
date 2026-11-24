from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class ELBv2DescribeSSLPoliciesRequest(BaseModel):
    Names: list[StrictStr] | None = None
    Marker: StrictStr | None = None
    PageSize: StrictInt | None = None
    LoadBalancerType: Literal['application', 'network', 'gateway'] | None = None
