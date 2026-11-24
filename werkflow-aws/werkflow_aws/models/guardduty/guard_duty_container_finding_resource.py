from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GuardDutyContainerFindingResource(BaseModel):
    Image: StrictStr | None = None
    ImageUid: StrictStr | None = None
