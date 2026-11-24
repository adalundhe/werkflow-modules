from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudWatchSchedule(BaseModel):
    Expression: StrictStr | None = None
    Duration: StrictStr | None = None
    Timezone: StrictStr | None = None
