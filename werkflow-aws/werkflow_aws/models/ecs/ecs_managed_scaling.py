from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class ECSManagedScaling(BaseModel):
    status: StrictStr | None = None
    targetCapacity: StrictInt | None = None
    minimumScalingStepSize: StrictInt | None = None
    maximumScalingStepSize: StrictInt | None = None
    instanceWarmupPeriod: StrictInt | None = None
