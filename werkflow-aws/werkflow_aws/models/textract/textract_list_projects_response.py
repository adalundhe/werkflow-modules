from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .textract_project_summary import TextractProjectSummary


class TextractListProjectsResponse(BaseModel):
    Projects: list[TextractProjectSummary] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
