from __future__ import annotations
from pydantic import BaseModel, StrictStr


class KinesisInternalFailureException(BaseModel):
    message: StrictStr | None = None
