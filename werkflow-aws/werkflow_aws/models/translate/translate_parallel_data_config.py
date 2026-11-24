from __future__ import annotations
from pydantic import BaseModel, StrictStr


class TranslateParallelDataConfig(BaseModel):
    S3Uri: StrictStr | None = None
    Format: StrictStr | None = None
