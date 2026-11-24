from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .guard_duty_bedrock_guardrail import GuardDutyBedrockGuardrail
from .guard_duty_content_policy_filter import GuardDutyContentPolicyFilter


class GuardDutyBedrockGuardrailDetails(BaseModel):
    GuardrailArn: StrictStr | None = None
    GuardrailVersion: StrictStr | None = None
    Guardrails: list[GuardDutyBedrockGuardrail] | None = None
    GuardrailAction: StrictStr | None = None
    GuardrailSource: StrictStr | None = None
    ContentPolicyFilters: list[GuardDutyContentPolicyFilter] | None = None
