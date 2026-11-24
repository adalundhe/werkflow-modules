from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConnectBatchGetAttachedFileMetadataRequest(BaseModel):
    FileIds: list[StrictStr]
    InstanceId: StrictStr
    AssociatedResourceArn: StrictStr
