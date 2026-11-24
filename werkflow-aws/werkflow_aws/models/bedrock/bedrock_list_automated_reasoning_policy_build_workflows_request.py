from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class BedrockListAutomatedReasoningPolicyBuildWorkflowsRequest(BaseModel):
    policyArn: StrictStr
    nextToken: StrictStr | None = None
    maxResults: StrictInt | None = None
