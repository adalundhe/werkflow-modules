from __future__ import annotations
from pydantic import BaseModel, StrictStr


class IoTCloudwatchAlarmAction(BaseModel):
    roleArn: StrictStr | None = None
    alarmName: StrictStr | None = None
    stateReason: StrictStr | None = None
    stateValue: StrictStr | None = None
