from __future__ import annotations
from pydantic import BaseModel, StrictStr


class TranslateInputDataConfig(BaseModel):
    S3Uri: StrictStr | None = None
    ContentType: StrictStr | None = None
