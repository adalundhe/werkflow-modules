from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EMRDeleteStudioRequest(BaseModel):
    StudioId: StrictStr
