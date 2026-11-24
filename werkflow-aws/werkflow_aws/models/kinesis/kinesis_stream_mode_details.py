from __future__ import annotations
from pydantic import BaseModel, StrictStr


class KinesisStreamModeDetails(BaseModel):
    StreamMode: StrictStr | None = None
