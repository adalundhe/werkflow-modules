from __future__ import annotations
from pydantic import BaseModel, StrictStr


class KinesisKMSDisabledException(BaseModel):
    message: StrictStr | None = None
