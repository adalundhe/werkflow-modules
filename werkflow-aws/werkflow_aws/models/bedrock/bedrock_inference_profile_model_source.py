from __future__ import annotations
from pydantic import BaseModel, StrictStr


class BedrockInferenceProfileModelSource(BaseModel):
    copyFrom: StrictStr | None = None
