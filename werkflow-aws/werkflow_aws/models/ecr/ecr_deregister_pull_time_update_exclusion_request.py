from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ECRDeregisterPullTimeUpdateExclusionRequest(BaseModel):
    principalArn: StrictStr
