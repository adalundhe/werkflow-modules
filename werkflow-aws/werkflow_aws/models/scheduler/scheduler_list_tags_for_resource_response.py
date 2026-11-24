from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .scheduler_tag import SchedulerTag


class SchedulerListTagsForResourceResponse(BaseModel):
    Tags: list[SchedulerTag] | None = None
    ResponseMetadata: dict[str, Any] | None = None
