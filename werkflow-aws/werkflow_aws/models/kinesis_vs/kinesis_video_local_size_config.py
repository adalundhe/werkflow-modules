from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class KinesisVideoLocalSizeConfig(BaseModel):
    MaxLocalMediaSizeInMB: StrictInt | None = None
    StrategyOnFullSize: StrictStr | None = None
