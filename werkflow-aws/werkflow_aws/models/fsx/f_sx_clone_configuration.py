from __future__ import annotations
from pydantic import BaseModel, StrictStr


class FSxCloneConfiguration(BaseModel):
    ParentVolumeId: StrictStr | None = None
    SnapshotId: StrictStr | None = None
