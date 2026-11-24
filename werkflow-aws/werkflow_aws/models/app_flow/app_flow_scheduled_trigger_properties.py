from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr


class AppFlowScheduledTriggerProperties(BaseModel):
    scheduleExpression: StrictStr | None = None
    dataPullMode: StrictStr | None = None
    scheduleStartTime: datetime.datetime | StrictStr | None = None
    scheduleEndTime: datetime.datetime | StrictStr | None = None
    timezone: StrictStr | None = None
    scheduleOffset: StrictInt | None = None
    firstExecutionFrom: datetime.datetime | StrictStr | None = None
    flowErrorDeactivationThreshold: StrictInt | None = None
