from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudWatchTag(BaseModel):
    Key: StrictStr | None = None
    Value: StrictStr | None = None
