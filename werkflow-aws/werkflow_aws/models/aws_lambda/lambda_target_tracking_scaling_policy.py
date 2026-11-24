from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr


class LambdaTargetTrackingScalingPolicy(BaseModel):
    PredefinedMetricType: StrictStr | None = None
    TargetValue: StrictFloat | StrictInt | None = None
