from __future__ import annotations
from pydantic import BaseModel, StrictStr


class BedrockDeleteInferenceProfileRequest(BaseModel):
    inferenceProfileIdentifier: StrictStr
