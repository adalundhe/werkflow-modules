from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .data_sync_tag_list_entry import DataSyncTagListEntry


class DataSyncTagResourceRequest(BaseModel):
    ResourceArn: StrictStr
    Tags: list[DataSyncTagListEntry]
