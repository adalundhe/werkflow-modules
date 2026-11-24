from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class EC2RestoreImageFromRecycleBinRequest(BaseModel):
    ImageId: StrictStr
    DryRun: StrictBool | None = None
