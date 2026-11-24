from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .bedrock_automated_reasoning_policy_statement_location import BedrockAutomatedReasoningPolicyStatementLocation


class BedrockAutomatedReasoningPolicyAtomicStatement(BaseModel):
    id: StrictStr | None = None
    text: StrictStr | None = None
    location: BedrockAutomatedReasoningPolicyStatementLocation | None = None
