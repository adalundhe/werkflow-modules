from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class CodeBuildUpdateProjectVisibilityResponse(BaseModel):
    projectArn: StrictStr | None = None
    publicProjectAlias: StrictStr | None = None
    projectVisibility: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
