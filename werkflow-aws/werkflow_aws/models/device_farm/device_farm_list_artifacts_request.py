from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class DeviceFarmListArtifactsRequest(BaseModel):
    arn: StrictStr
    type: Literal['SCREENSHOT', 'FILE', 'LOG']
    nextToken: StrictStr | None = None
