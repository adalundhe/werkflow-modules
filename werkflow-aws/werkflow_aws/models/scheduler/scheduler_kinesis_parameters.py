from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SchedulerKinesisParameters(BaseModel):
    PartitionKey: StrictStr | None = None
