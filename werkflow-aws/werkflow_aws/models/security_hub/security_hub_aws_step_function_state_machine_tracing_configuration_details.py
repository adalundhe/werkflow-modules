from __future__ import annotations
from pydantic import BaseModel, StrictBool


class SecurityHubAwsStepFunctionStateMachineTracingConfigurationDetails(BaseModel):
    Enabled: StrictBool | None = None
