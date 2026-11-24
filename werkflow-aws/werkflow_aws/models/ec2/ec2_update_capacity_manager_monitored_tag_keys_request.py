from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class EC2UpdateCapacityManagerMonitoredTagKeysRequest(BaseModel):
    ActivateTagKeys: list[StrictStr] | None = None
    DeactivateTagKeys: list[StrictStr] | None = None
    DryRun: StrictBool | None = None
    ClientToken: StrictStr | None = None
