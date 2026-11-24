from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EMRDescribeStudioRequest(BaseModel):
    StudioId: StrictStr
