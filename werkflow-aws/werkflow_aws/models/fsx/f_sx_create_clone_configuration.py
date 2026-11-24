from __future__ import annotations
from pydantic import BaseModel, StrictStr


class FSxCreateCloneConfiguration(BaseModel):
    ParentVolumeId: StrictStr
    SnapshotId: StrictStr | None = None
