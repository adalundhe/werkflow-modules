from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr
from .data_sync_nfs_mount_options import DataSyncNfsMountOptions
from .data_sync_on_prem_config import DataSyncOnPremConfig


class DataSyncDescribeLocationNfsResponse(BaseModel):
    LocationArn: StrictStr | None = None
    LocationUri: StrictStr | None = None
    OnPremConfig: DataSyncOnPremConfig | None = None
    MountOptions: DataSyncNfsMountOptions | None = None
    CreationTime: datetime.datetime | StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
