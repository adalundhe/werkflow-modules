from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class GlueGetWorkflowRequest(BaseModel):
    Name: StrictStr
    IncludeGraph: StrictBool | None = None
