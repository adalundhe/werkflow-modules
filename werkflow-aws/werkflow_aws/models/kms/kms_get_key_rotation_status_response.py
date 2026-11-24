from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class KMSGetKeyRotationStatusResponse(BaseModel):
    KeyRotationEnabled: StrictBool | None = None
    KeyId: StrictStr | None = None
    RotationPeriodInDays: StrictInt | None = None
    NextRotationDate: datetime.datetime | StrictStr | None = None
    OnDemandRotationStartDate: datetime.datetime | StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
