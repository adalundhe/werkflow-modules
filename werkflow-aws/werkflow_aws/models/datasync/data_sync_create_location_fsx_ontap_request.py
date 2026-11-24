from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .data_sync_fsx_protocol import DataSyncFsxProtocol
from .data_sync_tag_list_entry import DataSyncTagListEntry


class DataSyncCreateLocationFsxOntapRequest(BaseModel):
    Protocol: DataSyncFsxProtocol
    SecurityGroupArns: list[StrictStr]
    StorageVirtualMachineArn: StrictStr
    Subdirectory: StrictStr | None = None
    Tags: list[DataSyncTagListEntry] | None = None
