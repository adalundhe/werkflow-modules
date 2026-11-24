from __future__ import annotations
from pydantic import BaseModel, StrictStr


class TextractS3Object(BaseModel):
    Bucket: StrictStr | None = None
    Name: StrictStr | None = None
    Version: StrictStr | None = None
