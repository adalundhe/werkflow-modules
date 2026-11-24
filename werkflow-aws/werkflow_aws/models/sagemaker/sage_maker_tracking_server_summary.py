from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class SageMakerTrackingServerSummary(BaseModel):
    TrackingServerArn: StrictStr | None = None
    TrackingServerName: StrictStr | None = None
    CreationTime: datetime.datetime | StrictStr | None = None
    LastModifiedTime: datetime.datetime | StrictStr | None = None
    TrackingServerStatus: StrictStr | None = None
    IsActive: StrictStr | None = None
    MlflowVersion: StrictStr | None = None
