from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr


class RekognitionConnectedHomeSettingsForUpdate(BaseModel):
    Labels: list[StrictStr] | None = None
    MinConfidence: StrictFloat | StrictInt | None = None
