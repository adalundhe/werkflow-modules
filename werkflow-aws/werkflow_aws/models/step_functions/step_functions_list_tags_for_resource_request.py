from __future__ import annotations
from pydantic import BaseModel, StrictStr


class StepFunctionsListTagsForResourceRequest(BaseModel):
    resourceArn: StrictStr
