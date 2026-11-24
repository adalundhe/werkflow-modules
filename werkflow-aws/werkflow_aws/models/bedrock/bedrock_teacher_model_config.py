from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class BedrockTeacherModelConfig(BaseModel):
    teacherModelIdentifier: StrictStr | None = None
    maxResponseLengthForInference: StrictInt | None = None
