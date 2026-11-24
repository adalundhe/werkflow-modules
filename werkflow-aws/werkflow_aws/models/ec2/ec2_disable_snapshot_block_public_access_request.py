from __future__ import annotations
from pydantic import BaseModel, StrictBool


class EC2DisableSnapshotBlockPublicAccessRequest(BaseModel):
    DryRun: StrictBool | None = None
