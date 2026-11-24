from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .dms_event_category_group import DMSEventCategoryGroup


class DMSDescribeEventCategoriesResponse(BaseModel):
    EventCategoryGroupList: list[DMSEventCategoryGroup] | None = None
    ResponseMetadata: dict[str, Any] | None = None
