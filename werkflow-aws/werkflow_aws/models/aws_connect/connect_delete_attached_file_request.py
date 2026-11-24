from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConnectDeleteAttachedFileRequest(BaseModel):
    InstanceId: StrictStr
    FileId: StrictStr
    AssociatedResourceArn: StrictStr
