from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class DirectoryServiceLogSubscription(BaseModel):
    DirectoryId: StrictStr | None = None
    LogGroupName: StrictStr | None = None
    SubscriptionCreatedDateTime: datetime.datetime | StrictStr | None = None
