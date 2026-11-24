from __future__ import annotations
from typing import Literal
from pydantic import BaseModel


class EC2LaunchTemplateNetworkPerformanceOptionsRequest(BaseModel):
    BandwidthWeighting: Literal['default', 'vpc-1', 'ebs-1'] | None = None
