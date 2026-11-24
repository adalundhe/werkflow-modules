from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .comprehend_toxic_labels import ComprehendToxicLabels


class ComprehendDetectToxicContentResponse(BaseModel):
    ResultList: list[ComprehendToxicLabels] | None = None
    ResponseMetadata: dict[str, Any] | None = None
