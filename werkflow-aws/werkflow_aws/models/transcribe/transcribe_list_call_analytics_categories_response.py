from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .transcribe_category_properties import TranscribeCategoryProperties


class TranscribeListCallAnalyticsCategoriesResponse(BaseModel):
    NextToken: StrictStr | None = None
    Categories: list[TranscribeCategoryProperties] | None = None
    ResponseMetadata: dict[str, Any] | None = None
