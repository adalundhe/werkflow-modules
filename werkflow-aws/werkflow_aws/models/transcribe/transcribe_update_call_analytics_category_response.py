from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .transcribe_category_properties import TranscribeCategoryProperties


class TranscribeUpdateCallAnalyticsCategoryResponse(BaseModel):
    CategoryProperties: TranscribeCategoryProperties | None = None
    ResponseMetadata: dict[str, Any] | None = None
