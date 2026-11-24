from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class SageMakerJobSecondaryStatusTransition(BaseModel):
    Status: StrictStr | None = None
    StartTime: datetime.datetime | StrictStr | None = None
    EndTime: datetime.datetime | StrictStr | None = None
    StatusMessage: StrictStr | None = None
