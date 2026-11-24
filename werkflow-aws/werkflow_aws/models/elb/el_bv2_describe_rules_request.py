from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class ELBv2DescribeRulesRequest(BaseModel):
    ListenerArn: StrictStr | None = None
    RuleArns: list[StrictStr] | None = None
    Marker: StrictStr | None = None
    PageSize: StrictInt | None = None
