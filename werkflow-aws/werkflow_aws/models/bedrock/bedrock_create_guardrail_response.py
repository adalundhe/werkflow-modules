from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr


class BedrockCreateGuardrailResponse(BaseModel):
    guardrailId: StrictStr | None = None
    guardrailArn: StrictStr | None = None
    version: StrictStr | None = None
    createdAt: datetime.datetime | StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
