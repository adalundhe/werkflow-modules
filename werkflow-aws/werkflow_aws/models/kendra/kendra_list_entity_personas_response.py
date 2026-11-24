from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .kendra_personas_summary import KendraPersonasSummary


class KendraListEntityPersonasResponse(BaseModel):
    SummaryItems: list[KendraPersonasSummary] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
