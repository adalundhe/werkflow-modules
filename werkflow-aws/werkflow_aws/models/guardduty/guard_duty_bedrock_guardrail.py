from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GuardDutyBedrockGuardrail(BaseModel):
    Arn: StrictStr | None = None
    Version: StrictStr | None = None
