from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class CodeCatalystStopDevEnvironmentSessionResponse(BaseModel):
    spaceName: StrictStr | None = None
    projectName: StrictStr | None = None
    id: StrictStr | None = None
    sessionId: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
