from __future__ import annotations
from pydantic import BaseModel, StrictStr


class KinesisKMSInvalidStateException(BaseModel):
    message: StrictStr | None = None
