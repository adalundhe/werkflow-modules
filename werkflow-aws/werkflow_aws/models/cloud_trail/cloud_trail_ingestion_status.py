from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class CloudTrailIngestionStatus(BaseModel):
    LatestIngestionSuccessTime: datetime.datetime | StrictStr | None = None
    LatestIngestionSuccessEventID: StrictStr | None = None
    LatestIngestionErrorCode: StrictStr | None = None
    LatestIngestionAttemptTime: datetime.datetime | StrictStr | None = None
    LatestIngestionAttemptEventID: StrictStr | None = None
