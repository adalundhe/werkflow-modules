from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AccessAnalyzerRdsDbSnapshotAttributeValue(BaseModel):
    accountIds: list[StrictStr] | None = None
