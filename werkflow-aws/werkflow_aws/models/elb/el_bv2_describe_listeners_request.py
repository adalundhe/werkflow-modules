from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class ELBv2DescribeListenersRequest(BaseModel):
    LoadBalancerArn: StrictStr | None = None
    ListenerArns: list[StrictStr] | None = None
    Marker: StrictStr | None = None
    PageSize: StrictInt | None = None
