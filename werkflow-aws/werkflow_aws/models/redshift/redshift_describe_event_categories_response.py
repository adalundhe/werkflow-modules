from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .redshift_event_categories_map import RedshiftEventCategoriesMap


class RedshiftDescribeEventCategoriesResponse(BaseModel):
    EventCategoriesMapList: list[RedshiftEventCategoriesMap] | None = None
    ResponseMetadata: dict[str, Any] | None = None
