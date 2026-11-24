from __future__ import annotations
from pydantic import BaseModel, StrictStr


class KinesisVideoTag(BaseModel):
    Key: StrictStr
    Value: StrictStr
