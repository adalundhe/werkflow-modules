from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class ComprehendFlywheelSummary(BaseModel):
    FlywheelArn: StrictStr | None = None
    ActiveModelArn: StrictStr | None = None
    DataLakeS3Uri: StrictStr | None = None
    Status: StrictStr | None = None
    ModelType: StrictStr | None = None
    Message: StrictStr | None = None
    CreationTime: datetime.datetime | StrictStr | None = None
    LastModifiedTime: datetime.datetime | StrictStr | None = None
    LatestFlywheelIteration: StrictStr | None = None
