from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SimpleApplicationPropertyBean(BaseModel):
    id: StrictStr | None = None
    value: StrictStr | None = None
