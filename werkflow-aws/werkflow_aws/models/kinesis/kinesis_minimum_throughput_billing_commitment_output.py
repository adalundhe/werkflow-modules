from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class KinesisMinimumThroughputBillingCommitmentOutput(BaseModel):
    Status: StrictStr | None = None
    StartedAt: datetime.datetime | StrictStr | None = None
    EndedAt: datetime.datetime | StrictStr | None = None
    EarliestAllowedEndAt: datetime.datetime | StrictStr | None = None
