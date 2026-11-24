from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class CodeBuildListReportGroupsResponse(BaseModel):
    nextToken: StrictStr | None = None
    reportGroups: list[StrictStr] | None = None
    ResponseMetadata: dict[str, Any] | None = None
