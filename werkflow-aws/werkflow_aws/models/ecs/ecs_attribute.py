from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ECSAttribute(BaseModel):
    name: StrictStr | None = None
    value: StrictStr | None = None
    targetType: StrictStr | None = None
    targetId: StrictStr | None = None
