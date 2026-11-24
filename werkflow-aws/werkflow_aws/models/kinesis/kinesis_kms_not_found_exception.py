from __future__ import annotations
from pydantic import BaseModel, StrictStr


class KinesisKMSNotFoundException(BaseModel):
    message: StrictStr | None = None
