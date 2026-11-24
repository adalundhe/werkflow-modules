from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .data_sync_fsx_protocol import DataSyncFsxProtocol


class DataSyncUpdateLocationFsxOpenZfsRequest(BaseModel):
    LocationArn: StrictStr
    Protocol: DataSyncFsxProtocol | None = None
    Subdirectory: StrictStr | None = None
