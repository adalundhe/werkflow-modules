from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr
from .bedrock_automated_reasoning_policy_statement_reference import BedrockAutomatedReasoningPolicyStatementReference


class BedrockAutomatedReasoningPolicyRuleReport(BaseModel):
    rule: StrictStr | None = None
    groundingStatements: list[BedrockAutomatedReasoningPolicyStatementReference] | None = None
    groundingJustifications: list[StrictStr] | None = None
    accuracyScore: StrictFloat | StrictInt | None = None
    accuracyJustification: StrictStr | None = None
