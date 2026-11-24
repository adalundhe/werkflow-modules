from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GlueDeleteWorkflowRequest(BaseModel):
    Name: StrictStr
