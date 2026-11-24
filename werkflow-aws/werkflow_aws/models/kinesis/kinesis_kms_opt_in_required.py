from __future__ import annotations
from pydantic import BaseModel, StrictStr


class KinesisKMSOptInRequired(BaseModel):
    message: StrictStr | None = None
