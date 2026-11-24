from __future__ import annotations
from pydantic import BaseModel, StrictStr


class BedrockEvaluationPrecomputedRetrieveAndGenerateSourceConfig(BaseModel):
    ragSourceIdentifier: StrictStr | None = None
