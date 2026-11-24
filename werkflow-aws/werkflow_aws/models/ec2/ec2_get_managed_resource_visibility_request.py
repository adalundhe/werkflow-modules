from __future__ import annotations
from pydantic import BaseModel, StrictBool


class EC2GetManagedResourceVisibilityRequest(BaseModel):
    DryRun: StrictBool | None = None
