from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .transcribe_category_properties import TranscribeCategoryProperties


class TranscribeGetCallAnalyticsCategoryResponse(BaseModel):
    CategoryProperties: TranscribeCategoryProperties | None = None
    ResponseMetadata: dict[str, Any] | None = None
