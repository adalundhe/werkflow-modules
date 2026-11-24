from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class SageMakerJobSummary(BaseModel):
    JobArn: StrictStr | None = None
    JobName: StrictStr | None = None
    JobCategory: StrictStr | None = None
    JobStatus: StrictStr | None = None
    JobSecondaryStatus: StrictStr | None = None
    CreationTime: datetime.datetime | StrictStr | None = None
    LastModifiedTime: datetime.datetime | StrictStr | None = None
    EndTime: datetime.datetime | StrictStr | None = None
