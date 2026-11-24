from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .ecr_public_tag import ECRPublicTag


class ECRPublicListTagsForResourceResponse(BaseModel):
    tags: list[ECRPublicTag] | None = None
    ResponseMetadata: dict[str, Any] | None = None
