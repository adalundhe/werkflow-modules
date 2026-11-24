from __future__ import annotations
from pydantic import BaseModel, StrictStr


class StepFunctionsUntagResourceRequest(BaseModel):
    resourceArn: StrictStr
    tagKeys: list[StrictStr]
