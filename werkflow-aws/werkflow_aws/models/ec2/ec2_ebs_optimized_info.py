from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt


class EC2EbsOptimizedInfo(BaseModel):
    BaselineBandwidthInMbps: StrictInt | None = None
    BaselineThroughputInMBps: StrictFloat | StrictInt | None = None
    BaselineIops: StrictInt | None = None
    MaximumBandwidthInMbps: StrictInt | None = None
    MaximumThroughputInMBps: StrictFloat | StrictInt | None = None
    MaximumIops: StrictInt | None = None
