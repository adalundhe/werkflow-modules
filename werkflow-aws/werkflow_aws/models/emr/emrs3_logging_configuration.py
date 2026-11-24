from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EMRS3LoggingConfiguration(BaseModel):
    LogTypeUploadPolicy: dict[StrictStr, StrictStr] | None = None
