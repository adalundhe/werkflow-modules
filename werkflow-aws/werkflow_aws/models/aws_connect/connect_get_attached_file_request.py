from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class ConnectGetAttachedFileRequest(BaseModel):
    InstanceId: StrictStr
    FileId: StrictStr
    AssociatedResourceArn: StrictStr
    UrlExpiryInSeconds: StrictInt | None = None
    UrlContentDisposition: Literal['INLINE', 'ATTACHMENT'] | None = None
