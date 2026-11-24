from __future__ import annotations
from pydantic import BaseModel, StrictStr


class KinesisVideoMediaStorageConfiguration(BaseModel):
    StreamARN: StrictStr | None = None
    Status: StrictStr | None = None
