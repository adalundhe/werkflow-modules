from __future__ import annotations
from pydantic import BaseModel, StrictStr


class BedrockEvaluationRagConfigSummary(BaseModel):
    bedrockKnowledgeBaseIdentifiers: list[StrictStr] | None = None
    precomputedRagSourceIdentifiers: list[StrictStr] | None = None
