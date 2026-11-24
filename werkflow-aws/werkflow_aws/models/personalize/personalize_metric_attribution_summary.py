from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class PersonalizeMetricAttributionSummary(BaseModel):
    name: StrictStr | None = None
    metricAttributionArn: StrictStr | None = None
    status: StrictStr | None = None
    creationDateTime: datetime.datetime | StrictStr | None = None
    lastUpdatedDateTime: datetime.datetime | StrictStr | None = None
    failureReason: StrictStr | None = None
