from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class CodeBuildListReportsResponse(BaseModel):
    nextToken: StrictStr | None = None
    reports: list[StrictStr] | None = None
    ResponseMetadata: dict[str, Any] | None = None
