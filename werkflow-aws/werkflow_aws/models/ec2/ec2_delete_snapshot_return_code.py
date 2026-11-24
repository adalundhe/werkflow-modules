from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EC2DeleteSnapshotReturnCode(BaseModel):
    SnapshotId: StrictStr | None = None
    ReturnCode: StrictStr | None = None
