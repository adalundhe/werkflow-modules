from __future__ import annotations
from pydantic import BaseModel, StrictStr


class BedrockEvaluationPrecomputedRetrieveSourceConfig(BaseModel):
    ragSourceIdentifier: StrictStr | None = None
