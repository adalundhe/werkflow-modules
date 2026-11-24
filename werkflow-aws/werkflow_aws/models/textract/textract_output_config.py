from __future__ import annotations
from pydantic import BaseModel, StrictStr


class TextractOutputConfig(BaseModel):
    S3Bucket: StrictStr | None = None
    S3Prefix: StrictStr | None = None
