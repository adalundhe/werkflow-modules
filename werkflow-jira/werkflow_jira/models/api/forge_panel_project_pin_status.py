from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class ForgePanelProjectPinStatus(BaseModel):
    error: StrictStr | None = None
    pinned: StrictBool | None = None
    pinnedAt: StrictInt | None = None
    projectIdOrKey: StrictStr | None = None
