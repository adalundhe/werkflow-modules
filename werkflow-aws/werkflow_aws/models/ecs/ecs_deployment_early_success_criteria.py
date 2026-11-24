from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class ECSDeploymentEarlySuccessCriteria(BaseModel):
    enable: StrictBool | None = None
    healthyPercent: StrictInt | None = None
    sourceServiceRevisionCleanup: StrictStr | None = None
