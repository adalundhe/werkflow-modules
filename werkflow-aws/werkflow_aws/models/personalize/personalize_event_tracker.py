from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class PersonalizeEventTracker(BaseModel):
    name: StrictStr | None = None
    eventTrackerArn: StrictStr | None = None
    accountId: StrictStr | None = None
    trackingId: StrictStr | None = None
    datasetGroupArn: StrictStr | None = None
    status: StrictStr | None = None
    creationDateTime: datetime.datetime | StrictStr | None = None
    lastUpdatedDateTime: datetime.datetime | StrictStr | None = None
