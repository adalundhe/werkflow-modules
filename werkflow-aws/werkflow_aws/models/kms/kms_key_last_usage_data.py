from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class KMSKeyLastUsageData(BaseModel):
    Operation: StrictStr | None = None
    Timestamp: datetime.datetime | StrictStr | None = None
    CloudTrailEventId: StrictStr | None = None
    KmsRequestId: StrictStr | None = None
