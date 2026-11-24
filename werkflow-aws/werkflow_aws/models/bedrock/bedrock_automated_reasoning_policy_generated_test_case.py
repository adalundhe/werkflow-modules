from __future__ import annotations
from pydantic import BaseModel, StrictStr


class BedrockAutomatedReasoningPolicyGeneratedTestCase(BaseModel):
    queryContent: StrictStr | None = None
    guardContent: StrictStr | None = None
    expectedAggregatedFindingsResult: StrictStr | None = None
