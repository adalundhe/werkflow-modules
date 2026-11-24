from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictFloat, StrictInt, StrictStr


class BedrockRuntimeGuardrailContextualGroundingFilter(BaseModel):
    type: StrictStr | None = None
    threshold: StrictFloat | StrictInt | None = None
    score: StrictFloat | StrictInt | None = None
    action: StrictStr | None = None
    detected: StrictBool | None = None
