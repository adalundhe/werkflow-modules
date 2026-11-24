from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class KinesisAnalyticsParallelismConfigurationDescription(BaseModel):
    ConfigurationType: StrictStr | None = None
    Parallelism: StrictInt | None = None
    ParallelismPerKPU: StrictInt | None = None
    CurrentParallelism: StrictInt | None = None
    AutoScalingEnabled: StrictBool | None = None
