from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr


class BedrockCreateAutomatedReasoningPolicyTestCaseRequest(BaseModel):
    policyArn: StrictStr
    guardContent: StrictStr
    expectedAggregatedFindingsResult: Literal['VALID', 'INVALID', 'SATISFIABLE', 'IMPOSSIBLE', 'TRANSLATION_AMBIGUOUS', 'TOO_COMPLEX', 'NO_TRANSLATION']
    queryContent: StrictStr | None = None
    clientRequestToken: StrictStr | None = None
    confidenceThreshold: StrictFloat | StrictInt | None = None
