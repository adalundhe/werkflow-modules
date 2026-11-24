from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr


class BedrockAutomatedReasoningPolicyTestCase(BaseModel):
    testCaseId: StrictStr | None = None
    guardContent: StrictStr | None = None
    queryContent: StrictStr | None = None
    expectedAggregatedFindingsResult: StrictStr | None = None
    createdAt: datetime.datetime | StrictStr | None = None
    updatedAt: datetime.datetime | StrictStr | None = None
    confidenceThreshold: StrictFloat | StrictInt | None = None
