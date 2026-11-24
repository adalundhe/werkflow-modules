from __future__ import annotations
from pydantic import BaseModel, StrictStr


class KinesisKMSThrottlingException(BaseModel):
    message: StrictStr | None = None
