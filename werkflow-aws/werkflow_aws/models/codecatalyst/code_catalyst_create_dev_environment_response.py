from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class CodeCatalystCreateDevEnvironmentResponse(BaseModel):
    spaceName: StrictStr | None = None
    projectName: StrictStr | None = None
    id: StrictStr | None = None
    vpcConnectionName: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
