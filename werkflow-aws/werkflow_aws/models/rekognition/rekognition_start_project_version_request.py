from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class RekognitionStartProjectVersionRequest(BaseModel):
    ProjectVersionArn: StrictStr
    MinInferenceUnits: StrictInt
    MaxInferenceUnits: StrictInt | None = None
