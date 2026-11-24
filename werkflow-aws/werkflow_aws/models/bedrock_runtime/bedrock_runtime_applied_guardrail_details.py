from __future__ import annotations
from pydantic import BaseModel, StrictStr


class BedrockRuntimeAppliedGuardrailDetails(BaseModel):
    guardrailId: StrictStr | None = None
    guardrailVersion: StrictStr | None = None
    guardrailArn: StrictStr | None = None
    guardrailOrigin: list[StrictStr] | None = None
    guardrailOwnership: StrictStr | None = None
