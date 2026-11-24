from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class LightsailDisableAddOnRequest(BaseModel):
    addOnType: Literal['AutoSnapshot', 'StopInstanceOnIdle']
    resourceName: StrictStr
