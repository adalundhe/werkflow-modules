from __future__ import annotations
import datetime
from typing import Literal
from pydantic import BaseModel, StrictStr


class ComprehendFlywheelFilter(BaseModel):
    Status: Literal['CREATING', 'ACTIVE', 'UPDATING', 'DELETING', 'FAILED'] | None = None
    CreationTimeAfter: datetime.datetime | StrictStr | None = None
    CreationTimeBefore: datetime.datetime | StrictStr | None = None
