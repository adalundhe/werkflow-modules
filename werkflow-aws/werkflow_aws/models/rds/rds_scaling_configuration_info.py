from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class RDSScalingConfigurationInfo(BaseModel):
    MinCapacity: StrictInt | None = None
    MaxCapacity: StrictInt | None = None
    AutoPause: StrictBool | None = None
    SecondsUntilAutoPause: StrictInt | None = None
    TimeoutAction: StrictStr | None = None
    SecondsBeforeTimeout: StrictInt | None = None
