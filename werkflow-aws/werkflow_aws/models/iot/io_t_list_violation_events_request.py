from __future__ import annotations
import datetime
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class IoTListViolationEventsRequest(BaseModel):
    startTime: datetime.datetime | StrictStr
    endTime: datetime.datetime | StrictStr
    thingName: StrictStr | None = None
    securityProfileName: StrictStr | None = None
    behaviorCriteriaType: Literal['STATIC', 'STATISTICAL', 'MACHINE_LEARNING'] | None = None
    listSuppressedAlerts: StrictBool | None = None
    verificationState: Literal['FALSE_POSITIVE', 'BENIGN_POSITIVE', 'TRUE_POSITIVE', 'UNKNOWN'] | None = None
    nextToken: StrictStr | None = None
    maxResults: StrictInt | None = None
