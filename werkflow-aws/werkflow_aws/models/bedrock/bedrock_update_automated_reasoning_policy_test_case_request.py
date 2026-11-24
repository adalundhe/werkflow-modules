from __future__ import annotations
import datetime
from typing import Literal
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr


class BedrockUpdateAutomatedReasoningPolicyTestCaseRequest(BaseModel):
    policyArn: StrictStr
    testCaseId: StrictStr
    guardContent: StrictStr
    lastUpdatedAt: datetime.datetime | StrictStr
    expectedAggregatedFindingsResult: Literal['VALID', 'INVALID', 'SATISFIABLE', 'IMPOSSIBLE', 'TRANSLATION_AMBIGUOUS', 'TOO_COMPLEX', 'NO_TRANSLATION']
    queryContent: StrictStr | None = None
    confidenceThreshold: StrictFloat | StrictInt | None = None
    clientRequestToken: StrictStr | None = None
