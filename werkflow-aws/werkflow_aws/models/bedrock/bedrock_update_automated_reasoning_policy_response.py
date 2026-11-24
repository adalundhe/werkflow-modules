from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr


class BedrockUpdateAutomatedReasoningPolicyResponse(BaseModel):
    policyArn: StrictStr | None = None
    name: StrictStr | None = None
    definitionHash: StrictStr | None = None
    updatedAt: datetime.datetime | StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
