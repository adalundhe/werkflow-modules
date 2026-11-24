from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .code_catalyst_project_summary import CodeCatalystProjectSummary


class CodeCatalystListProjectsResponse(BaseModel):
    nextToken: StrictStr | None = None
    items: list[CodeCatalystProjectSummary] | None = None
    ResponseMetadata: dict[str, Any] | None = None
