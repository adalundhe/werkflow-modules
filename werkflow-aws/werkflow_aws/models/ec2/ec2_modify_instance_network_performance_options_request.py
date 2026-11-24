from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictStr


class EC2ModifyInstanceNetworkPerformanceOptionsRequest(BaseModel):
    InstanceId: StrictStr
    BandwidthWeighting: Literal['default', 'vpc-1', 'ebs-1']
    DryRun: StrictBool | None = None
