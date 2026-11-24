from __future__ import annotations
from pydantic import BaseModel, StrictStr


class TextractOutputConfiguration(BaseModel):
    S3Uri: StrictStr | None = None
