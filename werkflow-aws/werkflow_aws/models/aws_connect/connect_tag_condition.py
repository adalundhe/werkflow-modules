from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConnectTagCondition(BaseModel):
    TagKey: StrictStr | None = None
    TagValue: StrictStr | None = None
