from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .kendra_faq_summary import KendraFaqSummary


class KendraListFaqsResponse(BaseModel):
    NextToken: StrictStr | None = None
    FaqSummaryItems: list[KendraFaqSummary] | None = None
    ResponseMetadata: dict[str, Any] | None = None
