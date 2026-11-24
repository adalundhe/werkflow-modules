from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class ComprehendFlywheelIterationFilter(BaseModel):
    CreationTimeAfter: datetime.datetime | StrictStr | None = None
    CreationTimeBefore: datetime.datetime | StrictStr | None = None
