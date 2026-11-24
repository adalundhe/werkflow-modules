from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GuardDutyEbsSnapshotDetails(BaseModel):
    SnapshotArn: StrictStr | None = None
