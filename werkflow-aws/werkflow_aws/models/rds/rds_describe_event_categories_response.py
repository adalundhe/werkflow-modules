from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .rds_event_categories_map import RDSEventCategoriesMap


class RDSDescribeEventCategoriesResponse(BaseModel):
    EventCategoriesMapList: list[RDSEventCategoriesMap] | None = None
    ResponseMetadata: dict[str, Any] | None = None
