from __future__ import annotations
from pydantic import BaseModel, StrictStr


class FSxSnapmirrorExportedSnapshot(BaseModel):
    SnapshotId: StrictStr | None = None
    SnapshotName: StrictStr | None = None
