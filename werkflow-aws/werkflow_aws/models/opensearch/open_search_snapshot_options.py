from __future__ import annotations
from pydantic import BaseModel, StrictInt


class OpenSearchSnapshotOptions(BaseModel):
    AutomatedSnapshotStartHour: StrictInt | None = None
