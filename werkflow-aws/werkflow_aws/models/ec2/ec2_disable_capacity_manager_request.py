from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class EC2DisableCapacityManagerRequest(BaseModel):
    DryRun: StrictBool | None = None
    ClientToken: StrictStr | None = None
