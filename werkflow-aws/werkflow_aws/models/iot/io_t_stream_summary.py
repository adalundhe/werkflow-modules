from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class IoTStreamSummary(BaseModel):
    streamId: StrictStr | None = None
    streamArn: StrictStr | None = None
    streamVersion: StrictInt | None = None
    description: StrictStr | None = None
