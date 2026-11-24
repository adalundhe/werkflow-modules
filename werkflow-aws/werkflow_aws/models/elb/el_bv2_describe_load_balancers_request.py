from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class ELBv2DescribeLoadBalancersRequest(BaseModel):
    LoadBalancerArns: list[StrictStr] | None = None
    Names: list[StrictStr] | None = None
    Marker: StrictStr | None = None
    PageSize: StrictInt | None = None
