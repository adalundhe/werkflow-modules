from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .kendra_thesaurus_summary import KendraThesaurusSummary


class KendraListThesauriResponse(BaseModel):
    NextToken: StrictStr | None = None
    ThesaurusSummaryItems: list[KendraThesaurusSummary] | None = None
    ResponseMetadata: dict[str, Any] | None = None
