from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictFloat, StrictInt, StrictStr


class BedrockGuardrailContextualGroundingFilter(BaseModel):
    type: StrictStr | None = None
    threshold: StrictFloat | StrictInt | None = None
    action: StrictStr | None = None
    enabled: StrictBool | None = None
