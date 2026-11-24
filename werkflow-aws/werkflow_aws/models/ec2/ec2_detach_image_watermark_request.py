from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class EC2DetachImageWatermarkRequest(BaseModel):
    ImageId: StrictStr
    WatermarkKey: StrictStr
    DryRun: StrictBool | None = None
