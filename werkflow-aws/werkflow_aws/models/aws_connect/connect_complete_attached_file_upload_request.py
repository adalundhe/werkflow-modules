from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConnectCompleteAttachedFileUploadRequest(BaseModel):
    InstanceId: StrictStr
    FileId: StrictStr
    AssociatedResourceArn: StrictStr
