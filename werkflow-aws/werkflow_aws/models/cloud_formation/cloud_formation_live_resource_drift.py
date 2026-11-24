from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class CloudFormationLiveResourceDrift(BaseModel):
    PreviousValue: StrictStr | None = None
    ActualValue: StrictStr | None = None
    DriftDetectionTimestamp: datetime.datetime | StrictStr | None = None
