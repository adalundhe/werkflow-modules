from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .data_sync_tag_list_entry import DataSyncTagListEntry


class DataSyncCreateLocationFsxLustreRequest(BaseModel):
    FsxFilesystemArn: StrictStr
    SecurityGroupArns: list[StrictStr]
    Subdirectory: StrictStr | None = None
    Tags: list[DataSyncTagListEntry] | None = None
