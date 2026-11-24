from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConnectTaskAttachment(BaseModel):
    FileName: StrictStr
    S3Url: StrictStr
