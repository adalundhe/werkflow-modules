from __future__ import annotations
from pydantic import BaseModel, StrictStr


class KinesisVideoNotificationDestinationConfig(BaseModel):
    Uri: StrictStr | None = None
