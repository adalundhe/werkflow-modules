from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .data_sync_fsx_update_protocol import DataSyncFsxUpdateProtocol


class DataSyncUpdateLocationFsxOntapRequest(BaseModel):
    LocationArn: StrictStr
    Protocol: DataSyncFsxUpdateProtocol | None = None
    Subdirectory: StrictStr | None = None
