from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .neptune_event_categories_map import NeptuneEventCategoriesMap


class NeptuneDescribeEventCategoriesResponse(BaseModel):
    EventCategoriesMapList: list[NeptuneEventCategoriesMap] | None = None
    ResponseMetadata: dict[str, Any] | None = None
