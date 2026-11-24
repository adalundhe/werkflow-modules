from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .data_sync_ec2_config import DataSyncEc2Config
from .data_sync_tag_list_entry import DataSyncTagListEntry


class DataSyncCreateLocationEfsRequest(BaseModel):
    EfsFilesystemArn: StrictStr
    Ec2Config: DataSyncEc2Config
    Subdirectory: StrictStr | None = None
    Tags: list[DataSyncTagListEntry] | None = None
    AccessPointArn: StrictStr | None = None
    FileSystemAccessRoleArn: StrictStr | None = None
    InTransitEncryption: Literal['NONE', 'TLS1_2'] | None = None
