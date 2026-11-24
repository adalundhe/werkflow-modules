from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .data_sync_tag_list_entry import DataSyncTagListEntry


class DataSyncListTagsForResourceResponse(BaseModel):
    Tags: list[DataSyncTagListEntry] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
