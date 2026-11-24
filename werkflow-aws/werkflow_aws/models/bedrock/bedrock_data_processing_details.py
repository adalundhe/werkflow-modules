from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class BedrockDataProcessingDetails(BaseModel):
    status: StrictStr | None = None
    creationTime: datetime.datetime | StrictStr | None = None
    lastModifiedTime: datetime.datetime | StrictStr | None = None
