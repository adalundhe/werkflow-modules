from __future__ import annotations
from pydantic import BaseModel, StrictStr


class BedrockInferenceProfileModel(BaseModel):
    modelArn: StrictStr | None = None
