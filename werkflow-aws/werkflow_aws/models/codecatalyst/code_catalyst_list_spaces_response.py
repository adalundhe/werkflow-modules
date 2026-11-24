from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .code_catalyst_space_summary import CodeCatalystSpaceSummary


class CodeCatalystListSpacesResponse(BaseModel):
    nextToken: StrictStr | None = None
    items: list[CodeCatalystSpaceSummary] | None = None
    ResponseMetadata: dict[str, Any] | None = None
