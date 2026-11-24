from __future__ import annotations
from pydantic import BaseModel, StrictStr


class KinesisVideoImageGenerationDestinationConfig(BaseModel):
    Uri: StrictStr | None = None
    DestinationRegion: StrictStr | None = None
