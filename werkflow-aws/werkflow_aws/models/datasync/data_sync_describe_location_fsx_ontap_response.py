from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr
from .data_sync_fsx_protocol import DataSyncFsxProtocol


class DataSyncDescribeLocationFsxOntapResponse(BaseModel):
    CreationTime: datetime.datetime | StrictStr | None = None
    LocationArn: StrictStr | None = None
    LocationUri: StrictStr | None = None
    Protocol: DataSyncFsxProtocol | None = None
    SecurityGroupArns: list[StrictStr] | None = None
    StorageVirtualMachineArn: StrictStr | None = None
    FsxFilesystemArn: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
