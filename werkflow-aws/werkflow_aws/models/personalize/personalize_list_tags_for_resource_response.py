from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .personalize_tag import PersonalizeTag


class PersonalizeListTagsForResourceResponse(BaseModel):
    tags: list[PersonalizeTag] | None = None
    ResponseMetadata: dict[str, Any] | None = None
