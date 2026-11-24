from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudWatchLogsEntity(BaseModel):
    keyAttributes: dict[StrictStr, StrictStr] | None = None
    attributes: dict[StrictStr, StrictStr] | None = None
