from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .kms_tag import KMSTag


class KMSTagResourceRequest(BaseModel):
    KeyId: StrictStr
    Tags: list[KMSTag]
