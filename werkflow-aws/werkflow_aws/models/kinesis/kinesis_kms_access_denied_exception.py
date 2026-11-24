from __future__ import annotations
from pydantic import BaseModel, StrictStr


class KinesisKMSAccessDeniedException(BaseModel):
    message: StrictStr | None = None
