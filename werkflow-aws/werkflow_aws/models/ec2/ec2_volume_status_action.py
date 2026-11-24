from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EC2VolumeStatusAction(BaseModel):
    Code: StrictStr | None = None
    Description: StrictStr | None = None
    EventId: StrictStr | None = None
    EventType: StrictStr | None = None
