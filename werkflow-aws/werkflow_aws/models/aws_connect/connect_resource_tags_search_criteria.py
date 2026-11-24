from __future__ import annotations
from pydantic import BaseModel
from .connect_tag_search_condition import ConnectTagSearchCondition


class ConnectResourceTagsSearchCriteria(BaseModel):
    TagSearchCondition: ConnectTagSearchCondition | None = None
