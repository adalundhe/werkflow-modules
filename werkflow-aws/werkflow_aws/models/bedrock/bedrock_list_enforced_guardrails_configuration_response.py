from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .bedrock_account_enforced_guardrail_output_configuration import BedrockAccountEnforcedGuardrailOutputConfiguration


class BedrockListEnforcedGuardrailsConfigurationResponse(BaseModel):
    guardrailsConfig: list[BedrockAccountEnforcedGuardrailOutputConfiguration] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
