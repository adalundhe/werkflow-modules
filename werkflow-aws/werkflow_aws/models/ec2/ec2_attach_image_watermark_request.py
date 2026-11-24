from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class EC2AttachImageWatermarkRequest(BaseModel):
    ImageId: StrictStr
    WatermarkName: StrictStr
    DryRun: StrictBool | None = None
