from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class SageMakerIdleSettings(BaseModel):
    LifecycleManagement: StrictStr | None = None
    IdleTimeoutInMinutes: StrictInt | None = None
    MinIdleTimeoutInMinutes: StrictInt | None = None
    MaxIdleTimeoutInMinutes: StrictInt | None = None
