from __future__ import annotations
from pydantic import BaseModel, StrictStr


class KinesisResourceNotFoundException(BaseModel):
    message: StrictStr | None = None
