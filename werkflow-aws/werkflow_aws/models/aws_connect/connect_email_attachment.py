from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConnectEmailAttachment(BaseModel):
    FileName: StrictStr
    S3Url: StrictStr
