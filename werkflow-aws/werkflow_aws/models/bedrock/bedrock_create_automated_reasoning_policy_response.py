from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr


class BedrockCreateAutomatedReasoningPolicyResponse(BaseModel):
    policyArn: StrictStr | None = None
    version: StrictStr | None = None
    name: StrictStr | None = None
    description: StrictStr | None = None
    definitionHash: StrictStr | None = None
    createdAt: datetime.datetime | StrictStr | None = None
    updatedAt: datetime.datetime | StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
