from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ECRAttribute(BaseModel):
    key: StrictStr | None = None
    value: StrictStr | None = None
