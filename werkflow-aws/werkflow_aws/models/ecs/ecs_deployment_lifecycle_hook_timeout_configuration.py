from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class ECSDeploymentLifecycleHookTimeoutConfiguration(BaseModel):
    timeoutInMinutes: StrictInt | None = None
    action: StrictStr | None = None
