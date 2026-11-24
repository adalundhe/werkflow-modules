from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AppRunnerListTagsForResourceRequest(BaseModel):
    ResourceArn: StrictStr
