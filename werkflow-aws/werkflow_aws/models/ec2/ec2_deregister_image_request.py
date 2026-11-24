from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class EC2DeregisterImageRequest(BaseModel):
    ImageId: StrictStr
    DeleteAssociatedSnapshots: StrictBool | None = None
    DryRun: StrictBool | None = None
