from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class LexGetTestExecutionArtifactsUrlResponse(BaseModel):
    testExecutionId: StrictStr | None = None
    downloadArtifactsUrl: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
