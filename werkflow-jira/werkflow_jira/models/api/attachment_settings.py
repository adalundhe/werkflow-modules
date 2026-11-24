from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt


class AttachmentSettings(BaseModel):
    enabled: StrictBool | None = None
    uploadLimit: StrictInt | None = None
