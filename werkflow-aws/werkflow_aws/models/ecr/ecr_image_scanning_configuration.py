from __future__ import annotations
from pydantic import BaseModel, StrictBool


class ECRImageScanningConfiguration(BaseModel):
    scanOnPush: StrictBool | None = None
