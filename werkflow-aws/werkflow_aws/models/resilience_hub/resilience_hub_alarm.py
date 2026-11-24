from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ResilienceHubAlarm(BaseModel):
    alarmArn: StrictStr | None = None
    source: StrictStr | None = None
