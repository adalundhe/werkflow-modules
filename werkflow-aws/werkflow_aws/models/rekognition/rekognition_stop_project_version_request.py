from __future__ import annotations
from pydantic import BaseModel, StrictStr


class RekognitionStopProjectVersionRequest(BaseModel):
    ProjectVersionArn: StrictStr
