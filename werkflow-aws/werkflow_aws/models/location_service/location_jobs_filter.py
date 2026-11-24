from __future__ import annotations
from typing import Literal
from pydantic import BaseModel


class LocationJobsFilter(BaseModel):
    JobStatus: Literal['Pending', 'Running', 'Completed', 'Failed', 'Cancelling', 'Cancelled'] | None = None
