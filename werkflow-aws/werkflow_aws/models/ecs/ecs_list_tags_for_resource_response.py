from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .ecs_tag import ECSTag


class ECSListTagsForResourceResponse(BaseModel):
    tags: list[ECSTag] | None = None
    ResponseMetadata: dict[str, Any] | None = None
