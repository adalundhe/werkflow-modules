from __future__ import annotations
from pydantic import BaseModel, StrictStr


class BedrockGuardrailCrossRegionDetails(BaseModel):
    guardrailProfileId: StrictStr | None = None
    guardrailProfileArn: StrictStr | None = None
