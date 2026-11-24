from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class BedrockListAutomatedReasoningPolicyTestResultsRequest(BaseModel):
    policyArn: StrictStr
    buildWorkflowId: StrictStr
    nextToken: StrictStr | None = None
    maxResults: StrictInt | None = None
