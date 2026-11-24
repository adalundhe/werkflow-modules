from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class AmplifyJobSummary(BaseModel):
    jobArn: StrictStr | None = None
    jobId: StrictStr | None = None
    commitId: StrictStr | None = None
    commitMessage: StrictStr | None = None
    commitTime: datetime.datetime | StrictStr | None = None
    startTime: datetime.datetime | StrictStr | None = None
    status: StrictStr | None = None
    endTime: datetime.datetime | StrictStr | None = None
    jobType: StrictStr | None = None
    sourceUrl: StrictStr | None = None
    sourceUrlType: StrictStr | None = None
