from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudWatchWallClockWindow(BaseModel):
    Timezone: StrictStr | None = None
