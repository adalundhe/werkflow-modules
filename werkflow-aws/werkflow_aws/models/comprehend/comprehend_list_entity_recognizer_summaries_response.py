from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .comprehend_entity_recognizer_summary import ComprehendEntityRecognizerSummary


class ComprehendListEntityRecognizerSummariesResponse(BaseModel):
    EntityRecognizerSummariesList: list[ComprehendEntityRecognizerSummary] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
