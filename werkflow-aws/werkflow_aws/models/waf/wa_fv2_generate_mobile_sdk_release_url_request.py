from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class WAFv2GenerateMobileSdkReleaseUrlRequest(BaseModel):
    Platform: Literal['IOS', 'ANDROID']
    ReleaseVersion: StrictStr
