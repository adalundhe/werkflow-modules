from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ResilienceHubS3Location(BaseModel):
    bucket: StrictStr | None = None
    prefix: StrictStr | None = None
