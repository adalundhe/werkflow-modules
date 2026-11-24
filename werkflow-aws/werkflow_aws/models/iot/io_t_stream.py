from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class IoTStream(BaseModel):
    streamId: StrictStr | None = None
    fileId: StrictInt | None = None
