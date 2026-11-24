from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictStr


class EC2ModifySnapshotTierRequest(BaseModel):
    SnapshotId: StrictStr
    StorageTier: Literal['archive'] | None = None
    DryRun: StrictBool | None = None
