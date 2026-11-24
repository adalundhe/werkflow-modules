from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class BedrockListAutomatedReasoningPoliciesRequest(BaseModel):
    policyArn: StrictStr | None = None
    nextToken: StrictStr | None = None
    maxResults: StrictInt | None = None
