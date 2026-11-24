from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class BedrockUpdateAutomatedReasoningPolicyTestCaseResponse(BaseModel):
    policyArn: StrictStr | None = None
    testCaseId: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
