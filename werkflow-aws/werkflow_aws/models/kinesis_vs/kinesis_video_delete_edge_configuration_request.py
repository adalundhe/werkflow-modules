from __future__ import annotations
from pydantic import BaseModel, StrictStr


class KinesisVideoDeleteEdgeConfigurationRequest(BaseModel):
    StreamName: StrictStr | None = None
    StreamARN: StrictStr | None = None
