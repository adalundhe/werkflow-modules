from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class ConnectUpdatePromptResponse(BaseModel):
    PromptARN: StrictStr | None = None
    PromptId: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
