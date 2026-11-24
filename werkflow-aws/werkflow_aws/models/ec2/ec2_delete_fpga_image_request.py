from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class EC2DeleteFpgaImageRequest(BaseModel):
    FpgaImageId: StrictStr
    DryRun: StrictBool | None = None
