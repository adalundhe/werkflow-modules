from __future__ import annotations
from pydantic import BaseModel, StrictStr


class BedrockGetInferenceProfileRequest(BaseModel):
    inferenceProfileIdentifier: StrictStr
    projectIdentifier: StrictStr | None = None
