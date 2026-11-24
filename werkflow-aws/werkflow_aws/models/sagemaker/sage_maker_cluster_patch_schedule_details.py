from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class SageMakerClusterPatchScheduleDetails(BaseModel):
    NextPatchDate: datetime.datetime | StrictStr | None = None
