from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr


class CodeBuildTargetTrackingScalingConfiguration(BaseModel):
    metricType: StrictStr | None = None
    targetValue: StrictFloat | StrictInt | None = None
