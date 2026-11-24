from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .translate_tag import TranslateTag


class TranslateListTagsForResourceResponse(BaseModel):
    Tags: list[TranslateTag] | None = None
    ResponseMetadata: dict[str, Any] | None = None
