from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr
from .kms_key_last_usage_data import KMSKeyLastUsageData


class KMSGetKeyLastUsageResponse(BaseModel):
    KeyId: StrictStr | None = None
    KeyLastUsage: KMSKeyLastUsageData | None = None
    TrackingStartDate: datetime.datetime | StrictStr | None = None
    KeyCreationDate: datetime.datetime | StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
