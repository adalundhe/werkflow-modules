from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr


class BedrockPutEnforcedGuardrailConfigurationResponse(BaseModel):
    configId: StrictStr | None = None
    updatedAt: datetime.datetime | StrictStr | None = None
    updatedBy: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
