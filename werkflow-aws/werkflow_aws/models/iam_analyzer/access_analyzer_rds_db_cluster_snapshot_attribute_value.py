from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AccessAnalyzerRdsDbClusterSnapshotAttributeValue(BaseModel):
    accountIds: list[StrictStr] | None = None
