from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class CodeBuildListSharedProjectsResponse(BaseModel):
    nextToken: StrictStr | None = None
    projects: list[StrictStr] | None = None
    ResponseMetadata: dict[str, Any] | None = None
