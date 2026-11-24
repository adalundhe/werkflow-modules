from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class ELBv2DescribeTargetGroupsRequest(BaseModel):
    LoadBalancerArn: StrictStr | None = None
    TargetGroupArns: list[StrictStr] | None = None
    Names: list[StrictStr] | None = None
    Marker: StrictStr | None = None
    PageSize: StrictInt | None = None
