from __future__ import annotations
from pydantic import BaseModel, StrictStr


class BedrockAutomatedReasoningPolicyIngestContentAnnotation(BaseModel):
    content: StrictStr | None = None
