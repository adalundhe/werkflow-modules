from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class CodeCatalystCreateSourceRepositoryResponse(BaseModel):
    spaceName: StrictStr | None = None
    projectName: StrictStr | None = None
    name: StrictStr | None = None
    description: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
