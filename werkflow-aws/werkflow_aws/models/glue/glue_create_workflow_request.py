from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class GlueCreateWorkflowRequest(BaseModel):
    Name: StrictStr
    Description: StrictStr | None = None
    DefaultRunProperties: dict[StrictStr, StrictStr] | None = None
    Tags: dict[StrictStr, StrictStr] | None = None
    MaxConcurrentRuns: StrictInt | None = None
