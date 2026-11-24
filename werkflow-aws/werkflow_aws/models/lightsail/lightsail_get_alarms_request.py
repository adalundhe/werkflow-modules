from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LightsailGetAlarmsRequest(BaseModel):
    alarmName: StrictStr | None = None
    pageToken: StrictStr | None = None
    monitoredResourceName: StrictStr | None = None
