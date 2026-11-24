from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictInt


class KinesisAnalyticsParallelismConfigurationUpdate(BaseModel):
    ConfigurationTypeUpdate: Literal['DEFAULT', 'CUSTOM'] | None = None
    ParallelismUpdate: StrictInt | None = None
    ParallelismPerKPUUpdate: StrictInt | None = None
    AutoScalingEnabledUpdate: StrictBool | None = None
