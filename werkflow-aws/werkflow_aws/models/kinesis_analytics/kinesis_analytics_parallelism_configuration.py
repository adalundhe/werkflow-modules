from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictInt


class KinesisAnalyticsParallelismConfiguration(BaseModel):
    ConfigurationType: Literal['DEFAULT', 'CUSTOM']
    Parallelism: StrictInt | None = None
    ParallelismPerKPU: StrictInt | None = None
    AutoScalingEnabled: StrictBool | None = None
