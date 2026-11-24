from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ECRRegisterPullTimeUpdateExclusionRequest(BaseModel):
    principalArn: StrictStr
