from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr
from .wa_fv2_time_window import WAFv2TimeWindow


class WAFv2GetSampledRequestsRequest(BaseModel):
    WebAclArn: StrictStr
    RuleMetricName: StrictStr
    Scope: Literal['CLOUDFRONT', 'REGIONAL']
    TimeWindow: WAFv2TimeWindow
    MaxItems: StrictInt
