from __future__ import annotations
from pydantic import BaseModel, StrictStr


class FMSResourceTag(BaseModel):
    Key: StrictStr | None = None
    Value: StrictStr | None = None
