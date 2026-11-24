from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class CloudWatchAlarmContributor(BaseModel):
    ContributorId: StrictStr | None = None
    ContributorAttributes: dict[StrictStr, StrictStr] | None = None
    StateReason: StrictStr | None = None
    StateTransitionedTimestamp: datetime.datetime | StrictStr | None = None
