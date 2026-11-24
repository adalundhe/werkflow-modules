from __future__ import annotations
import datetime
from typing import Literal
from pydantic import BaseModel, StrictStr


class ComprehendDatasetFilter(BaseModel):
    Status: Literal['CREATING', 'COMPLETED', 'FAILED'] | None = None
    DatasetType: Literal['TRAIN', 'TEST'] | None = None
    CreationTimeAfter: datetime.datetime | StrictStr | None = None
    CreationTimeBefore: datetime.datetime | StrictStr | None = None
