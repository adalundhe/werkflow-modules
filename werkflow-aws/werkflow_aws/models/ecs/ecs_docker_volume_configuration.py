from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class ECSDockerVolumeConfiguration(BaseModel):
    scope: StrictStr | None = None
    autoprovision: StrictBool | None = None
    driver: StrictStr | None = None
    driverOpts: dict[StrictStr, StrictStr] | None = None
    labels: dict[StrictStr, StrictStr] | None = None
