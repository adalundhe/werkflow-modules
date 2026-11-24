from __future__ import annotations
from pydantic import BaseModel, StrictStr


class TextractInputConfiguration(BaseModel):
    S3Uri: StrictStr
