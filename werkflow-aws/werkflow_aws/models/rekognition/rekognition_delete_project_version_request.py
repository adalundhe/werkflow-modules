from __future__ import annotations
from pydantic import BaseModel, StrictStr


class RekognitionDeleteProjectVersionRequest(BaseModel):
    ProjectVersionArn: StrictStr
