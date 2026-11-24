from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class EC2CancelBundleTaskRequest(BaseModel):
    BundleId: StrictStr
    DryRun: StrictBool | None = None
