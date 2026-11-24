from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class QuickSightEffectiveLimit(BaseModel):
    resourceType: StrictStr | None = None
    limitValue: StrictInt | None = None
    limitUnit: StrictStr | None = None
    source: StrictStr | None = None
    profileId: StrictStr | None = None
