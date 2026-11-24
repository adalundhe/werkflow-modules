from __future__ import annotations
from pydantic import BaseModel, StrictStr


class KinesisVideoStreamStorageConfiguration(BaseModel):
    DefaultStorageTier: StrictStr | None = None
