from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .q_business_relevant_content import QBusinessRelevantContent


class QBusinessSearchRelevantContentResponse(BaseModel):
    relevantContent: list[QBusinessRelevantContent] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
