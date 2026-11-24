from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AccessAnalyzerEbsSnapshotConfiguration(BaseModel):
    userIds: list[StrictStr] | None = None
    groups: list[StrictStr] | None = None
    kmsKeyId: StrictStr | None = None
