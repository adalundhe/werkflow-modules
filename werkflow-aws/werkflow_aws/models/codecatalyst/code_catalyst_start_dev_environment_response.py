from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class CodeCatalystStartDevEnvironmentResponse(BaseModel):
    spaceName: StrictStr | None = None
    projectName: StrictStr | None = None
    id: StrictStr | None = None
    status: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
