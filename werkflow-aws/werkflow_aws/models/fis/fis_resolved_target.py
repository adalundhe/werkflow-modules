from __future__ import annotations
from pydantic import BaseModel, StrictStr


class FISResolvedTarget(BaseModel):
    resourceType: StrictStr | None = None
    targetName: StrictStr | None = None
    targetInformation: dict[StrictStr, StrictStr] | None = None
